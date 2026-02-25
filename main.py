import sys
import os
import pandas as pd

sys.path.append(os.path.join(os.getcwd(), 'src'))

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import calculate_rfm
from src.eda import perform_rfm_eda
from src.clustering import perform_clustering
from src.visualization import visualize_clusters
from src.evaluation import evaluate_clusters

def main():
    print("Starting Customer Segmentation Pipeline...")
    
    # 1. Load Data
    try:
        df = load_data()
    except Exception as e:
        print(f"Pipeline Stopped: {e}")
        return
    
    # 2. Preprocessing
    df = preprocess_data(df)
    
    # 3. Feature Engineering (RFM)
    rfm = calculate_rfm(df)
    
    # 4. EDA
    perform_rfm_eda(rfm)
    
    # 5. Clustering
    rfm_labeled, model, rfm_scaled_df = perform_clustering(rfm)
    
    # 6. Visualization
    visualize_clusters(rfm_labeled)
    
    # 7. Evaluation
    evaluate_clusters(rfm_scaled_df, rfm_labeled['Cluster'])
    
    # Save processed data
    output_path = "data/processed/rfm_clustered.csv"
    if not os.path.exists("data/processed"):
        os.makedirs("data/processed")
    rfm_labeled.to_csv(output_path, index=False)
    print(f"Segmented data saved to {output_path}")
    
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Pipeline Failed: {e}")
