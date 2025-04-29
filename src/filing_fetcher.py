# src/filing_fetcher.py

from sec_api import QueryApi
from src.config import SEC_API_KEY, NUM_FILINGS

queryApi = QueryApi(api_key=SEC_API_KEY)

def get_latest_10k_filings(ticker, num_filings=NUM_FILINGS):
    """
    Fetches the latest 10-K filings metadata for a given ticker.
    
    Args:
        ticker (str): Stock ticker symbol.
        num_filings (int): Number of filings to fetch.
        
    Returns:
        list: List of filings metadata dictionaries.
    """
    query = {
        "query": f"ticker:{ticker} AND formType:\"10-K\"",
        "from": "0",
        "size": str(num_filings),
        "sort": [{"filedAt": {"order": "desc"}}]
    }
    try:
        response = queryApi.get_filings(query)
        return response.get('filings', [])
    except Exception as e:
        print(f"[ERROR] Failed to fetch filings for {ticker}: {e}")
        return []
    

