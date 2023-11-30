"""
scikit-learn "Comparing different clustering algorithms on toy datasets"
https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html
のコードを参考に著者作成。
"""

import time  # 時間計測のためのライブラリ
import warnings  # 警告を非表示にするためのライブラリ
from itertools import cycle, islice  # イテレータを生成するためのライブラリ
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする
import numpy as np  # 数値演算のためのNumPy
from sklearn import cluster, datasets, mixture  # クラスタリングのためのライブラリ
from sklearn.neighbors import kneighbors_graph  # k近傍グラフを作成するためのライブラリ
from sklearn.preprocessing import StandardScaler  # データの正規化のためのライブラリ

np.random.seed(0)  # 再現性のため
plt.rcParams['font.size'] = 10  # プロットのフォントサイズを10に設定

n_samples = 500  # サンプルサイズ

noisy_circles = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05)  # 円形のクラスタ
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05)  # 月型のクラスタ
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)  # 正規分布に従うクラスタ
no_structure = np.random.rand(n_samples, 2), None  # 構造のないデータ

# 異方性のあるデータ
random_state = 170
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)

# 3つの正規分布に従うデータ
varied = datasets.make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)


plt.figure(figsize=(10, 12))  # サブプロットのサイズを設定
plt.subplots_adjust(
    left=0.02, right=0.98, bottom=0.001, top=0.95, wspace=0.05, hspace=0.01
)  # サブプロット間の余白を設定


plot_num = 1

default_base = {
    "quantile": 0.3,
    "eps": 0.3,
    "damping": 0.9,
    "preference": -200,
    "n_neighbors": 3,
    "n_clusters": 3,
    "min_samples": 7,
    "xi": 0.05,
    "min_cluster_size": 0.1,
    "allow_single_cluster": True,
    "hdbscan_min_cluster_size": 15,
    "hdbscan_min_samples": 3,
}

data_sets = [
    (noisy_circles, {"damping": 0.77, "preference": -240,
     "quantile": 0.2, "n_clusters": 2, "min_samples": 7, "xi": 0.08}),
    (noisy_moons, {"damping": 0.75, "preference": -220,
     "n_clusters": 2, "min_samples": 7, "xi": 0.1}),
    (varied, {"eps": 0.18, "n_neighbors": 2,
     "min_samples": 7, "xi": 0.01, "min_cluster_size": 0.2}),
    (aniso, {"eps": 0.15, "n_neighbors": 2,
     "min_samples": 7, "xi": 0.1, "min_cluster_size": 0.2}),
    (blobs, {"min_samples": 7, "xi": 0.1, "min_cluster_size": 0.2}),
    (no_structure, {}),
]

for i_dataset, (dataset, algo_params) in enumerate(data_sets):
    params = default_base.copy()
    params.update(algo_params)

    X, y = dataset
    X = StandardScaler().fit_transform(X)
    bandwidth = cluster.estimate_bandwidth(X, quantile=params["quantile"])

    connectivity = kneighbors_graph(
        X, n_neighbors=params["n_neighbors"], include_self=False
    )
    connectivity = 0.5 * (connectivity + connectivity.T)

    ms = cluster.MeanShift(bandwidth=bandwidth, bin_seeding=True)
    two_means = cluster.MiniBatchKMeans(n_clusters=params["n_clusters"])
    ward = cluster.AgglomerativeClustering(
        n_clusters=params["n_clusters"], linkage="ward", connectivity=connectivity
    )
    spectral = cluster.SpectralClustering(
        n_clusters=params["n_clusters"], eigen_solver="arpack", affinity="nearest_neighbors"
    )
    dbscan = cluster.DBSCAN(eps=params["eps"])
    hdbscan = cluster.HDBSCAN(
        min_samples=params["hdbscan_min_samples"],
        min_cluster_size=params["hdbscan_min_cluster_size"],
        allow_single_cluster=params["allow_single_cluster"],
    )
    optics = cluster.OPTICS(
        min_samples=params["min_samples"], xi=params["xi"], min_cluster_size=params["min_cluster_size"])
    affinity_propagation = cluster.AffinityPropagation(
        damping=params["damping"], preference=params["preference"])
    average_linkage = cluster.AgglomerativeClustering(
        linkage="average", affinity="cityblock",
        n_clusters=params["n_clusters"], connectivity=connectivity)
    birch = cluster.Birch(n_clusters=params["n_clusters"])
    gmm = mixture.GaussianMixture(
        n_components=params["n_clusters"], covariance_type="full"
    )

    clustering_algorithms = (
        ("MiniBatch\nKMeans", two_means),
        ("Affinity\nPropagation", affinity_propagation),
        ("MeanShift", ms),
        ("Spectral\nClustering", spectral),
        ("Ward", ward),
        ("Agglomerative\nClustering", average_linkage),
        ("DBSCAN", dbscan),
        ("HDBSCAN", hdbscan),
        ("OPTICS", optics),
        ("BIRCH", birch),
        ("Gaussian\nMixture", gmm),
    )

    for i_algo, (name, algorithm) in enumerate(clustering_algorithms):
        t0 = time.time()
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message="the number of connected components of the "
                + "connectivity matrix is [0-9]{1,2}"
                + " > 1. Completing it to avoid stopping the tree early.",
                category=UserWarning,
            )
            warnings.filterwarnings(
                "ignore",
                message="Graph is not fully connected, spectral embedding"
                + " may not work as expected.",
                category=UserWarning,
            )
            algorithm.fit(X)

        t1 = time.time()
        if hasattr(algorithm, "labels_"):
            y_pred = algorithm.labels_.astype(int)
        else:
            y_pred = algorithm.predict(X)

        new_plot_num = i_dataset + i_algo * (len(data_sets)) + 1
        print(new_plot_num)
        plt.subplot(len(clustering_algorithms), len(
            data_sets), new_plot_num)  # この行を変更

        if i_dataset == 0:
            plt.ylabel(name, rotation=90, size=14)

        colors = np.array(list(islice(cycle(["#377eb8", "#ff7f00", "#4daf4a",
                                             "#f781bf", "#a65628", "#984ea3",
                                             "#999999", "#e41a1c", "#dede00"]),
                                      int(max(y_pred) + 1))))
        colors = np.append(colors, ["#000000"])
        plt.scatter(X[:, 0], X[:, 1], s=10, color=colors[y_pred])

        plt.xlim(-2.5, 2.5)
        plt.ylim(-2.5, 2.5)
        plt.xticks(())
        plt.yticks(())
        plt.text(.99, .01, ("%.2fs" % (t1 - t0)).lstrip("0"),
                 transform=plt.gca().transAxes, size=15,
                 horizontalalignment="right")
        plot_num += 1

plt.tight_layout()  # レイアウトの調整
plt.savefig('4_3_3_various_clustering_examples.png', dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
