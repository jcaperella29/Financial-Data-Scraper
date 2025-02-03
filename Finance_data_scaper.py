from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import time

# Path to GeckoDriver and Firefox Binary
geckodriver_path = r"C:\Users\ccape\Downloads\geckodriver-v0.35.0-win32\geckodriver.exe"
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"

# Define the output directory
output_dir = "financial_data"
os.makedirs(output_dir, exist_ok=True)

# Configure Firefox Options
options = Options()
options.binary_location = firefox_binary_path

# Initialize WebDriver for Firefox
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

# Define the website and tabs to scrape
url = "https://stockanalysis.com/stocks/gm/financials/"
tabs = {
    # Skipping click for Income Statement as it's the default open tab
    "Balance Sheet": "//a[contains(text(), 'Balance Sheet')]",
    "Cash Flow": "//a[contains(text(), 'Cash Flow')]",
    "Ratios": "//a[contains(text(), 'Ratios')]"
}

try:
    # 🌐 Open the Website
    print("🌐 Opening the website...")
    driver.get(url)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("✅ Page loaded successfully.")

    # 📸 Capture Debugging Screenshot
    driver.save_screenshot("page_debug.png")
    print("📸 Saved screenshot as 'page_debug.png'")

    # Handle the Income Statement directly (default tab)
    print("📄 Processing tab: Income Statement (default tab)...")
    try:
        table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@data-test='financials']")))
        print(f"✅ Table found for Income Statement")

        # Extract table rows
        rows = table.find_elements(By.XPATH, ".//tr")
        table_data = []
        for row in rows:
            cells = row.find_elements(By.XPATH, ".//th | .//td")
            table_data.append([cell.text for cell in cells])

        # Convert to DataFrame
        df = pd.DataFrame(table_data[1:], columns=table_data[0])
        print(f"📊 Data extracted for Income Statement:\n", df.head())

        # Save to CSV
        output_file = os.path.join(output_dir, "income_statement.csv")
        df.to_csv(output_file, index=False)
        print(f"💾 Data saved to {output_file}\n")

    except Exception as e:
        print(f"❌ Failed to extract table for Income Statement. Error: {e}")

    # Loop through remaining tabs and extract the table data
    for tab_name, tab_xpath in tabs.items():
        print(f"📄 Navigating to tab: {tab_name}...")

        # Try clicking the tab with different methods
        try:
            # 🔄 Scroll into view
            tab_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, tab_xpath)))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", tab_element)
            time.sleep(1)  # Small delay to allow rendering

            # 🖱️ Click using Selenium
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, tab_xpath))).click()
            print(f"✅ Clicked on {tab_name}")

        except Exception as e:
            print(f"⚠️ Regular click failed for {tab_name}. Trying JavaScript click...")
            try:
                driver.execute_script("arguments[0].click();", tab_element)
                print(f"✅ JavaScript click successful for {tab_name}")
            except Exception as js_error:
                print(f"❌ JavaScript click failed for {tab_name}. Skipping tab. Error: {js_error}")
                continue  # Skip to the next tab

        time.sleep(2)  # Allow time for the table to load

        # Locate the financial table
        try:
            table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@data-test='financials']")))
            print(f"✅ Table found for {tab_name}")

            # Extract table rows
            rows = table.find_elements(By.XPATH, ".//tr")
            table_data = []
            for row in rows:
                cells = row.find_elements(By.XPATH, ".//th | .//td")
                table_data.append([cell.text for cell in cells])

            # Convert to DataFrame
            df = pd.DataFrame(table_data[1:], columns=table_data[0])
            print(f"📊 Data extracted for {tab_name}:\n", df.head())

            # Save to CSV
            output_file = os.path.join(output_dir, f"{tab_name.replace(' ', '_').lower()}.csv")
            df.to_csv(output_file, index=False)
            print(f"💾 Data saved to {output_file}\n")

        except Exception as e:
            print(f"❌ Failed to extract table for {tab_name}. Error: {e}")
            continue  # Skip to the next tab

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    driver.quit()
    print("🚪 Browser closed.")
