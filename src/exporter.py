# src/exporter.py

def export_to_excel(df, output_path):
    """
    Exports the DataFrame to an Excel file using the required format.
    
    Args:
        df (pd.DataFrame): Cleaned data.
        output_path (str): Path to save the Excel file.
    """
    # Ensure columns are in the correct order as per template
    columns_order = [
        "timevalue",
        "companyname",
        "industryclassification",
        "geonameen",
        "revenue",
        "revenue_unit"
    ]
    df = df[columns_order]
    
    # Save to Excel without index
    df.to_excel(output_path, index=False)
    print(f"[INFO] Exported data to {output_path}")
