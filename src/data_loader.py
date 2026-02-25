<<<<<<< HEAD
import pandas as pd
import os
import requests
import zipfile
import io


DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
DATA_PATH = os.path.join("data", "Online_Retail.xlsx")
CSV_PATH = os.path.join("data", "Online_Retail.csv")

def load_data():
    if not os.path.exists("data"):
        os.makedirs("data")
        
    if not os.path.exists(DATA_PATH) and not os.path.exists(CSV_PATH):
        print(f"Downloading dataset from {DATA_URL}...")
        try:
            response = requests.get(DATA_URL)
            response.raise_for_status()
            with open(DATA_PATH, "wb") as f:
                f.write(response.content)
            print("Download complete.")
        except Exception as e:
            print(f"Error downloading data: {e}")
            raise
    
    print("Loading data...")
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
    else:
        # Load Excel and save as CSV for faster future loads
        print("Reading Excel file (this might take a moment)...")
        df = pd.read_excel(DATA_PATH)
        df.to_csv(CSV_PATH, index=False)
        
    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    return df
=======
import pandas as pd
import os
import requests
import zipfile
import io


DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
DATA_PATH = os.path.join("data", "Online_Retail.xlsx")
CSV_PATH = os.path.join("data", "Online_Retail.csv")

def load_data():
    if not os.path.exists("data"):
        os.makedirs("data")
        
    if not os.path.exists(DATA_PATH) and not os.path.exists(CSV_PATH):
        print(f"Downloading dataset from {DATA_URL}...")
        try:
            response = requests.get(DATA_URL)
            response.raise_for_status()
            with open(DATA_PATH, "wb") as f:
                f.write(response.content)
            print("Download complete.")
        except Exception as e:
            print(f"Error downloading data: {e}")
            raise
    
    print("Loading data...")
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
    else:
        # Load Excel and save as CSV for faster future loads
        print("Reading Excel file (this might take a moment)...")
        df = pd.read_excel(DATA_PATH)
        df.to_csv(CSV_PATH, index=False)
        
    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    return df
>>>>>>> c2cafea4a0b4bee765cbeb05d2d36a7327a604bb
