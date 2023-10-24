import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.mixture import GaussianMixture

# データ生成
X, y_true = make_blobs(n_samples=400, centers=3, cluster_std=0.60, random_state=0)
X = X[:, ::-1]

# クラスタリング手法
clustering_algorithms = [
    ('KMeans', KMeans(n_clusters=3)),
    ('Hierarchical', AgglomerativeClustering(n_clusters=3)),
    ('DBSCAN', DBSCAN(eps=0.70)),
    ('GaussianMixture', GaussianMixture(n_components=3))
]

# プロット設定
plt.figure(figsize=(9, 7))

# クラスタリング結果をプロット
for i, (name, algorithm) in enumerate(clustering_algorithms):
    # クラスタリング実行
    algorithm.fit(X)
    if hasattr(algorithm, 'labels_'):
        y_pred = algorithm.labels_.astype(int)
    else:
        y_pred = algorithm.predict(X)

    # サブプロット作成
    plt.subplot(2, 2, i + 1)
    plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', edgecolors='k')
    plt.title(name)

plt.tight_layout()
plt.savefig('clustering.png', dpi=300)
plt.show()
