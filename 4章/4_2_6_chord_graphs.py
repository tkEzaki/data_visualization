from nichord.chord import plot_chord  # nichordはpip installでインストール
from nichord.glassbrain import plot_glassbrain  # nichordはpip installでインストール
# nichordはpip installでインストール
from nichord.combine import combine_imgs, plot_and_combine
from nichord.coord_labeler import get_idx_to_label  # nichordはpip installでインストール
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams['font.size'] = 14  # プロットのフォントサイズを14に設定

# ネットワークの定義
edges = [(0, 1), (0, 2), (1, 5), (3, 5), (4, 6), (2, 7), (6, 7)]  # エッジの定義
edge_weights = [-0.3, -0.5, 0.7, 0.5, -0.2, 0.3, 0.8]  # エッジの重み
coords = [[-24, -99, -12], [51, -3, -15], [-15, -70, 30], [21, 39, 39],
          [21, -66, 48], [54, 33, 12], [-33, 3, 3], [57, -45, 12]]  # 各ノードの座標

idx_to_label = get_idx_to_label(coords, atlas='yeo')  # ラベルの取得

fp_chord = r'4_2_6_3_1_chord.png'
plot_chord(
    idx_to_label, edges, edge_weights=edge_weights,
    coords=None, network_order=None,
    network_colors=None, linewidths=15,
    alphas=0.9, label_fontsize=50,
    fp_chord=fp_chord, do_ROI_circles=True,
    do_ROI_circles_specific=True, ROI_circle_radius=0.02,
    arc_setting=False
)  # コードグラフの描画

fp_glass = r'4_2_6_2_glass_brain.png'
plot_glassbrain(
    idx_to_label, edges, edge_weights, fp_glass,
    coords, linewidths=15, node_size=17
)  # グラスブレインの描画

# 画像の結合
fp_combined = r'4_2_6_3_chord_graphs.png'
combine_imgs(fp_glass, fp_chord, fp_combined)
