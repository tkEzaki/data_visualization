import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from networkx.drawing.nx_pydot import graphviz_layout

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
            G.add_edge(researcher, collaborator)

# グラフの描画
plt.figure(figsize=(4, 4))
# pos = nx.shell_layout(G)
pos = graphviz_layout(G, prog="dot")
nx.draw(G, pos, with_labels=True, node_color='gray', node_size=500, edge_color='black', font_color="white")
plt.savefig("network_hierarchy.png", dpi=300)
plt.show()
