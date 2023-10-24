import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from kmapper import KeplerMapper, Cover
import matplotlib.pyplot as plt

# パラメータ設定
n_samples = 500
n_features = 100
n_clusters = 3

# クラスターデータの生成
X, labels_true = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters)

# Mapperの設定
mapper = KeplerMapper(verbose=0)

# フィルタリングのためのPCAを適用
projected_X = PCA(n_components=2).fit_transform(X)

# Mapperによるクラスタリング
graph = mapper.map(projected_X, X, clusterer=DBSCAN(eps=100), cover=Cover(n_cubes=10, perc_overlap=0.2))

# Mapperグラフの描画
mapper.visualize(graph, path_html="mapper_visualization.html", title="Mapper visualization of 100D clusters")
plt.show()
