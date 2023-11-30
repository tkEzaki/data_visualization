import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.patches as patches
import japanize_matplotlib

plt.rcParams['font.size'] = 14

axis_label_fontsize = 14
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
np.random.seed(0)


# 研究スコア
research_scores = np.zeros((10, 10))
for i in range(10):
    for j in range(10):
        if i == j:
            research_scores[i][j] = np.nan  # 自分自身との類似度は1
        elif collaboration.iloc[i, j] == 1:
            research_scores[i][j] = np.random.uniform(0.5, 1.0)
        else:
            research_scores[i][j] = np.random.uniform(0.0, 0.5)
            
research_scores = (research_scores + research_scores.T) / 2  # 対称行列にする
research_scores = pd.DataFrame(research_scores, columns=researchers, index=researchers)

# ヒートマップの描画
fig, axs = plt.subplots(ncols=2, figsize=(10, 4.5))

# ax = sns.heatmap(collaboration, annot=True, fmt=".0f", xticklabels=researchers, yticklabels=researchers, cmap='binary', cbar_kws={'label':'共著関係', 'ticks': [0, 1]}, linewidths=0.5, linecolor='black', ax=axs[0])
ax = sns.heatmap(collaboration, annot=True, fmt=".0f", xticklabels=researchers, yticklabels=researchers, cmap='binary', cbar_kws={'label':'', 'ticks': []}, linewidths=0.5, linecolor='black', ax=axs[0])

ax.xaxis.tick_top()  # Set the x-axis labels to the top




# Add hatches to the diagonal
for i in range(len(researchers)):
    ax.add_patch(patches.Rectangle((i, i), 1, 1, fill=True, facecolor="gray", edgecolor='k'))

ax_2 = sns.heatmap(research_scores, annot=True, fmt=".1f", xticklabels=researchers, yticklabels=researchers, cmap='jet', cbar_kws={'label':'類似度スコア', 'ticks': [0, 0.2,0.4,0.6,0.8,1]}, linewidths=0.5, linecolor='black', ax=axs[1])
axs[1].xaxis.tick_top()  # Set the x-axis labels to the top

# Add hatches to the diagonal
for i in range(len(researchers)):
    ax_2.add_patch(patches.Rectangle((i, i), 1, 1, fill=True, facecolor="gray", edgecolor='k'))


# 軸線の表示
for ax in axs:
    ax.axhline(y=0, color='k', linewidth=2)
    ax.axhline(y=research_scores.shape[1], color='k', linewidth=2)
    ax.axvline(x=0, color='k', linewidth=2)
    ax.axvline(x=research_scores.shape[0], color='k', linewidth=2)
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=axis_label_fontsize)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=axis_label_fontsize)

plt.tight_layout()
plt.savefig("4_2_1_relation_heatmap.png", dpi=300)
plt.savefig("4_2_1_relation_heatmap.svg", dpi=300)

plt.show()
