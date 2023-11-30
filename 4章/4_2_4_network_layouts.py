import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import networkx as nx  # グラフ解析のためのNetworkX
import numpy as np  # 数値演算のためのNumPy
from networkx.drawing.nx_pydot import graphviz_layout  # Graphvizのレイアウト


G_er = nx.erdos_renyi_graph(30, 0.2)  # ERネットワーク
G_ws = nx.watts_strogatz_graph(30, 5, 0.1)  # Watts-Strogatzネットワーク
G_ba = nx.barabasi_albert_graph(30, 1)  # Barabasi-Albertネットワーク

# レイアウトを設定
layouts = ['circular', 'circo', 'kamada_kawai']

fig, axes = plt.subplots(len(layouts), 3, figsize=(10, 10))  # サブプロットを生成

# 各ネットワークをリストに格納しループで描画する
graphs = [G_er, G_ws, G_ba]
titles = ['ER Network', 'Watts-Strogatz Network',
          'Barab\u00E1si-Albert Network']
node_color = ["blue", "orange", "green"]
# 各ネットワークとレイアウトでループ
for i, layout in enumerate(layouts):
    for j, graph in enumerate(graphs):
        ax = axes[i][j]
        if i <= 2:
            ax.set_aspect('equal')
        if layout == 'circular':
            pos = nx.circular_layout(graph)  # 円形レイアウトを使用
        elif layout == 'circo':
            # Graphvizのcircoレイアウトを使用
            pos = graphviz_layout(graph, prog='circo')
        elif layout == 'kamada_kawai':
            pos = nx.kamada_kawai_layout(graph)  # Kamada-Kawaiレイアウトを使用

        nx.draw(
            graph, pos, with_labels=False, ax=ax,
            node_size=40, edge_color="gray", node_color=node_color[i]
        )  # ネットワークを描画


plt.tight_layout()  # レイアウトの調整
plt.savefig("4_2_4_network_layouts.png", dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
