<<<<<<< HEAD
import pandas as pd

def preprocess_data(df):
    print("Preprocessing data...")
    
    # Check for missing values
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    
    # Remove records without CustomerID (essential for segmentation)
    df = df.dropna(subset=['CustomerID'])
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Filter cancelled transactions (InvoiceNo starts with 'C' or Quantity < 0)
    # Some datasets represent cancellations with negative quantity
    df = df[df['Quantity'] > 0]
    
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Create TotalPrice
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    print(f"Shape after cleaning: {df.shape}")
    return df
=======
import pandas as pd

def preprocess_data(df):
    print("Preprocessing data...")
    
    # Check for missing values
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    
    # Remove records without CustomerID (essential for segmentation)
    df = df.dropna(subset=['CustomerID'])
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Filter cancelled transactions (InvoiceNo starts with 'C' or Quantity < 0)
    # Some datasets represent cancellations with negative quantity
    df = df[df['Quantity'] > 0]
    
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Create TotalPrice
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    print(f"Shape after cleaning: {df.shape}")
    return df
>>>>>>> c2cafea4a0b4bee765cbeb05d2d36a7327a604bb
