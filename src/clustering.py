from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

def perform_clustering(rfm):
    print("Performing clustering...")
    if not os.path.exists("plots"):
        os.makedirs("plots")
        
    # Scale Data
    # RFM data is usually skewed. Log transformation is often recommended before scaling.
    rfm_log = rfm[['Recency', 'Frequency', 'Monetary']].apply(np.log1p)
    
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_log)
    rfm_scaled_df = pd.DataFrame(rfm_scaled, columns=['Recency', 'Frequency', 'Monetary'])
    
    # 1. Elbow Method
    inertia = []
    K_range = range(1, 11)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(rfm_scaled)
        inertia.append(kmeans.inertia_)
        
    plt.figure(figsize=(8, 5))
    plt.plot(K_range, inertia, marker='o')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method')
    plt.grid(True)
    plt.savefig("plots/elbow_method.png")
    plt.close()
    
    # 2. Silhouette Score (for K=2 to 10)
    sil_scores = []
    K_sil_range = range(2, 11)
    for k in K_sil_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(rfm_scaled)
        score = silhouette_score(rfm_scaled, labels)
        sil_scores.append(score)
        
    plt.figure(figsize=(8, 5))
    plt.plot(K_sil_range, sil_scores, marker='o', color='green')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Scores')
    plt.grid(True)
    plt.savefig("plots/silhouette_scores.png")
    plt.close()
    
    # Choose optimal K (e.g., 3 or 4 based on typical RFM). 
    # For automation, let's pick K=3 or 4, or simple logic.
    # Let's say K=4 is classic (Gold, Silver, Bronze, new/lost).
    optimal_k = 4 # Hardcoded for simplicity, but graphs allow user judgment
    print(f"Applying K-Means with K={optimal_k}")
    
    model = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    clusters = model.fit_predict(rfm_scaled)
    
    # Assign labels to original data
    rfm['Cluster'] = clusters
    
    # Cluster Analysis
    cluster_summary = rfm.groupby('Cluster').agg({
        'Recency': 'mean',
        'Frequency': 'mean',
        'Monetary': 'mean',
        'Cluster': 'count'
    }).rename(columns={'Cluster': 'Count'})
    
    print("Cluster Summary:")
    print(cluster_summary)
    
    return rfm, model, rfm_scaled_df
