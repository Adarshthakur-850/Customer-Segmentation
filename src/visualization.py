import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

def visualize_clusters(rfm):
    print("Visualizing clusters...")
    if not os.path.exists("plots"):
        os.makedirs("plots")
        
    # 2D Scatter Plots (PairPlot equivalent colored by Cluster)
    plt.figure(figsize=(10, 8))
    sns.pairplot(rfm, vars=['Recency', 'Frequency', 'Monetary'], hue='Cluster', palette='tab10')
    plt.savefig("plots/cluster_pairplot.png")
    plt.close()
    
    # Box Plots for Cluster comparison
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    sns.boxplot(x='Cluster', y='Recency', data=rfm, ax=axes[0])
    sns.boxplot(x='Cluster', y='Frequency', data=rfm, ax=axes[1])
    sns.boxplot(x='Cluster', y='Monetary', data=rfm, ax=axes[2])
    
    # Use Log scale for better visibility if skewed
    axes[1].set_yscale('log')
    axes[2].set_yscale('log')
    
    plt.tight_layout()
    plt.savefig("plots/cluster_boxplots.png")
    plt.close()
    
    # 3D Scatter Plot (using Plotly - saved as HTML)
    try:
        fig = px.scatter_3d(rfm, x='Recency', y='Frequency', z='Monetary',
                  color='Cluster', opacity=0.7,
                  title="3D Cluster Visualization")
        fig.write_html("plots/cluster_3d.html")
    except Exception as e:
        print(f"Skipping 3D Plotly plot: {e}")
