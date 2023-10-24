import networkx as nx
import matplotlib.pyplot as plt

# グラフオブジェクトを作成
G = nx.Graph()

# ノードを追加
G.add_nodes_from([1, 2, 3, 4, 5])

# エッジを追加
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (3, 5)])

# グラフを描画
nx.draw(G)
plt.show()
