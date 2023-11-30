import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import networkx as nx  # グラフ解析のためのNetworkX
import pandas as pd  # データフレーム操作のためのPandas
import numpy as np  # 数値演算のためのNumPy
import matplotlib.cm as cm  # カラーマップのためのMatplotlib

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
                       research_score_data.T) / 2  # 対称行列にする
research_scores = pd.DataFrame(
    research_score_data, columns=researchers, index=researchers)  # データフレームに変換

# 共著データのネットワークを作成
collaboration_network = nx.from_pandas_adjacency(collaboration)  # ネットワークに変換
collaboration_network.remove_edges_from(
    nx.selfloop_edges(collaboration_network))  # 自己ループを削除

# 研究スコアのネットワークを作成
research_scores_network = nx.from_pandas_adjacency(
    research_scores)  # ネットワークに変換
research_scores_network.remove_edges_from(
    nx.selfloop_edges(research_scores_network))  # 自己ループを削除


fig, axes = plt.subplots(2, 2, figsize=(8, 8))  # サブプロットの作成

# 各サブプロットのアスペクト比を1に設定
for row in axes:
    for ax in row:
        ax.set_aspect('equal')

# 共著データのネットワークを円状に描画
plt.sca(axes[0, 0])
nx.draw_circular(
    collaboration_network, with_labels=True, width=2,
    edge_color='black', node_color='gray', font_color='white', font_size=15
)  # 円状にネットワークを描画

# 共著データのネットワークをspring layoutで描画
plt.sca(axes[0, 1])
nx.draw_spring(
    collaboration_network, with_labels=True, width=2,
    edge_color='black', node_color='gray', font_color='white', font_size=15
)  # spring layoutでネットワークを描画


# 研究スコアのネットワークを円状に描画
plt.sca(axes[1, 0])
edge_widths = [research_scores_network[u][v]['weight'] *
               5 for u, v in research_scores_network.edges()]  # エッジの太さを設定
edge_colors = [research_scores_network[u][v]['weight']
               for u, v in research_scores_network.edges()]  # エッジの色を設定

nx.draw_circular(
    research_scores_network, with_labels=True, width=edge_widths,
    edge_color=edge_colors, edge_cmap=plt.cm.jet, node_color='gray',
    font_color='white', font_size=15, edge_vmin=0, edge_vmax=1
)  # 円状にネットワークを描画

# 研究スコアのネットワークをspring layoutで描画
plt.sca(axes[1, 1])
edge_widths = [research_scores_network[u][v]['weight']
               * 5 for u, v in research_scores_network.edges()]
edge_colors = [research_scores_network[u][v]['weight']
               for u, v in research_scores_network.edges()]

nx.draw_spring(
    research_scores_network, with_labels=True, width=edge_widths,
    edge_color=edge_colors, edge_cmap=plt.cm.jet, node_color='gray',
    font_color='white', font_size=15, edge_vmin=0, edge_vmax=1
)  # spring layoutでネットワークを描画

plt.subplots_adjust(wspace=0.2, hspace=0.2)  # サブプロット間のスペース調整
plt.savefig("4_2_2_network_visualization.png", dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
