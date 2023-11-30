import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import networkx as nx  # グラフ解析のためのNetworkX
import random  # 乱数生成のためのrandom
from networkx.drawing.nx_pydot import graphviz_layout  # Graphvizのレイアウト

# ランダム有向グラフを生成
G_dir_random = nx.DiGraph()  # 有向グラフを生成

for i in range(30):
    for j in range(30):
        if random.random() < 0.1 and i != j:
            G_dir_random.add_edge(i, j)  # 10%の確率でエッジを追加


# ヒエラルキーのある有向グラフを生成
G_dir_hierarchy = nx.DiGraph()
edges = []
for i in range(1, 30):
    edges.append((random.randrange(0, i), i))  # 各ノードは前方の全てのノードからランダムに接続

G_dir_hierarchy.add_edges_from(edges)  # エッジを追加


# レイアウトを設定
layouts = ['dot', 'circo', 'kamada_kawai']

fig, axes = plt.subplots(len(layouts), 2, figsize=(8, 10))  # サブプロットを生成

# 各グラフとレイアウトでループ
graphs = [G_dir_random, G_dir_hierarchy]
titles = ['Directed Random Graph', 'Directed Graph with Wide Hierarchy']
colors = ["violet", "orange", "green"]

for i, layout in enumerate(layouts):
    for j, graph in enumerate(graphs):
        ax = axes[i][j]
        ax.set_aspect('equal')  # アスペクト比を1に設定
        if layout == 'dot' or layout == 'circo':
            pos = graphviz_layout(graph, prog=layout)  # レイアウトの位置を決定
        elif layout == 'kamada_kawai':
            pos = nx.kamada_kawai_layout(graph)  # Kamada-Kawaiレイアウトを使用

        nx.draw(
            graph, pos, with_labels=False, ax=ax,
            node_size=40, edge_color="gray",
            node_color=colors[i], arrows=True
        )  # グラフを描画

plt.tight_layout()  # レイアウトの調整
plt.savefig("4_2_5_network_layouts_directed.png", dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
