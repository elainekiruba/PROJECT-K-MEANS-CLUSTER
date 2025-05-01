# PROJECT-K-MEANS-CLUSTER
# K-Means Clustering Project

📌 Project Description
              This project performs clustering on a dataset using the K-Means algorithm. It identifies distinct groups in the data and visualizes the results.
              This is a simple Python project demonstration K-Means Clustering using the `sklearn` library.

 📁 Files Included

- `kmeans_clustering.py` – Main script to run K-Means
- `\Live_20210128.csv"` – Input dataset
- `output/clusters.png` – Output image of clustered data
- `notebooks/kmeans_demo.ipynb` – Optional: Jupyter Notebook version of the project

  
📊 Customer Segmentation using K-Means Clustering 

Dataset: Facebook Live Sellers Usage & Engagement (Thailand)
         This project applies K-Means clustering to identify usage and engagement patterns of Facebook Live sellers based on their interactions, reactions, and content performance. The goal is to segment sellers into meaningful clusters based on behavioral metrics.


🔧 Tools & Libraries
- Python
- Pandas, NumPy – Data manipulation
- Scikit-learn – Machine learning (`KMeans`, `MinMaxScaler`, `StandardScaler`)
- Matplotlib, Seaborn – Data visualization
  

📁 Dataset Features
Key columns used for clustering:
- `num_reactions`
- `num_comments`
- `num_shares`
- `num_likes`
- `num_loves`
- `num_wows`
- `num_hahas`
- `num_sads`
- `num_angrys`

⚙️ Approach
1. Data Cleaning & Preprocessing
   - Selected relevant numeric features.
   - Applied MinMax Scaling for clustering input.
   - Also experimented with Standard Scaling for comparison.

2. Model Training
   - Used `KMeans` from Scikit-learn.
   - Chose optimal number of clusters via elbow method.

3. Visualization
   - Clustered scatter plots to visualize groupings.
   - Plotted with 2D projections of scaled features.

 📈 Results
- The model segmented the sellers into 5 distinct clusters (e.g., low, medium, high engagement groups).
- Visual inspection through scatter plots helped interpret behavior patterns.
- StandardScaler also tested; showed similar clusters with consistent patterns.

 📉  Scatter Plot
Based on `num_reactions` and `num_comments` (after MinMax Scaling):

👩‍💻 Author
Elaine - www.linkedin.com/in/elaine-kiruba-r




