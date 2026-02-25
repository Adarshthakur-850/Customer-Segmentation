<<<<<<< HEAD
from sklearn.metrics import silhouette_score, davies_bouldin_score
import pandas as pd
import numpy as np

def evaluate_clusters(rfm_scaled_df, labels):
    print("Evaluating clusters...")
    
    sil_score = silhouette_score(rfm_scaled_df, labels)
    db_score = davies_bouldin_score(rfm_scaled_df, labels)
    
    print(f"Silhouette Score: {sil_score:.4f}")
    print(f"Davies-Bouldin Score: {db_score:.4f}")
    
    return {'Silhouette': sil_score, 'Davies_Bouldin': db_score}
=======
from sklearn.metrics import silhouette_score, davies_bouldin_score
import pandas as pd
import numpy as np

def evaluate_clusters(rfm_scaled_df, labels):
    print("Evaluating clusters...")
    
    sil_score = silhouette_score(rfm_scaled_df, labels)
    db_score = davies_bouldin_score(rfm_scaled_df, labels)
    
    print(f"Silhouette Score: {sil_score:.4f}")
    print(f"Davies-Bouldin Score: {db_score:.4f}")
    
    return {'Silhouette': sil_score, 'Davies_Bouldin': db_score}
>>>>>>> c2cafea4a0b4bee765cbeb05d2d36a7327a604bb
