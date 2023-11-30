import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import japanize_matplotlib

plt.rcParams["font.size"] = 15

# ネットワーク生成部分
n = 49
m = 1

dim = int(np.sqrt(n))
G_square = nx.grid_2d_graph(dim, dim, periodic=False)
old_pos_square = {(i, j): (j, -i) for i, j in G_square.nodes()}
mapping = {old: new for new, old in enumerate(G_square.nodes())}
G_square = nx.relabel_nodes(G_square, mapping)
pos_square = {mapping[old]: coord for old, coord in old_pos_square.items()}

G_random = nx.erdos_renyi_graph(n, 0.2, seed=1)
pos_random = nx.kamada_kawai_layout(G_random)

G_ba = nx.barabasi_albert_graph(n, m, seed=0)
pos_ba = nx.spring_layout(G_ba)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

fig, axs = plt.subplots(1, 3, figsize=(18, 6))
nx.draw(G_square, pos=pos_square, ax=axs[0], with_labels=False, node_color=colors[0])
nx.draw(G_random, pos=pos_random, ax=axs[1], with_labels=False, node_color=colors[1])
nx.draw(G_ba, pos=pos_ba, ax=axs[2], with_labels=False, node_color=colors[2])
plt.tight_layout()
plt.savefig('7_3_2_1_example_networks.png', dpi=300)
plt.savefig('7_3_2_1_example_networks.svg', dpi=300)

plt.show()


def compute_network_metrics(G):
    metrics = {}
    metrics['平均次数'] = np.mean([d for n, d in G.degree()])
    metrics['平均最短経路長'] = nx.average_shortest_path_length(G)
    metrics['クラスター係数'] = nx.average_clustering(G)
    metrics['同類選択性'] = nx.degree_assortativity_coefficient(G)
    return metrics


metrics_square = compute_network_metrics(G_square)
metrics_random = compute_network_metrics(G_random)
metrics_ba = compute_network_metrics(G_ba)

labels = list(metrics_square.keys())
network_names = ['格子', 'ランダム', 'BA']

square_vals = [metrics_square[label] for label in labels]
random_vals = [metrics_random[label] for label in labels]
ba_vals = [metrics_ba[label] for label in labels]

x = np.arange(len(labels))
width = 0.3


# 指標ごとにサブプロット
fig, axs = plt.subplots(1, len(labels), figsize=(10, 5))


def add_values(ax, values, colors):
    for i, (value, color) in enumerate(zip(values, colors)):
        if not np.isnan(value):
            ax.annotate(f'{value:.2f}',
                        xy=(i, value),
                        xytext=(0, -1),
                        textcoords="offset points",
                        ha='center', va='bottom')
        else:
            ax.annotate('NA',
                        xy=(i, 0),
                        xytext=(0, -1),
                        textcoords="offset points",
                        ha='center', va='bottom')
            ax.bar(i, 0, color=color)  # nanでも色を付ける


for i, label in enumerate(labels):
    ax = axs[i]
    values = [metrics_square[label], metrics_random[label], metrics_ba[label]]
    bars = ax.bar(network_names, values, color=colors)
    ax.set_xticklabels(network_names, rotation=30, ha='right')
    ax.set_title(label, fontsize=15)
    add_values(ax, values, colors)

plt.tight_layout()
plt.savefig('7_3_2_2_network_metrics_comparison.png', dpi=300)
plt.savefig('7_3_2_2_network_metrics_comparison.svg', dpi=300)

plt.show()
