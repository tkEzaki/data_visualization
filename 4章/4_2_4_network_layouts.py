import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from networkx.drawing.nx_pydot import graphviz_layout


# ネットワークを生成 seedは指定する
G_er = nx.erdos_renyi_graph(30, 0.2)  # ERネットワーク
G_ws = nx.watts_strogatz_graph(30, 5, 0.1)  # Watts-Strogatzネットワーク
G_ba = nx.barabasi_albert_graph(30, 1)  # Barabasi-Albertネットワーク

# レイアウトを設定
layouts = ['circular', 'circo', 'kamada_kawai']

fig, axes = plt.subplots(len(layouts), 3, figsize=(10, 10))  # サブプロットを生成

graphs = [G_er, G_ws, G_ba]
titles = ['ER Network', 'Watts-Strogatz Network', 'Barab\u00E1si-Albert Network']
node_color = ["blue", "orange", "green"]
# 各ネットワークとレイアウトでループ
for i, layout in enumerate(layouts):
    for j, graph in enumerate(graphs):
        ax = axes[i][j]
        if i <= 2:
            ax.set_aspect('equal')
        if layout == 'circular':
            pos = nx.circular_layout(graph)  # レイアウトの位置を決定
        elif layout == 'circo':
            pos = graphviz_layout(graph, prog='circo')
        elif layout == 'kamada_kawai':
            pos = nx.kamada_kawai_layout(graph)
        nx.draw(graph, pos, with_labels=False, ax=ax, node_size=40, edge_color="gray", node_color=node_color[i])  # ネットワークを描画
        # if i == 0:
        #     ax.set_title(titles[j])
        # if j == 0:
        #     ax.set_ylabel(layout)

plt.tight_layout()
plt.savefig("4_2_4_network_layouts.png", dpi=300)
plt.savefig("4_2_4_network_layouts.svg", dpi=300)

plt.show()
