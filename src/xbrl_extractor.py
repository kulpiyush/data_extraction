# src/xbrl_extractor.py

from src.sec_api import get_all_revenue_facts_from_sec

def extract_revenue_from_xbrl(filing_url):
    """
    Updated to use SEC API instead of sec-api.io
    """
    # Get CIK from URL (example: .../data/320193/... -> CIK=0000320193)
    cik = filing_url.split('/data/')[1].split('/')[0].zfill(10)
    
    revenue, currency = get_all_revenue_facts_from_sec(cik)
    
    if revenue:
        return float(revenue), currency
    return None, None