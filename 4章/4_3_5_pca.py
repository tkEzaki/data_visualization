import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from sklearn.datasets import make_classification  # サンプルデータの生成
from sklearn.decomposition import PCA  # 主成分分析器
from sklearn.manifold import TSNE, MDS  # t-SNE, MDSのインポート
from sklearn.preprocessing import StandardScaler  # データの正規化のためのライブラリ
from sklearn.neural_network import MLPRegressor  # 多層パーセプトロン（MLP）のインポート
from sklearn.cluster import SpectralClustering  # SpectralClusteringのインポート
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams['font.size'] = 16  # プロットのフォントサイズを16に設定

# データセットの生成
X, y = make_classification(
    n_samples=300, n_features=10, n_informative=2,
    n_redundant=5, n_clusters_per_class=1, random_state=42, n_classes=3
)  # 高次元のデータを生成

# 主成分分析 (PCA)
pca = PCA()
X_pca = pca.fit_transform(X)  # PCAによる次元削減


# PCAの2次元に対してSpectral Clustering
clusters_pca = SpectralClustering(
    n_clusters=3, random_state=42).fit_predict(X_pca[:, :2])

# PCAの各主成分の説明力
explained_variance_all = pca.explained_variance_ratio_


# グラフ描画
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# PCA結果のクラスタリング
axs[0].scatter(X_pca[:, 0], X_pca[:, 1], c=clusters_pca,
               cmap='viridis')  # クラスタリング結果をプロット
axs[0].set_xlabel('PC 1')  # x軸のラベル
axs[0].set_ylabel('PC 2')  # y軸のラベル

# PCAの各主成分の説明力
axs[1].bar(
    [f'PC {i+1}' for i in range(len(explained_variance_all))],
    explained_variance_all
)
axs[1].set_ylim(0, 1)  # y軸の範囲を設定
axs[1].set_xticklabels(
    [f'PC {i+1}' for i in range(len(explained_variance_all))],
    rotation=30, ha='right'
)  # x軸の目盛りを設定


plt.tight_layout()  # レイアウトの調整
plt.savefig('4_3_5_pca.png', dpi=300)  # 画像を保存
plt.show()  # 画像を表示
