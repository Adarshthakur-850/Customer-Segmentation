import pandas as pd
import datetime as dt

def calculate_rfm(df):
    print("Calculating RFM metrics...")
    
    # Reference date: 1 day after the last transaction in the dataset
    latest_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
    
    # Group by CustomerID
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (latest_date - x.max()).days, # Recency
        'InvoiceNo': 'count', # Frequency (using count of items/lines or unique invoices?)
                              # Standard RFM often uses count of unique invoices (orders)
                              # Let's check if 'InvoiceNo' is unique per order. Yes.
        'TotalPrice': 'sum'   # Monetary
    }).reset_index()
    
    # Rename columns
    rfm.rename(columns={
        'InvoiceDate': 'Recency',
        'InvoiceNo': 'Frequency',
        'TotalPrice': 'Monetary'
    }, inplace=True)
    
    # Better Frequency calculation: count unique invoices per customer
    # The aggregation above counts total rows (products). 
    # Let's fix Frequency to be unique orders.
    frequency_df = df.groupby('CustomerID')['InvoiceNo'].nunique().reset_index()
    frequency_df.rename(columns={'InvoiceNo': 'Frequency'}, inplace=True)
    
    # Update RFM dataframe with correct Frequency
    rfm['Frequency'] = frequency_df['Frequency']
    
    print(f"RFM Shape: {rfm.shape}")
    print(rfm.head())
    
    return rfm
