import networkx as nx  # ネットワーク解析のためのNetworkX
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy


# 適当なネットワークを生成
G = nx.erdos_renyi_graph(30, 0.1, seed=18)

# ノードの位置を計算
pos = nx.kamada_kawai_layout(G)

# Betweenness Centralityを計算
betweenness_centrality = nx.betweenness_centrality(G)

# Closeness Centralityを計算
closeness_centrality = nx.closeness_centrality(G)

# Eigen Centralityを計算
eigen_centrality = nx.eigenvector_centrality_numpy(G)

# Page Rankを計算
page_rank = nx.pagerank(G)

# サブプロットを描画
fig, axs = plt.subplots(2, 2, figsize=(12, 12))

# Betweenness Centrality
nx.draw(G, pos, ax=axs[0, 0], node_color=list(betweenness_centrality.values()), cmap=plt.cm.jet, with_labels=False)

# Closeness Centrality
nx.draw(G, pos, ax=axs[0, 1], node_color=list(closeness_centrality.values()), cmap=plt.cm.jet, with_labels=False)

# Eigen Centrality
nx.draw(G, pos, ax=axs[1, 0], node_color=list(eigen_centrality.values()), cmap=plt.cm.jet, with_labels=False)

# Page Rank
nx.draw(G, pos, ax=axs[1, 1], node_color=list(page_rank.values()), cmap=plt.cm.jet, with_labels=False)

plt.savefig("7_3_1_network_centrality_measures.png", dpi=300)  # 図を保存
plt.show()  # 図の表示
