import matplotlib.pyplot as plt
import networkx as nx
import random
from networkx.drawing.nx_pydot import graphviz_layout

# ランダム有向グラフを生成
G_dir_random = nx.DiGraph()
for i in range(30):
    for j in range(30):
        if random.random() < 0.1 and i != j:
            G_dir_random.add_edge(i, j)

# ヒエラルキーのある有向グラフを生成
G_dir_hierarchy = nx.DiGraph()
edges = []
for i in range(1, 30):
    edges.append((random.randrange(0, i), i))  # 各ノードは前方の全てのノードからランダムに接続
G_dir_hierarchy.add_edges_from(edges)

# レイアウトを設定
layouts = ['dot', 'circo', 'kamada_kawai']

fig, axes = plt.subplots(len(layouts), 2, figsize=(8, 10))  # サブプロットを生成

graphs = [G_dir_random, G_dir_hierarchy]
titles = ['Directed Random Graph', 'Directed Graph with Wide Hierarchy']
colors = ["violet", "orange", "green"]
# 各グラフとレイアウトでループ
for i, layout in enumerate(layouts):
    for j, graph in enumerate(graphs):
        ax = axes[i][j]
        ax.set_aspect('equal')
        if layout == 'dot' or layout == 'circo':
            pos = graphviz_layout(graph, prog=layout)  # レイアウトの位置を決定
        elif layout == 'kamada_kawai':
            pos = nx.kamada_kawai_layout(graph)
        nx.draw(graph, pos, with_labels=False, ax=ax, node_size=20, edge_color="gray", node_color=colors[i], arrows=True)  # グラフを描画
        # if i == 0:
        #     ax.set_title(titles[j])
        # if j == 0:
        #     ax.set_ylabel(layout, size='large')

plt.tight_layout()
plt.savefig("directed_graph_layouts.png", dpi=300)
plt.show()
