import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.patches as patches
import japanize_matplotlib

plt.rcParams["font.size"] = 16


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

# ax = sns.heatmap(collaboration, annot=True, fmt=".0f", xticklabels=researchers, yticklabels=researchers, cmap='binary', cbar_kws={'ticks': [0, 1]}, linewidths=0.5, linecolor='black', ax=ax)
ax = sns.heatmap(collaboration, annot=True, fmt=".0f", xticklabels=researchers, yticklabels=researchers, cmap='binary', cbar_kws={'ticks': []}, linewidths=0.5, linecolor='black', ax=ax)

ax.xaxis.tick_top()  # Set the x-axis labels to the top
ax.set_title("指導された研究者", fontsize=16)
ax.set_ylabel("指導した研究者")

# Add hatches to the diagonal
for i in range(len(researchers)):
    ax.add_patch(patches.Rectangle((i, i), 1, 1, fill=True, facecolor="gray", edgecolor='k'))

# 軸線の表示
ax.axhline(y=0, color='k', linewidth=2)
ax.axhline(y=collaboration.shape[1], color='k', linewidth=2)
ax.axvline(x=0, color='k', linewidth=2)
ax.axvline(x=collaboration.shape[0], color='k', linewidth=2)

plt.savefig("4_2_3_1_hierarchy_relation_heatmap.png", dpi=300)
plt.savefig("4_2_3_1_hierarchy_relation_heatmap.svg", dpi=300)

plt.show()
