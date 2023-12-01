import networkx as nx  # ネットワーク解析のためのNetworkX
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy

# 乱数のシードを設定
np.random.seed(1)

# 図の準備
plt.figure(figsize=(4, 4))

# グラフ（バーベルグラフ）を生成
G = nx.barbell_graph(5, 1)

# 基準となるノード（ここではノード 0）
source_node = 0

# 基準ノードからの最短距離を計算
shortest_paths = nx.single_source_shortest_path_length(G, source_node)

# ネットワークを描画する際のノードの色を設定
node_colors = ['gold' if node ==
               source_node else 'lightblue' for node in G.nodes()]

# ネットワークを描画
pos = nx.spring_layout(G)  # 位置を計算
nx.draw(G, pos, with_labels=False, node_color=node_colors,
        font_weight='bold')  # node_colorにリストを指定

# ノードに基準ノードからの最短距離をラベルとして追加
labels = {node: f"{dist}" for node, dist in shortest_paths.items()}
nx.draw_networkx_labels(G, pos, labels=labels)  # ラベルを描画

plt.savefig("6_1_4_network_distance.png", dpi=300)  # 図を保存
plt.show()  # 図の表示
