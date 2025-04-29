## Data extraction of company data source with Python

## Overview

This project automates the extraction of key financial data-specifically, **revenue**-from the latest 10-K filings of S&P 500 companies...

## Features

- **Automated company list fetching:** ...
- **SEC filings integration:** ...
- **Robust revenue extraction:** ...
- **Industry classification:** ...
- **Clean, structured output:** ...


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


## Note

1. **Note on API Limits**
    - Due to the sec-api.io free tier rate limits, I was able to extract and process data for only 15 companies in this project run. For larger-scale or more frequent data extraction, we have to consider upgrading to a paid plan with higher request quotas and additional features.
    - References:
        - The free tier of sec-api.io has request and data volume limits.
        - The SEC’s own EDGAR system also enforces rate limits on automated requests.
