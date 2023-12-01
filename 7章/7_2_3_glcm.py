import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
from skimage.feature import graycomatrix, graycoprops  # GLCMのためのライブラリ
from skimage import data  # サンプル画像のためのライブラリ
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams["font.size"] = 16  # フォントサイズを設定

PATCH_SIZE = 21

# データの読み込み 
image = data.camera()

# 画像の一部を切り出し（grass）
grass_patch = image[280:280 + PATCH_SIZE, 454:454 + PATCH_SIZE]

# 画像の一部を切り出し（sky）
sky_patch = image[38:38 + PATCH_SIZE, 34:34 + PATCH_SIZE]

# GLCM/指標の計算
features = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation']
grass_features = [graycoprops(graycomatrix(grass_patch, [1], [0], symmetric=True, normed=True), feature)[0, 0]
                  for feature in features]
sky_features = [graycoprops(graycomatrix(sky_patch, [1], [0], symmetric=True, normed=True), feature)[0, 0]
                for feature in features]

# 描画
fig, axs = plt.subplots(2, 3, figsize=(10, 6.67))

# 元画像の表示
axs[0, 0].imshow(image, cmap=plt.cm.gray, vmin=0, vmax=255)
axs[0, 0].plot(454 + PATCH_SIZE / 2, 280 + PATCH_SIZE / 2, 'gs')  # Grass
axs[0, 0].plot(34 + PATCH_SIZE / 2, 38 + PATCH_SIZE / 2, 'bs')   # Sky
axs[0, 0].set_xlabel('Original Image')
axs[0, 0].set_xticks([])
axs[0, 0].set_yticks([])
axs[0, 0].axis('image')

# 切り出した画像の表示（sky, grass）
axs[0, 1].imshow(sky_patch, cmap=plt.cm.gray, vmin=0, vmax=255)
axs[0, 1].set_xlabel('Sky')
axs[0, 1].set_xticks([])
axs[0, 1].set_yticks([])

axs[0, 2].imshow(grass_patch, cmap=plt.cm.gray, vmin=0, vmax=255)
axs[0, 2].set_xlabel('Grass')
axs[0, 2].set_xticks([])
axs[0, 2].set_yticks([])

# 棒グラフで指標を表示
barWidth = 0.3
r1 = np.arange(len(grass_features))
r2 = [x + barWidth for x in r1]

axs[1, 0].bar(r2, grass_features, color='g', width=barWidth, edgecolor='grey', label='Grass')
axs[1, 0].bar(r1, sky_features, color='b', width=barWidth, edgecolor='grey', label='Sky')

axs[1, 0].set_xticks([r + barWidth for r in range(len(grass_features))])
axs[1, 0].set_xticklabels(features, rotation=30, ha='right')
axs[1, 0].set_yscale('log')
axs[1, 0].legend()

# GLCMの表示（sky）
axs[1, 1].imshow(graycomatrix(sky_patch, [1], [0], symmetric=True, normed=True)[:, :, 0, 0], cmap='jet', origin='lower')
axs[1, 1].set_title('GLCM of Sky', fontsize=16)
axs[1, 1].set_xlabel('Pixel value')
axs[1, 1].set_ylabel('Pixel value')

# GCMLの表示（grass）
axs[1, 2].imshow(graycomatrix(grass_patch, [1], [0], symmetric=True, normed=True)[:, :, 0, 0], cmap='jet', origin='lower')
axs[1, 2].set_title('GLCM of Grass', fontsize=16)
axs[1, 2].set_xlabel('Pixel value')
axs[1, 2].set_ylabel('Pixel value')

plt.tight_layout()  # レイアウトの設定
plt.savefig('7_2_3_glcm.png', dpi=300)  # 画像の保存
plt.show()  # 画面表示
