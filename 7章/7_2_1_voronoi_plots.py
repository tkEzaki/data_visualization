import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from scipy.spatial import Voronoi, distance_matrix  # ボロノイ図のためのSciPy
from shapely.geometry import Polygon, Point, MultiPolygon  # 図形描画のためのShapely
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 16  # フォントサイズを設定

# ランダムな点を生成
np.random.seed(42)  # シード値を固定
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
        polygon = Polygon([vor.vertices[i] for i in region])  # 領域を表す多角形を生成
        clipped_polygon = polygon.intersection(bounding_box)  # 領域をクリッピング
        if not clipped_polygon.is_empty:  # 領域が空でなければ
            clipped_polygons.append(clipped_polygon)  # 領域を追加
            clipped_areas.append(clipped_polygon.area)  # 領域の面積を追加


# 半径0.2のディスクを生成
def create_disk(point, radius=0.2):
    return Point(point).buffer(radius)


# 各点にディスクを置く
disks = [create_disk(point) for point in points]

# オーバーラップした部分を切り取る（ボロノイ図的に分割）
modified_polygons = []
for i, disk in enumerate(disks):
    modified_polygon = disk  # ディスクを初期化
    for clipped_polygon in clipped_polygons:  # クリッピングされた領域に対して
        if clipped_polygon.contains(Point(points[i])):  # ディスクの中心が含まれていれば
            modified_polygon = modified_polygon.intersection(
                clipped_polygon)  # 切り取る
            break
    modified_polygons.append(modified_polygon)  # 切り取った領域を追加

# 最終的なポリゴン（変形ボロノイセル）の面積を計算
final_areas = [polygon.area for polygon in modified_polygons]

# 最初のfigure
fig1, axs1 = plt.subplots(1, 2, figsize=(10, 6))

# 1つ目のサブプロット：オリジナルのボロノイ図
ax = axs1[0]
norm1 = plt.Normalize(min(clipped_areas), max(clipped_areas))  # カラーマップの正規化
cmap1 = plt.cm.jet  # カラーマップの設定

for polygon, area in zip(clipped_polygons, clipped_areas):  # 領域と面積のペアに対して
    x, y = polygon.exterior.xy  # 領域の外周を取得
    ax.fill(x, y, facecolor=cmap1(norm1(area)), edgecolor="k")  # 領域を塗りつぶし

ax.scatter(points[:, 0], points[:, 1], c='white', marker='o')  # 点をプロット
ax.set_xlim([0, 1])  # x軸の範囲を設定
ax.set_ylim([0, 1])  # y軸の範囲を設定

# 最近傍点を矢印で表示
for i, j in enumerate(nearest_indices):
    ax.arrow(points[i, 0], points[i, 1], points[j, 0] - points[i, 0], points[j, 1] - points[i, 1],
             head_width=0.02, head_length=0.02, fc='magenta', ec='magenta', alpha=0.5)

# カラーバーを表示
plt.colorbar(plt.cm.ScalarMappable(norm=norm1, cmap=cmap1),
             ax=ax, orientation='horizontal', pad=0.08)


# 2つ目のサブプロット：ディスク付きボロノイ図
ax = axs1[1]

for polygon, area in zip(modified_polygons, final_areas):  # 領域と面積のペアに対して
    if isinstance(polygon, Polygon):  # 領域が単一の多角形の場合
        x, y = polygon.exterior.xy  # 領域の外周を取得
        ax.fill(x, y, facecolor=cmap1(norm1(area)), edgecolor="k")  # 領域を塗りつぶし
    elif isinstance(polygon, MultiPolygon):  # 領域が複数の多角形の場合
        for sub_polygon in polygon.geoms:  # 領域を構成する各多角形に対して
            x, y = sub_polygon.exterior.xy  # 領域の外周を取得
            ax.fill(x, y, facecolor=cmap1(norm1(area)),
                    edgecolor="k")  # 領域を塗りつぶし

ax.scatter(points[:, 0], points[:, 1], c='white', marker='o')  # 点をプロット
ax.set_xlim([0, 1])  # x軸の範囲を設定
ax.set_ylim([0, 1])  # y軸の範囲を設定

# カラーバーを表示
plt.colorbar(plt.cm.ScalarMappable(norm=norm1, cmap=cmap1),
             ax=ax, orientation='horizontal', pad=0.08)

# 最初のfigureを表示
plt.tight_layout()  # レイアウトを調整
plt.savefig('7_2_1_1_voronoi_diagram.png', dpi=300)  # 図を保存
plt.show()  # 図を表示


# 2つ目の図
fig2, axs2 = plt.subplots(1, 2, figsize=(10, 4))

# 3つ目のサブプロット：最短距離のヒストグラム
ax = axs2[0]
min_dists = np.min(dist_matrix, axis=1)  # 各点の最短距離を取得
ax.hist(min_dists, bins=10, color='blue', alpha=0.7, edgecolor='black')
ax.set_xlabel('最近傍点までの最短')  # x軸のラベルを設定
ax.set_ylabel('頻度')  # y軸のラベルを設定


# 4つ目のサブプロット：ボロノイセルの面積のヒストグラム（2種類）
ax = axs2[1]
bins = np.linspace(
    0, max(max(clipped_areas), max(final_areas)), 10)  # ビンのエッジを計算
ax.hist(clipped_areas, bins=bins, color='green',
        alpha=0.5, edgecolor='black', label='通常ボロノイ図')
ax.hist(final_areas, bins=bins, color='red',
        alpha=0.5, edgecolor='black', label='最大距離制限')

ax.set_xlabel('各領域の面積')  # x軸のラベルを設定
ax.set_ylabel('頻度')  # y軸のラベルを設定
ax.legend(loc='upper left')  # 凡例を表示

# 2つ目のfigureを表示
plt.tight_layout()  # レイアウトを調整
plt.savefig('7_2_1_2_voronoi_histogram.png', dpi=300)  # 図を保存
plt.show()  # 図を表示
