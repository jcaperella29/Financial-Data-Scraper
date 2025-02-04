📜 Updated README for Financial Data Scraper 🚀💰
📌 Overview
This project is a multi-company web scraping utility built using Python and Selenium to extract financial data from Stock Analysis. It navigates through financial tabs for multiple companies—including Income Statement, Balance Sheet, Cash Flow, and Ratios—and saves the extracted data as CSV files.

⚡ Features
✅ Supports multiple stock symbols (e.g., GM, AAPL, TSLA).
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
1️⃣ Update paths in the script
Open scraper.py and modify:

GECKODRIVER_PATH: Path to your GeckoDriver executable.
FIREFOX_BINARY_PATH: Path to your Firefox installation.
2️⃣ Define companies to scrape
Modify the companies dictionary inside main():

python
Copy
Edit
companies = {
    "GM": "https://stockanalysis.com/stocks/gm/financials/",
    "AAPL": "https://stockanalysis.com/stocks/aapl/financials/",
    "TSLA": "https://stockanalysis.com/stocks/tsla/financials/",
}
3️⃣ Run the script
bash
Copy
Edit
python scraper.py
4️⃣ View results
Extracted CSV files will be saved inside the financial_data/ folder.

📂 File Structure
bash
Copy
Edit
financial-data-scraper/
├── financial_data/             # Output folder for CSV files
│   ├── GM_income_statement.csv  # GM Income Statement
│   ├── GM_balance_sheet.csv     # GM Balance Sheet
│   ├── AAPL_income_statement.csv # AAPL Income Statement
│   ├── TSLA_cash_flow.csv        # TSLA Cash Flow
│   └── ... (more files)
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
🔜 User input for stock symbols instead of hardcoded list.
🔜 Multi-threading for faster data extraction.
🔜 Database integration to store financial data.
