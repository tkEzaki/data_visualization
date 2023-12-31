from sklearn.neighbors import KernelDensity  # カーネル密度推定のためのscikit-learn
import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from scipy.spatial import Voronoi  # ボロノイ図のためのSciPy
from shapely.geometry import Polygon, Point  # 図形描画のためのShapely
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 16  # フォントサイズを設定

# ランダムな点を生成
np.random.seed(42)  # シード値を固定
points = np.random.rand(20, 2)

# 関心領域から遠く離れた4点を追加
far_points = np.array([[-1, -1], [2, -1], [2, 2], [-1, 2]])

# 新しい点セットを作成
new_points = np.vstack([points, far_points])

# 新しいボロノイ図を計算
vor = Voronoi(new_points)

# [0,1]x[0,1] の領域を定義
bounding_box = Polygon([[0, 0], [1, 0], [1, 1], [0, 1]])

# ボロノイ図の領域をクリッピング
clipped_polygons = []
clipped_areas = []
for region in vor.regions:
    if not -1 in region and len(region) > 0:
        polygon = Polygon([vor.vertices[i] for i in region])
        clipped_polygon = polygon.intersection(bounding_box)
        if not clipped_polygon.is_empty:
            clipped_polygons.append(clipped_polygon)
            clipped_areas.append(clipped_polygon.area)

# 面積の逆数（密度）を計算し、色の範囲を10-90パーセンタイルで設定
densities = 1 / np.array(clipped_areas)
min_density = np.percentile(densities, 10)
max_density = np.percentile(densities, 90)

# カーネル密度推定のバンド幅を三種類設定
bandwidths = [0.05, 0.1, 0.2]
kde_results = []

for bw in bandwidths:  # バンド幅ごとに処理
    kde = KernelDensity(bandwidth=bw, kernel='gaussian')  # カーネル密度推定のインスタンスを生成
    kde.fit(points)  # カーネル密度推定の学習
    x, y = np.linspace(0, 1, 100), np.linspace(0, 1, 100)
    xx, yy = np.meshgrid(x, y)
    gridpoints = np.c_[xx.ravel(), yy.ravel()]
    z = np.exp(kde.score_samples(gridpoints))
    zz = z.reshape(xx.shape)
    kde_results.append(zz)

# 図に描画
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# 左上ディスクなしのボロノイ図
ax = axs[0, 0]
norm1 = plt.Normalize(min_density - 20, max_density+10)
cmap1 = plt.cm.jet

for polygon, density in zip(clipped_polygons, densities):
    x, y = polygon.exterior.xy
    ax.fill(x, y, facecolor=cmap1(norm1(density)), edgecolor="k")

ax.scatter(points[:, 0], points[:, 1], c='k', alpha=0.5, marker='o')
ax.set_title('ボロノイ図')
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.0])


# カーネル密度推定（三種類のバンド幅）
for i, (bw, zz) in enumerate(zip(bandwidths, kde_results)):
    ax = axs.flatten()[i + 1]
    ax.contourf(xx, yy, zz, cmap='jet')
    ax.scatter(points[:, 0], points[:, 1], c='k', alpha=0.5, label='Data Points')
    ax.set_title(f'KDE（バンド幅={bw}）')

plt.tight_layout()
plt.savefig('7_2_2_KDE.png', dpi=300)
plt.show()
