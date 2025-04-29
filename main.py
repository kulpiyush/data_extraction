# src/main.py

from src.data_fetcher import get_sp500_companies
from src.filing_fetcher import get_latest_10k_filings
from src.xbrl_extractor import extract_revenue_from_xbrl
from src.config import SEC_API_KEY
from src.data_cleaner import clean_data
from src.exporter import export_to_excel
import pandas as pd
import time

def main():
    companies_df = get_sp500_companies()
    results = []
    for idx, row in companies_df.iterrows():
        ticker = row['ticker']
        print(f"Processing {ticker} ({idx+1}/{len(companies_df)})...")
        filings = get_latest_10k_filings(ticker)
        for filing in filings:
            year = filing.get('periodOfReport', '')[:4]
            company_name = filing.get('companyName', '')
            industry = row['gics_sector']           # Use from S&P 500 list
            country = filing.get('stateOfIncorporation', 'USA')
            filing_url = filing['linkToFilingDetails']

            revenue, revenue_unit = extract_revenue_from_xbrl(filing_url, SEC_API_KEY)
            if revenue is not None:
                results.append({
                    "timevalue": year,
                    "companyname": company_name,
                    "industryclassification": industry,
                    "geonameen": country,
                    "revenue": revenue,
                    "revenue_unit": revenue_unit
                })
            else:
                print(f"Revenue not found for {ticker} {year}.")
        time.sleep(0.5)
        if idx >= 15:  # For testing, limit to 100 companies
            break

    final_df = clean_data(pd.DataFrame(results))
    export_to_excel(final_df, "/Users/piyushkulkarni/Desktop/statista_task/data/CaseStudy_Sourcing_sample-1.xlsx")

if __name__ == "__main__":
    main()
