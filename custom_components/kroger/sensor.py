import logging
import aiohttp
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(hours=4)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Kroger sensors from a config entry."""
    # Logic: Prefer 'options' (edited via UI), fallback to 'data' (initial setup)
    upc_string = entry.options.get("upc_list", entry.data.get("upc_list", ""))
    
    client_id = entry.data["client_id"]
    client_secret = entry.data["client_secret"]
    store_id = entry.data["store_id"]
    
    upcs = [upc.strip() for upc in upc_string.split(",")]

    entities = []
    for upc in upcs:
        entities.append(KrogerSensor(upc, client_id, client_secret, store_id))
    
    async_add_entities(entities, True)

class KrogerSensor(SensorEntity):
    """Kroger Sensor with 'Yellow Tag' Logic."""

    def __init__(self, upc, client_id, client_secret, store_id):
        self._upc = upc
        self._client_id = client_id
        self._client_secret = client_secret
        self._store_id = store_id
        self._state = None
        self._product_name = None
        self._attributes = {}
        self._token = None

        self.entity_id = f"sensor.kroger_{store_id}_{upc}"
        self._attr_unique_id = f"kroger_{store_id}_{upc}"
        self._attr_native_unit_of_measurement = "USD"
        self._attr_device_class = SensorDeviceClass.MONETARY
        self._attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def name(self):
        return self._product_name or f"Kroger {self._upc}"

    @property
    def native_value(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    async def _get_token(self, session):
        url = "https://api.kroger.com/v1/connect/oauth2/token"
        auth = aiohttp.BasicAuth(self._client_id, self._client_secret)
        data = {"grant_type": "client_credentials", "scope": "product.compact"}
        async with session.post(url, auth=auth, data=data) as resp:
            res = await resp.json()
            return res.get("access_token")

    async def async_update(self):
        """Fetch and process price data."""
        session = async_get_clientsession(self.hass)
        if not self._token:
            self._token = await self._get_token(session)

        url = f"https://api.kroger.com/v1/products/{self._upc}?filter.locationId={self._store_id}"
        headers = {"Authorization": f"Bearer {self._token}", "Accept": "application/json"}

        try:
            async with session.get(url, headers=headers) as resp:
                if resp.status == 401:
                    self._token = await self._get_token(session)
                    return await self.async_update()
                
                data = await resp.json()
                product = data["data"]
                item = product["items"][0]
                
                self._product_name = product.get("description")

                reg = item.get("price", {}).get("regular", 0)
                promo = item.get("price", {}).get("promo", 0)
                fulfillment_promo = item.get("fulfillment", {}).get("instore", {}).get("price", {}).get("promo", 0)
                
                actual_promo = max(promo, fulfillment_promo)
                self._state = actual_promo if actual_promo > 0 else reg

                self._attributes["regular_price"] = reg
                self._attributes["promo_price"] = actual_promo
                self._attributes["snap_eligible"] = product.get("snapEligible", False)

        except Exception as e:
            _LOGGER.error("Error updating Kroger sensor %s: %s", self._upc, e)