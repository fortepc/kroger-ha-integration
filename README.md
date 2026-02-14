# 🛒 Kroger Price Tracker for Home Assistant (v0.2.4)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
![HA Version](https://img.shields.io/badge/Home%20Assistant-2025.1+-blue.svg)

This is my first ever public integration. I built this because my partner is a major bargain hunter and I thought I could make her a better way to track grocery and supply prices without checking 50 different apps. I also have a Dollar General price tracker in progress but it's not been reliable enough to publish yet and is a pain to update the tracked products. Once that's working reliably you can expect that to be published too.

It's built to grab the current price, including showing when there's some kind of promotional deal, and some extra metadata for the entity to have as attributes to make some custom markdown cards useful. 

---

## 🚀 How to Get Started

### 1. Grab your Kroger API Keys
Kroger has an API for this, and all you have to is "create an app" on their site (don't worry, it's free). Follow these steps to get through their registration forms:

* **Go to:** [Kroger Developer Portal](https://developer.kroger.com/).
* **Sign up** and create an **Organization**.
* **Go to:** **My Apps > Register App**.

#### Page 1: App Information
Kroger will ask you several questions. Here is how to answer them:

| Question | What to enter/select |
| :--- | :--- |
| **Who will be using these credentials?** | Select **Personal App**. |
| **Application Name** | Pick something unique (e.g., "My Home Price Watcher"). |
| **App Description** | A quick sentence like: "Tracking grocery prices for my Home Assistant dashboard." |
| **Support Email Address** | Enter your own email address where you can receive API updates. |
| **Environment** | Select **Production**. This ensures you are getting live, real-world pricing. |
| **API Products** | **CRITICAL:** You must select **Product Search** (this gives you the `product.compact` scope). I'd also recomend including Locations so future versions of this integration may be able to find your Store ID automatically |

#### Page 2: Additional Information
* **Everything on this page is Optional.** You can leave the Homepage, Logo, Redirect URI, and Policy links **completely blank**.
* Just hit **Save** or **Finish** at the bottom!

### 2. Find your Store ID (Location ID)
Prices change depending on which store you're at. 
* Go to the [Kroger Store Locator](https://www.kroger.com/stores/search).
* Find your local store.
* Look at the URL or the store details. You’re looking for a string of numbers with / in it. Before the slash is a district number of some kind, and after the slash is the **Store Number**. For Store ID we need to combine both of those into 1 string. For example, if the URL is https://www.kroger.com/stores/grocery/in/peru/peru-kroger/012/00345 then the Store ID we need for the integration would be `01200345`.

### 3. Find Product UPCs
This is the "ID" for the food/items you want to track.
* Search for a product on Kroger.com.
* Click the item to open its page.
* Look at the URL. The UPC is the long string of numbers at the end.
* *Example:* In `.../p/milk/0001111040101`, the UPC is `0001111040101`.

---

## 🛠 Installation

1. **HACS:** Add this URL as a **Custom Repository** under the "Integration" category.
2. **Setup:** Go to **Settings > Devices & Services > Add Integration** and search for **Kroger**.
3. **Configure:** Enter your ID, Secret, Store ID, and a list of UPCs (comma-separated).

---

## 📝 The To-Do List (Future Improvements)
This is just the start! Here’s what I’m planning to add:
* [ ] **Expand Attributes:** Add a checklist in the UI to choose more data (Brand, Categories, Size, etc.).
* [ ] **Automatic Store Locator:** Give users the option to automatically use the Kroger location closest to their Home Assistant instance location.
* [ ] **HACS Default:** Get this listed in the official HACS store.
* [ ] **Price Drop Logic:** Native binary sensors to show if an item is currently "On Sale."
* [ ] **Unit Pricing:** Track price per ounce/pound for better comparison.

---

## 🤝 Contributing
If you have ideas or found a bug, please open an issue! I'm still learning the ropes of HA integration development, so any help is welcome.

---
*Developed with ☕ and drywall dust in Peru, IN.*