import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE, MDS
import umap

plt.rcParams['font.family'] = "Yu Gothic"

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
# PNGファイルとして保存
plt.savefig('first_image_with_colorbar.png', dpi=300)


plt.axis('on')
# 主成分分析 (PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print("PCA")

# t-SNE による次元圧縮
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)
print("tSNE")

# MDS による次元圧縮
mds = MDS(n_components=2, random_state=42)
X_mds = mds.fit_transform(X)
print("MDS")

# UMAPによる次元圧縮
umap_transformer = umap.UMAP(n_components=2, random_state=42)
X_umap = umap_transformer.fit_transform(X)
print("UMAP")

# K-means クラスタリング
clusters_pca = KMeans(n_clusters=10, random_state=42).fit_predict(X_pca)
print("PCA with K-means")
clusters_mds = KMeans(n_clusters=10, random_state=42).fit_predict(X_mds)
print("MDS with KMeans")
clusters_tsne = KMeans(n_clusters=10, random_state=42).fit_predict(X_tsne)
print("t-SNE with KMeans")
clusters_umap = KMeans(n_clusters=10, random_state=42).fit_predict(X_umap)
print("UMAP with KMeans")

# 描画
fig, axs = plt.subplots(2, 4, figsize=(12, 6))  # サブプロットを2x4に

# PCA結果のクラスタリング
axs[0, 0].scatter(X_pca[:, 0], X_pca[:, 1], c=clusters_pca, cmap='jet')
axs[0, 0].set_title('PCA (K-means)')
scatter = axs[0, 1].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='jet')
# plt.colorbar(scatter, ax=axs[0, 1])
axs[0, 1].set_title('PCA (正解ラベル)')

# MDS結果のクラスタリング
axs[0, 2].scatter(X_mds[:, 0], X_mds[:, 1], c=clusters_mds, cmap='jet')
axs[0, 2].set_title('MDS (K-means)')
scatter = axs[0, 3].scatter(X_mds[:, 0], X_mds[:, 1], c=y, cmap='jet')
# plt.colorbar(scatter, ax=axs[0, 3])
axs[0, 3].set_title('MDS (正解ラベル)')

# t-SNE結果のクラスタリング
axs[1, 0].scatter(X_tsne[:, 0], X_tsne[:, 1], c=clusters_tsne, cmap='jet')
axs[1, 0].set_title('t-SNE  (K-means)')
scatter = axs[1, 1].scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='jet')
# plt.colorbar(scatter, ax=axs[1, 1])
axs[1, 1].set_title('t-SNE (正解ラベル)')

# UMAP結果のクラスタリング
axs[1, 2].scatter(X_umap[:, 0], X_umap[:, 1], c=clusters_umap, cmap='jet')
axs[1, 2].set_title('UMAP  (K-means)')
scatter = axs[1, 3].scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='jet')
# plt.colorbar(scatter, ax=axs[1, 3])
axs[1, 3].set_title('UMAP (正解ラベル)')

plt.tight_layout()
plt.savefig('dimensionality_reduction.png', dpi=300)
plt.show()
