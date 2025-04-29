# src/xbrl_extractor.py
import requests
from sec_api import XbrlApi
from src.config import SEC_API_KEY

xbrlApi = XbrlApi(api_key=SEC_API_KEY)



def extract_revenue_from_xbrl(filing_url, api_key):
    """
    Extracts revenue from SEC filing using the XBRL-to-JSON Converter API.
    Returns (revenue, currency) or (None, None) if not found.
    """
    endpoint = "https://api.sec-api.io/xbrl-to-json"
    params = {
        "htm-url": filing_url,
        "token": api_key
    }
    response = requests.get(endpoint, params=params)
    if response.status_code != 200:
        print(f"[ERROR] API error: {response.status_code} - {response.text}")
        return None, None

    xbrl_json = response.json()
    statements = xbrl_json.get("StatementsOfIncome", {})

    # Look for common revenue tags
    revenue_tags = [
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "Revenues",
        "SalesRevenueNet",
        "SalesRevenueGoodsNet",
        "NetSales"
    ]
    for tag in revenue_tags:
        if tag in statements:
            # Get the most recent value (usually the first item)
            revenue_item = statements[tag][0]
            revenue = revenue_item.get("value")
            currency = revenue_item.get("unitRef", "USD")
            return revenue, currency
    return None, None
