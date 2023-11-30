import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from sklearn.datasets import load_digits  # 手書き数字データセット
from sklearn.decomposition import PCA  # 主成分分析器
from sklearn.cluster import KMeans  # k-meansクラスタリング
from sklearn.manifold import TSNE, MDS  # t-SNE, MDSのインポート
import umap  # UMAPのインポート
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams['font.size'] = 14  # プロットのフォントサイズを14に設定

# データセットの読み込み
digits = load_digits()
X = digits.data
y = digits.target

# 最初の画像データを取得
first_image = X[0].reshape(8, 8)

# 画像サイズを5x5に指定
plt.figure(figsize=(3, 2))

# 画像を表示
plt.imshow(first_image, cmap='gray')
plt.axis('off')
# カラーバーを追加
plt.colorbar()
plt.tight_layout()  # レイアウトの調整

# PNGファイルとして保存
plt.savefig('4_3_6_2_digit_image.png', dpi=300)


# 次元圧縮を実施する
plt.axis('on')
# 主成分分析 (PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# t-SNE による次元圧縮
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

# MDS による次元圧縮
mds = MDS(n_components=2, random_state=42)
X_mds = mds.fit_transform(X)

# UMAPによる次元圧縮
umap_transformer = umap.UMAP(n_components=2, random_state=42)
X_umap = umap_transformer.fit_transform(X)


# K-means クラスタリング
clusters_pca = KMeans(n_clusters=10, random_state=42).fit_predict(X_pca)  # PCA
clusters_mds = KMeans(n_clusters=10, random_state=42).fit_predict(X_mds)  # MDS
clusters_tsne = KMeans(
    n_clusters=10, random_state=42).fit_predict(X_tsne)  # t-SNE
clusters_umap = KMeans(
    n_clusters=10, random_state=42).fit_predict(X_umap)  # UMAP

# 描画
fig, axs = plt.subplots(2, 4, figsize=(12, 6))  # サブプロットを2x4に

# PCA結果のクラスタリングを描画
axs[0, 0].scatter(X_pca[:, 0], X_pca[:, 1], c=clusters_pca, cmap='jet')
axs[0, 0].set_title('PCA (K-means)')
scatter = axs[0, 1].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='jet')
axs[0, 1].set_title('PCA (正解ラベル)')

# MDS結果のクラスタリングを描画
axs[0, 2].scatter(X_mds[:, 0], X_mds[:, 1], c=clusters_mds, cmap='jet')
axs[0, 2].set_title('MDS (K-means)')
scatter = axs[0, 3].scatter(X_mds[:, 0], X_mds[:, 1], c=y, cmap='jet')
axs[0, 3].set_title('MDS (正解ラベル)')

# t-SNE結果のクラスタリングを描画
axs[1, 0].scatter(X_tsne[:, 0], X_tsne[:, 1], c=clusters_tsne, cmap='jet')
axs[1, 0].set_title('t-SNE  (K-means)')
scatter = axs[1, 1].scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='jet')
axs[1, 1].set_title('t-SNE (正解ラベル)')

# UMAP結果のクラスタリングを描画
axs[1, 2].scatter(X_umap[:, 0], X_umap[:, 1], c=clusters_umap, cmap='jet')
axs[1, 2].set_title('UMAP  (K-means)')
scatter = axs[1, 3].scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='jet')
axs[1, 3].set_title('UMAP (正解ラベル)')

plt.tight_layout()  # レイアウトの調整
plt.savefig('4_3_6_1_dimensionality_reduction.png', dpi=300)  # 画像を保存
plt.show()  # 画像を表示
