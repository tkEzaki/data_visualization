import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
from gtda.mapper import make_mapper_pipeline
from gtda.mapper import plot_static_mapper_graph
from gtda.mapper import MapperInteractivePlotter

# データセットの読み込み
digits = load_digits()
X = digits.data
y = digits.target

# 主成分分析 (PCA) で次元圧縮
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Mapperパイプラインを作成
mapper = make_mapper_pipeline(
    filter_func=PCA(n_components=2),
    cover=make_union(KMeans(10)),
    clustering_preprocessing=StandardScaler(),
    clusterer=DBSCAN(),
)

# Mapperグラフを計算
graph = mapper.fit_transform(X_pca)

# 静的な Mapper グラフをプロット
plot_static_mapper_graph(graph)

# インタラクティブな Mapper グラフをプロット
plotter = MapperInteractivePlotter(graph, X_pca)
plotter.plot()
