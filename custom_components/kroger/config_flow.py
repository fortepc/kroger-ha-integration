"""Config flow for Kroger Price Tracker integration."""
import voluptuous as vol
from homeassistant.config_entries import ConfigFlow, OptionsFlowWithReload, ConfigEntry
from homeassistant.core import callback

DOMAIN = "kroger"

class KrogerConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Kroger Price Tracker."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial setup."""
        if user_input is not None:
            return self.async_create_entry(
                title=f"Store {user_input['store_id']}", 
                data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("client_id"): str,
                vol.Required("client_secret"): str,
                vol.Required("store_id"): str,
                vol.Required("upc_list"): str,
            })
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> "KrogerOptionsFlowHandler":
        """Get the options flow handler."""
        return KrogerOptionsFlowHandler()


class KrogerOptionsFlowHandler(OptionsFlowWithReload):
    """Handle the options flow via the Configure button."""

    async def async_step_init(self, user_input=None):
        """Manage the UPC list."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Access existing data safely from the managed self.config_entry
        # Use .options first (UI edits), then .data (Initial setup)
        current_upcs = self.config_entry.options.get(
            "upc_list", self.config_entry.data.get("upc_list", "")
        )

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required("upc_list", default=current_upcs): str,
            }),
        )