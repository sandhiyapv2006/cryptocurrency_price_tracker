# Cryptocurrency Price Tracker - Mini Project 1

## 📘 PROJECT DESCRIPTION
The Cryptocurrency Price Tracker is a Selenium-powered Python tool that dynamically scrapes real-time cryptocurrency prices from CoinMarketCap. It collects essential details such as coin name, current price, 24-hour change, and market cap.

It automates browser interaction using Chrome WebDriver to load JavaScript-based pages and extract accurate market data.

## ✨ FEATURES
1. **Live Price Scraping** - Scrapes real-time prices and market data
2. **Dynamic Page Handling** - Uses Selenium WebDriver for JavaScript pages
3. **Top 10 Coins Data** - Extracts coin name, price, 24h change, market cap
4. **CSV Export** - Saves data into structured CSV file
5. **Headless Browser Option** - Run in background without opening browser
6. **Historical Logging** - Appends timestamped data for trend tracking
7. **Filtering** - Filter by price threshold or highest 24h gainers

## 🛠 TECHNOLOGIES USED
- **Python** - Primary language
- **Libraries:**
    - Selenium - Dynamic scraping and browser control
    - pandas - Data manipulation and export
    - webdriver_manager - Auto manage ChromeDriver
    - time - Delays and timestamps
- **Browser Automation:** Google Chrome + ChromeDriver
- **Data Storage:** CSV format

## 📊 OUTCOMES
1. Real-Time Market Monitoring
2. Trend Analysis with historical data
3. Custom Alert and Filtering Logic
4. Dashboard Ready data for visualization
5. Portfolio Tracking for investors

## 📂 Files in this Repo
- `cryptocurrency_tracker.py` - Main source code
- `crypto_prices.csv` - Output data
- `Cryptocurrency_Price_Tracker_Project_Report.pdf` - Project Report

## ▶️ How to Run
```bash
pip install selenium pandas webdriver-manager
python cryptocurrency_tracker.py
