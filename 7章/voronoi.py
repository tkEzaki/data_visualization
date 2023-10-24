import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, distance_matrix
from shapely.geometry import Polygon
from matplotlib.colors import ListedColormap
plt.rcParams['font.family'] = 'Yu Gothic'
plt.rcParams['font.size'] = 14

# ランダムな点を生成
np.random.seed(42)
points = np.random.rand(20, 2)

# 領域内の各点から別の点への距離行列を計算
dist_matrix = distance_matrix(points, points)

# 対角成分を無限大に設定（自分自身への距離を無視）
np.fill_diagonal(dist_matrix, np.inf)

# 各点から最も近い点のインデックスを取得
nearest_indices = np.argmin(dist_matrix, axis=1)

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

# 三枚のサブプロットを作成
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# 1つ目のサブプロット：ボロノイ図と最短距離の矢印
ax = axs[0]
norm = plt.Normalize(min(clipped_areas), max(clipped_areas))
cmap = plt.cm.jet

for polygon, area in zip(clipped_polygons, clipped_areas):
    x, y = polygon.exterior.xy
    ax.fill(x, y, facecolor=cmap(norm(area)), edgecolor="k")

ax.scatter(points[:, 0], points[:, 1], c='white', marker='o')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical')

for i, j in enumerate(nearest_indices):
    ax.arrow(points[i, 0], points[i, 1], points[j, 0] - points[i, 0], points[j, 1] - points[i, 1],
             head_width=0.02, head_length=0.02, fc='k', ec='k', alpha=0.3)

# 2つ目のサブプロット：最短距離のヒストグラム
ax = axs[1]
min_dists = np.min(dist_matrix, axis=1)
ax.hist(min_dists, bins=10, color='blue', alpha=0.7, edgecolor='black')
ax.set_title('Histogram of Nearest Distances')
ax.set_xlabel('Distance')
ax.set_ylabel('Frequency')

# 3つ目のサブプロット：ボロノイセルの面積のヒストグラム
ax = axs[2]
ax.hist(clipped_areas, bins=10, color='green', alpha=0.7, edgecolor='black')
ax.set_title('Histogram of Voronoi Cell Areas')
ax.set_xlabel('Area')
ax.set_ylabel('Frequency')

plt.tight_layout()
plt.show()
