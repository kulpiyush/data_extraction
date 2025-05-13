import requests

def get_all_revenue_facts_from_sec(cik):
    """
    Retrieve all reported revenue facts for a company from the SEC XBRL company-concept API.

    This function queries the SEC's public XBRL API for the specified company's CIK and
    collects all available 'us-gaap:Revenues' data points across filings. Each revenue
    fact includes the reported value, currency, and the fiscal period end date.

    Args:
        cik (str): The 10-digit Central Index Key (CIK) of the company (zero-padded as needed).

    Returns:
        list of dict: A list of revenue fact dictionaries, each containing:
            - 'value' (float or int): The reported revenue amount.
            - 'currency' (str): The currency unit (e.g., 'USD').
            - 'end' (str): The fiscal period end date in 'YYYY-MM-DD' format.
    """
    headers = {
        'User-Agent': 'Statista Case Study Extractor kulpiyush15@gmail.com',
        'Accept-Encoding': 'gzip, deflate',
    }
    url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/Revenues.json"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        units = data.get('units', {})
        all_facts = []
        for currency, values in units.items():
            for fact in values:
                # Each fact: {'val': ..., 'end': 'YYYY-MM-DD', ...}
                all_facts.append({
                    'value': fact['val'],
                    'currency': currency,
                    'end': fact['end']
                })
        return all_facts
    except Exception as e:
        print(f"[ERROR] SEC API request failed: {e}")
        return []
