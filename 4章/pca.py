import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE, MDS
import umap
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.cluster import SpectralClustering  # SpectralClusteringのインポート

# データセットの生成
X, y = make_classification(n_samples=300, n_features=10, n_informative=2, n_redundant=5, n_clusters_per_class=1, random_state=42, n_classes=3)

# 主成分分析 (PCA)
pca = PCA()
X_pca = pca.fit_transform(X)
# Spectral Clustering
clusters_pca = SpectralClustering(n_clusters=3, random_state=42).fit_predict(X_pca[:, :2])


explained_variance_all = pca.explained_variance_ratio_
# 描画
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# PCA結果のクラスタリング
axs[0].scatter(X_pca[:, 0], X_pca[:, 1], c=clusters_pca, cmap='viridis')
axs[0].set_xlabel('PC 1')
axs[0].set_ylabel('PC 2')
# axs[0].set_title('PCA: Clustering results')

# PCAの各主成分の説明力
axs[1].bar([f'PC {i+1}' for i in range(len(explained_variance_all))], explained_variance_all)
# axs[1].set_title('PCA: Explained variance of each component')
axs[1].set_ylim(0, 1)
# axs[1].set_ylabel('Explained variance ratio')


plt.tight_layout()
plt.savefig('pca.png', dpi=300)
plt.show()
