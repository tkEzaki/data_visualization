import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.cm as cm

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

# 共著データのネットワークを作成
collaboration_network = nx.from_pandas_adjacency(collaboration)
collaboration_network.remove_edges_from(nx.selfloop_edges(collaboration_network))  # 自己ループを削除

# 研究スコアのネットワークを作成
research_scores_network = nx.from_pandas_adjacency(research_scores)
research_scores_network.remove_edges_from(nx.selfloop_edges(research_scores_network))  # 自己ループを削除

fig, axes = plt.subplots(2, 2, figsize=(8, 8))

# 各サブプロットのアスペクト比を1に設定
for row in axes:
    for ax in row:
        ax.set_aspect('equal')

# 共著データのネットワークを円状に描画
plt.sca(axes[0, 0])
nx.draw_circular(collaboration_network, with_labels=True, width=2, edge_color='black', node_color='gray', font_color='white')
# axes[0, 0].set_title("Collaboration Network - Circular Layout")

# 共著データのネットワークをspring layoutで描画
plt.sca(axes[0, 1])
nx.draw_spring(collaboration_network, with_labels=True, width=2, edge_color='black', node_color='gray', font_color='white')
# axes[0, 1].set_title("Collaboration Network - Spring Layout")

# 研究スコアのネットワークを円状に描画
plt.sca(axes[1, 0])
edge_widths = [research_scores_network[u][v]['weight'] * 5 for u, v in research_scores_network.edges()]
edge_colors = [research_scores_network[u][v]['weight'] for u, v in research_scores_network.edges()]
nx.draw_circular(research_scores_network, with_labels=True, width=edge_widths, edge_color=edge_colors, edge_cmap=plt.cm.jet, node_color='gray', font_color='white', edge_vmin=0, edge_vmax=1)
# axes[1, 0].set_title("Research Scores Network - Circular Layout")

# 研究スコアのネットワークをspring layoutで描画
plt.sca(axes[1, 1])
edge_widths = [research_scores_network[u][v]['weight'] * 5 for u, v in research_scores_network.edges()]
edge_colors = [research_scores_network[u][v]['weight'] for u, v in research_scores_network.edges()]
nx.draw_spring(research_scores_network, with_labels=True, width=edge_widths, edge_color=edge_colors, edge_cmap=plt.cm.jet, node_color='gray', font_color='white', edge_vmin=0, edge_vmax=1)
# axes[1, 1].set_title("Research Scores Network - Spring Layout")

plt.tight_layout()
# spaceを調整
plt.subplots_adjust(wspace=0.2, hspace=0.2)
plt.savefig("network.png", dpi=300)
plt.show()
