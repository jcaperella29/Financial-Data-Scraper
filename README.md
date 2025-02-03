# Financial-Data-Scraper

Financial Data Scraper 🧾🚀
Overview
This project is a web scraping utility built using Python and Selenium to extract financial data from Stock Analysis for a specific company (e.g., General Motors). It navigates through different financial tabs—Income Statement, Balance Sheet, Cash Flow, and Ratios—to save the data as CSV files for further analysis.

Features
📄 Extracts data from the following financial tabs:
Income Statement (default tab on page load)
Balance Sheet
Cash Flow
Ratios
💾 Saves each table as a separate CSV file.
🖼️ Captures a debugging screenshot of the webpage.
📜 Logs progress and errors for easy debugging.
Requirements
Python 3.7+
Selenium 4+
Firefox Browser
GeckoDriver (Ensure it's in your PATH or provide the full path).
Installation
Clone this repository:
bash
Copy
Edit
git clone https://github.com/yourusername/financial-data-scraper.git
cd financial-data-scraper
Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Download and install:
Firefox Browser: Download Firefox
GeckoDriver: Download GeckoDriver
Usage
Update paths in the script:
geckodriver_path: Path to your GeckoDriver executable.
firefox_binary_path: Path to your Firefox installation.
Run the script:
bash
Copy
Edit
python scraper.py
CSV files will be saved in the financial_data directory.
File Structure
bash
Copy
Edit
financial-data-scraper/
├── financial_data/             # Output folder for CSV files
│   ├── income_statement.csv    # Income Statement data
│   ├── balance_sheet.csv       # Balance Sheet data
│   ├── cash_flow.csv           # Cash Flow data
│   └── ratios.csv              # Ratios data
├── scraper.py                  # Main script
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── page_debug.png              # Debugging screenshot
Notes
The Income Statement tab is the default open tab on the financials page, so no clicking is performed for this tab.
JavaScript-based clicking is used as a fallback for navigating other tabs if standard Selenium clicks fail.
Ensure the website structure has not changed; otherwise, updates to XPaths might be required.
Troubleshooting
Browser not found: Check the firefox_binary_path in the script.
Version mismatch: Ensure Firefox and GeckoDriver versions are compatible.
Timeout errors: Increase the WebDriverWait timeouts in the script.
