# src/data_cleaner.py

import pandas as pd

def clean_data(df):
    """
    Cleans and standardizes the extracted data.
    
    Args:
        df (pd.DataFrame): Raw extracted data.
        
    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Drop rows with missing revenue or company name
    df = df.dropna(subset=['revenue', 'companyname'])
    
    # Convert revenue to numeric (float)
    df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
    df = df.dropna(subset=['revenue'])
    
    # Standardize country names (optional, here just fill missing with 'Unknown')
    df['geonameen'] = df['geonameen'].fillna('Unknown')
    
    # Strip whitespace from strings
    str_cols = ['companyname', 'industryclassification', 'geonameen', 'revenue_unit']
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()
    
    # Sort by company and year descending
    df = df.sort_values(by=['companyname', 'timevalue'], ascending=[True, False])
    
    return df.reset_index(drop=True)
