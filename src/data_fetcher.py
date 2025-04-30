import pandas as pd

def get_sp500_companies():
    """
    Fetches the current list of S&P 500 companies from Wikipedia.
    Returns:
        pd.DataFrame: DataFrame with columns ['ticker', 'company_name', 'gics_sector', 'cik']
    """
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    tables = pd.read_html(url)
    sp500_table = tables[0]

    tickers = sp500_table['Symbol'].tolist()
    company_names = sp500_table['Security'].tolist()
    gics_sectors = sp500_table['GICS Sector'].tolist()
    ciks = sp500_table['CIK'].astype(str).str.zfill(10).tolist()  # CIK as 10-digit string

    df = pd.DataFrame({
        'ticker': tickers,
        'company_name': company_names,
        'gics_sector': gics_sectors,
        'cik': ciks
    })

    return df
