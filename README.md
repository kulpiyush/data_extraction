## Data extraction of company data source with Python

## Overview

This project automates the extraction of key financial data-specifically, revenue-from the latest 10-K filings of S&P 500 companies using only free and public SEC APIs. The output is a clean, structured Excel file suitable for analysis.

## Features

- **Automated company list fetching:** Automated company list fetching: Scrapes the latest S&P 500 company list from Wikipedia, including ticker, company name, GICS sector, and CIK.
- **Direct SEC EDGAR integration:** Retrieves recent 10-K filings for each company directly from the SEC EDGAR system.
- **Accurate, per-year revenue extraction:** Extracts all available revenue facts from the SEC XBRL API and matches each value to the correct fiscal year for every company.
- **Industry classification:** Each company’s GICS sector is included for industry-level analysis.
- **Clean, structured output:** Cleans the collected data and exports it to Excel for easy review and downstream use.


## How It Works

1. **Fetch S&P 500 Companies**
    - Scrapes Wikipedia for the most current list of S&P 500 companies, including ticker, company name, GICS sector, and CIK.
2. **Get Latest 10-K Filings**
    - For each company, queries the SEC EDGAR system to find recent 10-K filings.
3. **Extract Revenue Datas**
    - Uses the SEC XBRL company-concept API to extract all available revenue facts for each company, then matches each revenue value to the correct fiscal year using the filing metadata.
4. **Join Industry Classification**
    - Each company’s GICS sector is included for industry-level analysis.
5. **Clean and Export**
    - Cleans the collected data and exports it to Excel for easy review and downstream use.


## Note

1. **No API Key or Paid Plan Needed**
    - This project does not require sec-api.io or any paid API. All data is sourced directly from the official SEC EDGAR APIs, which are free to use.

2. **References:**
    - SEC EDGAR Submissions API
    - SEC XBRL Company Concept API

3. **Directory Structure:**
````
├── .gitignore
├── data
│   └── CaseStudy_Sourcing_sample-1.xlsx
├── main.py
├── README.md
├── requirements.txt
└── src
    ├── __init__.py
    ├── __pycache__
    ├── data_cleaner.py
    ├── data_fetcher.py
    ├── exporter.py
    ├── filing_fetcher.py
    ├── sec_api.py
    └── xbrl_extractor.py
````