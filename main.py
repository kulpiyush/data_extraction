from src.data_fetcher import get_sp500_companies
from src.filing_fetcher import get_latest_10k_filings
from src.sec_api import get_all_revenue_facts_from_sec  # <-- Use this function!
from src.data_cleaner import clean_data
from src.exporter import export_to_excel
import pandas as pd
import time

def main():
    companies_df = get_sp500_companies()
    results = []
    for idx, row in companies_df.iterrows():
        ticker = row['ticker']
        cik = row['cik']
        print(f"Processing {ticker} ({idx+1}/{len(companies_df)})...")

        # 1. Fetch all revenue facts for this company (once per company)
        all_revenue_facts = get_all_revenue_facts_from_sec(cik)

        # 2. Fetch filings for this company
        filings = get_latest_10k_filings(ticker, cik=cik)
        for filing in filings:
            year = filing.get('periodOfReport', '')[:4]
            if not year:
                # Fallback: try filingDate if periodOfReport is missing
                year = filing.get('filingDate', '')[:4]
            company_name = row['company_name']
            industry = row['gics_sector']
            country = filing.get('stateOfIncorporation', 'USA')

            # 3. Find the revenue fact for this year
            revenue = None
            revenue_unit = None
            for fact in all_revenue_facts:
                if fact['end'][:4] == year:
                    revenue = fact['value']
                    revenue_unit = fact['currency']
                    break

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
        if idx >= 500:  # For testing, limit to 101 companies
            break

    final_df = clean_data(pd.DataFrame(results))
    export_to_excel(final_df, "/Users/piyushkulkarni/Desktop/statista_task/data/CaseStudy_Sourcing_sample-1.xlsx")

if __name__ == "__main__":
    main()
