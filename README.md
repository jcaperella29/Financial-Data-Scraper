📜 Updated README for Financial Data Scraper 🚀💰
📌 Overview
This project is a multi-company web scraping utility built using Python and Selenium to extract financial data from Stock Analysis. It navigates through financial tabs for multiple companies—including Income Statement, Balance Sheet, Cash Flow, and Ratios—and saves the extracted data as CSV files.

🔥 New Feature:

Users can now provide stock tickers & URLs in a CSV file (tickers.csv), eliminating the need to modify the script manually.
A sample tickers.csv file is included to help users get started quickly.
⚡ Features
✅ Supports multiple stock symbols (e.g., GM, AAPL, TSLA).
✅ Reads stock tickers & URLs from tickers.csv (no need to edit the script).
✅ Scrapes key financial data from multiple tabs:

📄 Income Statement (default tab)
📊 Balance Sheet
💰 Cash Flow
📈 Ratios
✅ Saves extracted data into CSV files (e.g., AAPL_income_statement.csv).
✅ Logs progress & handles errors gracefully 🛡
✅ Captures debugging screenshot (page_debug.png) 🖼️
🔧 Requirements
📌 Python 3.7+
📌 Selenium 4+
📌 Firefox Browser
📌 GeckoDriver (Ensure it's in your PATH or provide the full path).

📥 Installation
1️⃣ Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/financial-data-scraper.git
cd financial-data-scraper
2️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Download and install:

🔹 Firefox Browser
🔹 GeckoDriver
🚀 Usage
1️⃣ Edit tickers.csv to Add Companies
Instead of modifying Python code, simply edit tickers.csv with stock symbols and their corresponding URLs.

📄 Example tickers.csv (included in the repo):

csv
Copy
Edit
ticker,url
GM,https://stockanalysis.com/stocks/gm/financials/
AAPL,https://stockanalysis.com/stocks/aapl/financials/
TSLA,https://stockanalysis.com/stocks/tsla/financials/
MSFT,https://stockanalysis.com/stocks/msft/financials/
2️⃣ Run the script
bash
Copy
Edit
python scraper.py
3️⃣ View results
Extracted CSV files will be saved inside the financial_data/ folder.

📂 File Structure
bash
Copy
Edit
financial-data-scraper/
├── financial_data/             # Output folder for CSV files
│   ├── GM_income_statement.csv  # GM Income Statement
│   ├── AAPL_balance_sheet.csv   # AAPL Balance Sheet
│   ├── TSLA_cash_flow.csv       # TSLA Cash Flow
│   └── ... (more files)
├── tickers.csv                 # User-provided ticker/URL input (new feature!)
├── scraper.py                  # Main scraper script
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── page_debug.png              # Debugging screenshot
⚠ Notes
🔹 Income Statement is preloaded when the page loads, so no click is needed for it.
🔹 JavaScript fallback clicking is used if normal Selenium clicks fail.
🔹 If the website structure changes, XPath adjustments may be needed.

🛠 Troubleshooting
❌ Browser Not Found → Verify FIREFOX_BINARY_PATH in the script.
❌ Version Mismatch → Ensure Firefox & GeckoDriver versions are compatible.
❌ Timeout Errors → Increase Selenium WebDriverWait timeout values.

🎯 Future Enhancements
🔜 Automatic detection of new stock listings
🔜 Multi-threading for faster data extraction
🔜 Database integration to store financial data

🎉 Now users can easily scrape financials by just updating a CSV! 🚀📊💰
