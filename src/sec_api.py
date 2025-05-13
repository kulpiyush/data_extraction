import requests

def get_all_revenue_facts_from_sec(cik):
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
