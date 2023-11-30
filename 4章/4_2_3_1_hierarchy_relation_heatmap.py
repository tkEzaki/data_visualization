import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import seaborn as sns  # グラフ作成のためのSeaborn
import numpy as np  # 数値演算のためのNumPy
import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.patches as patches  # 図形描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams["font.size"] = 16  # プロットのフォントサイズを16に設定


# 研究者リスト
researchers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# 共著データ
collaboration = pd.DataFrame([
    [np.nan, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, np.nan, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, np.nan, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, np.nan, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, np.nan, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, np.nan, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, np.nan, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, np.nan, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, np.nan, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, np.nan],
], columns=researchers, index=researchers)


# ヒートマップの描画
fig, ax = plt.subplots(figsize=(6, 5))

ax = sns.heatmap(
    collaboration, annot=True, fmt=".0f", xticklabels=researchers,
    yticklabels=researchers, cmap='binary', cbar_kws={'ticks': []},
    linewidths=0.5, linecolor='black', ax=ax
)  # ヒートマップを描画

ax.xaxis.tick_top()  # x軸のラベルを上に表示"
ax.set_title("指導された研究者", fontsize=16)  # タイトルの追加
ax.set_ylabel("指導した研究者")  # y軸のラベル

# 対角線上のセルをグレーにする
for i in range(len(researchers)):
    ax.add_patch(patches.Rectangle((i, i), 1, 1, fill=True,
                 facecolor="gray", edgecolor='k'))

# 軸線の表示
ax.axhline(y=0, color='k', linewidth=2)
ax.axhline(y=collaboration.shape[1], color='k', linewidth=2)
ax.axvline(x=0, color='k', linewidth=2)
ax.axvline(x=collaboration.shape[0], color='k', linewidth=2)

plt.savefig("4_2_3_1_hierarchy_relation_heatmap.png", dpi=300)  # 画像の保存
plt.show()  # 画像の表示
