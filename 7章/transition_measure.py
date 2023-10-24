# 必要なライブラリのインポート
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm
plt.rcParams['font.family'] = 'Yu Gothic'
np.random.seed(42)
# じゃんけんの手を表す定数
ROCK, SCISSORS, PAPER = 0, 1, 2

# データ生成関数


def generate_data(transition_prob, n=1000):
    states = [np.random.choice([ROCK, SCISSORS, PAPER])]
    for _ in range(n - 1):
        current_state = states[-1]
        next_state = np.random.choice([ROCK, SCISSORS, PAPER], p=transition_prob[current_state])
        states.append(next_state)
    return np.array(states)


# じゃんけんマシンAの遷移確率
transition_prob_A = {
    ROCK: [0.2, 0.5, 0.3],
    SCISSORS: [0.4, 0.1, 0.5],
    PAPER: [0.3, 0.6, 0.1]
}

# じゃんけんマシンBの遷移確率
transition_prob_B = {
    ROCK: [0.3, 0.4, 0.3],
    SCISSORS: [0.2, 0.3, 0.5],
    PAPER: [0.4, 0.2, 0.4]
}

# データ生成
data_A = generate_data(transition_prob_A)
data_B = generate_data(transition_prob_B)


# 最初の50回のじゃんけんの時系列を折れ線グラフで描画
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(range(50), data_A[:50], label='じゃんけんマシンA')
ax.plot(range(50), data_B[:50], label='じゃんけんマシンB')
ax.set_title('分析対象のジャンケン時系列（最初の50ラウンド）')
# ax.set_xticks(range(50))
ax.set_yticks([ROCK, SCISSORS, PAPER])
ax.set_yticklabels(['グー', 'チョキ', 'パー'])
ax.legend(loc='lower left')
plt.tight_layout()
plt.savefig('janken_ts.png', dpi=300)
plt.show()


# 各手の連続回数の平均値を計算


def calculate_run_mean(data):
    counts = {ROCK: [], SCISSORS: [], PAPER: []}
    run_count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            run_count += 1
        else:
            counts[data[i - 1]].append(run_count)
            run_count = 1
    return {key: np.mean(val) for key, val in counts.items()}


mean_run_A = calculate_run_mean(data_A)
mean_run_B = calculate_run_mean(data_B)

# データから遷移確率を計算する関数


def calculate_empirical_transition_prob(data):
    counts = {
        ROCK: {ROCK: 0, SCISSORS: 0, PAPER: 0},
        SCISSORS: {ROCK: 0, SCISSORS: 0, PAPER: 0},
        PAPER: {ROCK: 0, SCISSORS: 0, PAPER: 0}
    }

    for i in range(len(data) - 1):
        current_state = data[i]
        next_state = data[i + 1]
        counts[current_state][next_state] += 1

    transition_prob_emp = {}
    for state, next_states in counts.items():
        total = sum(next_states.values())
        transition_prob_emp[state] = [next_states[ROCK] / total, next_states[SCISSORS] / total, next_states[PAPER] / total]

    return transition_prob_emp


# 実際のデータから遷移確率を計算
transition_prob_emp_A = calculate_empirical_transition_prob(data_A)
transition_prob_emp_B = calculate_empirical_transition_prob(data_B)

# さらに修正されたネットワーク描画関数

# 日本語ラベルを使用したネットワーク描画関数


def plot_transition_graph(ax, prob_matrix, title):
    G = nx.DiGraph()
    jp_labels = {0: 'グー', 1: 'チョキ', 2: 'パー'}
    labels = {}
    edge_widths = []
    edge_colors = []
    for i, state1 in enumerate([ROCK, SCISSORS, PAPER]):
        for j, state2 in enumerate([ROCK, SCISSORS, PAPER]):
            G.add_edge(jp_labels[state1], jp_labels[state2], weight=prob_matrix[i][j])
            labels[(jp_labels[state1], jp_labels[state2])] = f"{prob_matrix[i][j]:.2f}"
            edge_widths.append(prob_matrix[i][j] * 10)
            edge_colors.append(prob_matrix[i][j])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, ax=ax, with_labels=False, node_color='lightblue', font_weight='bold',
            node_size=700, font_size=18, connectionstyle='arc3,rad=0.3', edge_color=edge_colors,
            width=edge_widths, edge_cmap=plt.cm.jet, arrowstyle='-|>')

    for edge, label in labels.items():
        p1, p2 = pos[edge[0]], pos[edge[1]]
        p = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
        if p1[0] != p2[0]:
            # ベクトルの方向を計算
            d = [p2[0] - p1[0], p2[1] - p1[1]]
            # 垂直なベクトルを計算
            n = [-d[1], d[0]]
            # 正規化
            norm = np.sqrt(n[0]**2 + n[1]**2)
            n = [n[0] / norm, n[1] / norm]
            # ずらす距離
            shift = 0.1
            # ラベルの位置をずらす
            ax.text(p[0] - n[0] * shift, p[1] - n[1] * shift, label, fontsize=10, ha='center', va='center')
        else:
            shift = 0.15
            ax.text(p[0] + shift, p[1] + shift, label, fontsize=10, ha='center', va='center')

        # # ラベルの位置をずらす
        # shift = 0.2 if p1[0] >= p2[0] else 0
        # ax.text(p[0] + shift, p[1] + shift, label, fontsize=10, ha='center', va='center')

    for node, (x, y) in pos.items():
        ax.text(x, y, node, fontsize=12, ha='center', va='center')

    ax.set_title(title)


# 描画（集団棒グラフとネットワークグラフを含む）
fig, axes = plt.subplots(2, 2, figsize=(8, 8))
bar_width = 0.35
index = np.arange(3)

# 集団棒グラフで各手の出現割合を描画
bar1 = axes[0, 0].bar(index, [np.sum(data_A == ROCK) / 1000, np.sum(data_A == SCISSORS) / 1000, np.sum(data_A == PAPER) / 1000], bar_width, alpha=0.5, label='じゃんけんマシンA')
bar2 = axes[0, 0].bar(index + bar_width, [np.sum(data_B == ROCK) / 1000, np.sum(data_B == SCISSORS) / 1000, np.sum(data_B == PAPER) / 1000], bar_width, alpha=0.5, label='じゃんけんマシンB')
axes[0, 0].set_xticks(index + bar_width / 2)
axes[0, 0].set_xticklabels(['グー', 'チョキ', 'パー'])
axes[0, 0].set_title('出現頻度')
axes[0, 0].legend(loc='lower left')

# 集団棒グラフで各手の連続回数の平均値を描画
bar1 = axes[0, 1].bar(index, [mean_run_A[ROCK], mean_run_A[SCISSORS], mean_run_A[PAPER]], bar_width, alpha=0.5, label='Machine A')
bar2 = axes[0, 1].bar(index + bar_width, [mean_run_B[ROCK], mean_run_B[SCISSORS], mean_run_B[PAPER]], bar_width, alpha=0.5, label='Machine B')
axes[0, 1].set_xticks(index + bar_width / 2)
axes[0, 1].set_xticklabels(['グー', 'チョキ', 'パー'])
axes[0, 1].set_title('持続回数の平均値')
# axes[0, 1].legend()

# 実際のデータから計算した遷移確率のネットワークグラフを描画
plot_transition_graph(axes[1, 0], transition_prob_emp_A, '遷移確率（じゃんけんマシンA）')
plot_transition_graph(axes[1, 1], transition_prob_emp_B, '遷移確率（じゃんけんマシンB）')

plt.tight_layout()
plt.savefig('janken_analysis.png', dpi=300)
plt.show()
