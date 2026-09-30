import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://coinmarketcap.com/"
CSV_FILE = "crypto_prices.csv"

def get_driver():
    options = Options()
    # options.add_argument("--headless") # Keep it OFF first to see if it works
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def scrape_data():
    driver = get_driver()
    driver.get(URL)

    print("Waiting for table to load...")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.XPATH, "//table/tbody/tr")))

    time.sleep(3)
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    print(f"Found {len(rows)} rows")

    all_coins = []
    for row in rows[:10]:
        try:
            # More stable selectors
            name = row.find_element(By.XPATH, ".//td[3]//p[contains(@class,'coin-item-name') or contains(@class,'sc-')]").text
            if not name:
                name = row.find_element(By.XPATH, ".//td[3]").text.split('\n')[0]

            price = row.find_element(By.XPATH, ".//td[4]").text
            change = row.find_element(By.XPATH, ".//td[5]").text
            market_cap = row.find_element(By.XPATH, ".//td[7]").text

            all_coins.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, price, change, market_cap])
        except Exception as e:
            print(f"Skipping a row: {e}")
            continue

    driver.quit()
    return all_coins

def save_to_csv(data):
    if not data:
        print("Still no data - CoinMarketCap may be showing a Cloudflare check. Try running without headless.")
        return
    df_new = pd.DataFrame(data, columns=["Timestamp", "Coin_Name", "Price", "24h_Change", "Market_Cap"])
    print(df_new)
    try:
        df_old = pd.read_csv(CSV_FILE)
        df_final = pd.concat([df_old, df_new], ignore_index=True)
    except FileNotFoundError:
        df_final = df_new
    df_final.to_csv(CSV_FILE, index=False)
    print(f"Saved to {CSV_FILE}")

if __name__ == "__main__":
    data = scrape_data()
    save_to_csv(data)