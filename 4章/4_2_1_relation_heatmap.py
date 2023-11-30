import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import seaborn as sns  # グラフ作成のためのSeaborn
import numpy as np  # 数値演算のためのNumPy
import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.patches as patches  # 図形描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams['font.size'] = 14  # プロットのフォントサイズを14に設定

axis_label_fontsize = 14  # 軸ラベルのフォントサイズ

# 研究者リスト
researchers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# 共著データ
collaboration = pd.DataFrame([
    [np.nan, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, np.nan, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, np.nan, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, np.nan, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, np.nan, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, np.nan, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, np.nan, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, np.nan, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, np.nan, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, np.nan],
], columns=researchers, index=researchers)

# ランダムシードを設定
np.random.seed(0)  # 再現性のため

# 研究スコア
research_score_data = np.zeros((10, 10))  # 10x10のゼロ行列を作成
for i in range(10):
    for j in range(10):
        if i == j:
            research_score_data[i][j] = np.nan  # 自分自身との類似度は1
        elif collaboration.iloc[i, j] == 1:
            research_score_data[i][j] = np.random.uniform(
                0.5, 1.0)  # 共著者は類似度が高い
        else:
            research_score_data[i][j] = np.random.uniform(
                0.0, 0.5)  # それ以外は類似度が低い

research_score_data = (research_score_data +
                       research_score_data.T) / 2  # 対称行列にする処理
research_scores = pd.DataFrame(
    research_score_data, columns=researchers, index=researchers
)  # データフレームに変換

# ヒートマップの描画
fig, axs = plt.subplots(ncols=2, figsize=(10, 4.5))

ax = sns.heatmap(
    collaboration, annot=True, fmt=".0f",
    xticklabels=researchers, yticklabels=researchers,
    cmap='binary', cbar_kws={'label': '', 'ticks': []},
    linewidths=0.5, linecolor='black', ax=axs[0]
)  # ヒートマップを描画

ax.xaxis.tick_top()  # x軸のラベルを上に表示

# 対角線上のセルをグレーに
for i in range(len(researchers)):
    ax.add_patch(patches.Rectangle((i, i), 1, 1, fill=True,
                 facecolor="gray", edgecolor='k'))  # グレーのセルを描画

ax_2 = sns.heatmap(
    research_scores, annot=True, fmt=".1f",
    xticklabels=researchers, yticklabels=researchers,
    cmap='jet', cbar_kws={
        'label': '類似度スコア', 'ticks': [0, 0.2, 0.4, 0.6, 0.8, 1]},
    linewidths=0.5, linecolor='black', ax=axs[1]
)  # ヒートマップを描画

ax_2.xaxis.tick_top()  # x軸のラベルを上に表示

# 対角線上のセルをグレーに
for i in range(len(researchers)):
    ax_2.add_patch(patches.Rectangle(
        (i, i), 1, 1, fill=True, facecolor="gray", edgecolor='k'))


# 軸線の表示
for ax in axs:
    ax.axhline(y=0, color='k', linewidth=2)
    ax.axhline(y=research_scores.shape[1], color='k', linewidth=2)
    ax.axvline(x=0, color='k', linewidth=2)
    ax.axvline(x=research_scores.shape[0], color='k', linewidth=2)
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=axis_label_fontsize)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=axis_label_fontsize)

plt.tight_layout()  # レイアウトの調整
plt.savefig("4_2_1_relation_heatmap.png", dpi=300)  # 画像を保存
plt.show()
