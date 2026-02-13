# 🛒 Kroger Price Tracker for Home Assistant (v0.2.4)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
![HA Version](https://img.shields.io/badge/Home%20Assistant-2025.1+-blue.svg)

Hey everyone! This is my first ever public integration. I built this because my partner is a major deal hunter and I thought this may help her compare prices. I'm also working on a Dollar General price tracker as well that will be paired with this. 

It’s built for **Home Assistant OS** and handles the Kroger API's weird "Yellow Tag" sale logic so you always see the actual price you'll pay at the register.

---

## 🚀 How to Get Started

### 1. Grab your Kroger API Keys
Kroger doesn't just hand these out, you have to "create an app" on their site (don't worry, it's free):
* Go to the [Kroger Developer Portal](https://developer.kroger.com/).
* Sign up and create an **Organization**.
* Go to **My Apps > Register App**.
* **Name:** "HA Price Tracker" (or whatever you want).
* **Scopes:** You **MUST** check the `product.compact` scope.
* **Redirect URL:** Use `http://localhost`.
* Copy your **Client ID** and **Client Secret**.

### 2. Find your Store ID (Location ID)
Prices change depending on which store you're at. 
* Go to the [Kroger Store Locator](https://www.kroger.com/stores/search).
* Find your local store.
* Look at the URL or the store details. You’re looking for a **Store Number** (usually 8 digits, e.g., `02100902`). There will be a slash in the middle of it seperating the district number from the store number, but we need the whole thing, just take out the slash.

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
* [ ] **HACS Default:** Get this listed in the official HACS store.
* [ ] **Price Drop Logic:** Native binary sensors to show if an item is currently "On Sale."
* [ ] **Unit Pricing:** Track price per ounce/pound for better comparison.

---

## 🤝 Contributing
If you have ideas or found a bug, please open an issue! I'm still learning the ropes of HA integration development, so any help is welcome.

---
*Developed with ☕ and drywall dust in Peru, IN.*
