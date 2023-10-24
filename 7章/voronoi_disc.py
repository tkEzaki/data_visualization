import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, distance_matrix
from shapely.geometry import Polygon, Point, MultiPolygon
import math
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

# 半径0.2のディスクを生成

RADIUS = 0.2


def create_disk(point, radius=RADIUS):
    return Point(point).buffer(radius)


# 各点にディスクを置く
disks = [create_disk(point) for point in points]

# オーバーラップした部分を切り取る（ボロノイ図的に分割）
modified_polygons = []
for i, disk in enumerate(disks):
    modified_polygon = disk

    for clipped_polygon in clipped_polygons:
        # if point i in clipped_polygon:
        if clipped_polygon.contains(create_disk(points[i], radius=0.0000001)):
            modified_polygon = modified_polygon.intersection(clipped_polygon)
            break

    # modified_polygon = modified_polygon.intersection(clipped_polygons[i])
    modified_polygons.append(modified_polygon)

# 最終的なポリゴン（変形ボロノイセル）の面積を計算
final_areas = [polygon.area for polygon in modified_polygons]
print(final_areas)
# 描画
fig, ax = plt.subplots()
norm = plt.Normalize(min(final_areas), max(final_areas))
cmap = plt.cm.jet

# 以下は修正後のコードの一部です。
for polygon, area in zip(modified_polygons, final_areas):
    if isinstance(polygon, Polygon):
        x, y = polygon.exterior.xy
        ax.fill(x, y, facecolor=cmap(norm(area)), edgecolor="k")
    elif isinstance(polygon, MultiPolygon):
        for sub_polygon in polygon.geoms:  # 修正: geoms属性を使用
            x, y = sub_polygon.exterior.xy
            ax.fill(x, y, facecolor=cmap(norm(area)), edgecolor="k")

ax.scatter(points[:, 0], points[:, 1], c='k', marker='o')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical')

plt.show()
