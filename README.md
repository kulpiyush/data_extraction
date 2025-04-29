## Data extraction of company data source with Python

## Overview

This project automates the extraction of key financial data-specifically, **revenue**-from the latest 10-K filings of S&P 500 companies...

## Features

- **Automated company list fetching:** ...
- **SEC filings integration:** ...
- **Robust revenue extraction:** ...
- **Industry classification:** ...
- **Clean, structured output:** ...

## Directory Structure
STATISTA_TASK/
│
├── data/
│   ├── CaseStudy_Sourcing_sample-1.xlsx  # Provided Excel template
│  
│   
│
├── src/
│   ├── config.py                 # API keys and constants
│   ├── data_fetcher.py           # Fetches S&P 500 list with GICS sector
│   ├── filing_fetcher.py         # Gets latest 10-K filings metadata
│   ├── xbrl_extractor.py         # Extracts revenue from filings via API
│   ├── data_cleaner.py           # Cleans and standardizes data
│   ├── exporter.py               # Exports DataFrame to Excel
│   └── main.py                   # Main pipeline script
│
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── .gitignore                    # Standard Python ignores

## How It Works

1. **Fetch S&P 500 Companies**
    - Scrapes Wikipedia for the most current list of S&P 500 companies, including ticker, company name, and GICS sector.
2. **Get Latest 10-K Filings**
    - For each company, queries the SEC EDGAR system to find the most recent 10-K filing.
3. **Extract Revenue Datas**
    - Uses the sec-api XBRL-to-JSON Converter to extract standardized revenue figures from each filing.
4. **Join Industry Classification**
    - Each company’s GICS sector is included for industry-level analysis.
5. **Clean and Export**
    - Cleans the collected data and exports it to Excel for easy review and downstream use.
