import matplotlib.pyplot as plt
import seaborn as sns
import os

def perform_rfm_eda(rfm):
    print("Performing EDA on RFM features...")
    if not os.path.exists("plots"):
        os.makedirs("plots")
        
    # Distribution of R, F, M
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    sns.histplot(rfm['Recency'], bins=50, kde=True, ax=axes[0])
    axes[0].set_title('Recency Distribution')
    
    # Frequency can be skewed, limit range for plotting
    sns.histplot(rfm[rfm['Frequency'] < 50]['Frequency'], bins=50, kde=True, ax=axes[1])
    axes[1].set_title('Frequency Distribution (< 50)')
    
    # Monetary can have outliers
    sns.histplot(rfm[rfm['Monetary'] < 5000]['Monetary'], bins=50, kde=True, ax=axes[2])
    axes[2].set_title('Monetary Distribution (< 5000)')
    
    plt.tight_layout()
    plt.savefig("plots/rfm_distributions.png")
    plt.close()
    
    # Correlation Heatmap
    plt.figure(figsize=(6, 5))
    sns.heatmap(rfm[['Recency', 'Frequency', 'Monetary']].corr(), annot=True, cmap='coolwarm')
    plt.title("RFM Correlation")
    plt.savefig("plots/rfm_correlation.png")
    plt.close()
