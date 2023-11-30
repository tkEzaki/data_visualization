import networkx as nx  # グラフ解析のためのNetworkX
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import pandas as pd  # データフレーム操作のためのPandas
import numpy as np  # 数値演算のためのNumPy
from networkx.drawing.nx_pydot import graphviz_layout  # Graphvizのレイアウト

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

# ネットワークの作成
G = nx.DiGraph()

# エッジの追加
for i, researcher in enumerate(researchers):
    for j, collaborator in enumerate(researchers):
        if collaboration.loc[researcher, collaborator] == 1:
            G.add_edge(researcher, collaborator)  # 共著者がいる場合はエッジを追加

# グラフの描画
plt.figure(figsize=(4, 4))
pos = graphviz_layout(G, prog="dot")  # Graphvizのdotレイアウトを使用
nx.draw(
    G, pos, with_labels=True, node_color='gray',
    node_size=500, edge_color='black', font_color="white",
    font_size=16
)  # グラフを描画
plt.savefig("4_2_3_2_hierarchy_network_visualization.png", dpi=300)  # 画像の保存
plt.show()  # 画像の表示
