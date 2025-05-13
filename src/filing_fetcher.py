# src/filing_fetcher.py

import requests

def get_latest_10k_filings(ticker, cik=None, count=5):
    """
    Fetches the latest 10-K filings for a company using SEC EDGAR API.
    Args:
        ticker (str): Ticker symbol (not used here, but kept for compatibility)
        cik (str): 10-digit CIK string
        count (int): Number of filings to return
    Returns:
        List of dicts: Each dict contains 'periodOfReport', 'stateOfIncorporation', 'linkToFilingDetails'
    """
    if cik is None:
        raise ValueError("CIK must be provided for SEC API access.")

    headers = {
        'User-Agent': 'Statista Case Study Extractor kulpiyush15@gmail.com',  # Use info!
        'Accept-Encoding': 'gzip, deflate',
    }
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        filings = data.get('filings', {}).get('recent', {})
        forms = filings.get('form', [])
        accession_numbers = filings.get('accessionNumber', [])
        periods = filings.get('periodOfReport', [])
        states = filings.get('stateOfIncorporation', [])
        # Build list of 10-K filings
        filings_list = []
        for i, form in enumerate(forms):
            if form == "10-K":
                filing = {
                            "periodOfReport": periods[i] if i < len(periods) and periods[i] else filings.get('filingDate', [])[i] if i < len(filings.get('filingDate', [])) else "",
                            "stateOfIncorporation": states[i] if i < len(states) and states[i] else "USA",
                            "linkToFilingDetails": f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession_numbers[i].replace('-', '')}/{accession_numbers[i]}-index.htm"
                        }
                filings_list.append(filing)
                if len(filings_list) >= count:
                    break
        return filings_list
    except Exception as e:
        print(f"[ERROR] Failed to fetch filings for CIK {cik}: {e}")
        return []
