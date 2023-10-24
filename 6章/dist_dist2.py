import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import wasserstein_distance, entropy, ks_2samp, chisquare
from sklearn.metrics import mutual_info_score

plt.rcParams['font.family'] = 'Yu Gothic'
plt.rcParams['font.size'] = 16

# 相互情報量
def mutual_information(x, y, n_bins=20):
    hist_x, _ = np.histogram(x, bins=n_bins)
    hist_y, _ = np.histogram(y, bins=n_bins)
    mi = mutual_info_score(hist_x, hist_y)
    return mi

# スミルノフ-コロモゴロフ統計量
def ks_statistic(x, y):
    return ks_2samp(x, y).statistic

# カイ二乗統計量
def chi_square_statistic(x, y, bin_edges):
    hist_x, _ = np.histogram(x, bins=bin_edges)
    hist_y, _ = np.histogram(y, bins=bin_edges)
    return chisquare(hist_x, hist_y).statistic

# KLダイバージェンス
def kl_divergence(p, q):
    kl_div = entropy(p, q)
    return kl_div if kl_div != np.inf else 0

# JSダイバージェンス
def js_divergence(p, q):
    m = 0.5 * (p + q)
    return 0.5 * kl_divergence(p, m) + 0.5 * kl_divergence(q, m)

# 全変動距離
def total_variation_distance(p, q):
    return 0.5 * np.sum(np.abs(p - q))

# 指標を計算
def compute_metrics(dist_a, dist_b, bin_edges):
    hist_a, _ = np.histogram(dist_a, bins=bin_edges, density=True)
    hist_b, _ = np.histogram(dist_b, bins=bin_edges, density=True)
    return [
        ks_statistic(dist_a, dist_b),
        total_variation_distance(hist_a, hist_b),
        wasserstein_distance(bin_edges[:-1], bin_edges[:-1], hist_a, hist_b),
        js_divergence(hist_a, hist_b),
    ]

plt.rcParams['font.family'] = 'Yu Gothic'
sample_size = 1000
mean1_new, std1_new = 0, 1
mean2_new, std2_new = 1, 1
dist1_1_new = np.random.normal(mean1_new, std1_new, sample_size)
dist1_2_new = np.random.normal(mean2_new, std2_new, sample_size)
mean3_new, std3_new = -1, 0.5
mean4_new, std4_new = 1, 1.5
dist2_1_new = np.random.normal(mean3_new, std3_new, sample_size)
dist2_2_new = np.random.normal(mean4_new, std4_new, sample_size)
mean5, std5 = -2, 1
mean6, std6 = 2, 1
mean7, std7 = 0, 1.5
dist3_1 = np.concatenate([np.random.normal(mean5, std5, sample_size // 2),
                          np.random.normal(mean6, std6, sample_size // 2)])
dist3_2 = np.random.normal(mean7, std7, sample_size)

# 全体で使用する色
common_colors = ['darkblue', 'darkorange']

# ビンの幅をすべての分布で同じにするために、すべてのデータから最小値と最大値を取得
all_data = np.concatenate([dist1_1_new, dist1_2_new, dist2_1_new, dist2_2_new, dist3_1, dist3_2])
min_val = np.min(all_data)
max_val = np.max(all_data)

# ビンのエッジを計算
bin_edges = np.linspace(min_val, max_val, 21)

# 各距離指標を計算
metrics = ['コルモゴロフ・スミルノフ統計量', '全変動距離', 'ワッサースタイン距離', 'JS情報量']
distances1 = compute_metrics(dist1_1_new, dist1_2_new, bin_edges)
distances2 = compute_metrics(dist2_1_new, dist2_2_new, bin_edges)
distances3 = compute_metrics(dist3_1, dist3_2, bin_edges)

# 棒グラフのY軸のスケールを調整
max_distance = 2.5

# 分布ペアのヒストグラムを描画（個別の図として）
fig1, axes1 = plt.subplots(1, 3, figsize=(12, 4))

axes1[0].hist(dist1_1_new, alpha=0.5, label=f'N({mean1_new},{std1_new}^2)', bins=bin_edges, color=common_colors[0])
axes1[0].hist(dist1_2_new, alpha=0.5, label=f'N({mean2_new},{std2_new}^2)', bins=bin_edges, color=common_colors[1])
axes1[0].set_title('分布ペア１')
# axes1[0].legend()

axes1[1].hist(dist2_1_new, alpha=0.5, label=f'N({mean3_new},{std3_new}^2)', bins=bin_edges, color=common_colors[0])
axes1[1].hist(dist2_2_new, alpha=0.5, label=f'N({mean4_new},{std4_new}^2)', bins=bin_edges, color=common_colors[1])
axes1[1].set_title('分布ペア２')
# axes1[1].legend()

axes1[2].hist(dist3_1, alpha=0.5, label=f'GMM', bins=bin_edges, color=common_colors[0])
axes1[2].hist(dist3_2, alpha=0.5, label=f'N({mean7},{std7}^2)', bins=bin_edges, color=common_colors[1])
axes1[2].set_title('分布ペア３')
# axes1[2].legend()

plt.tight_layout()
plt.savefig('dist_pairs.png')
# plt.show()

# 各指標の距離をグループ棒グラフとして描画
fig2, ax2 = plt.subplots(figsize=(12, 4))
x = np.arange(len(metrics))
width = 0.15

ax2.bar(x - width*1.2, distances1, width, label='分布ペア１', color=common_colors[0])
ax2.bar(x, distances2, width, label='分布ペア２', color=common_colors[1])
ax2.bar(x + width*1.2, distances3, width, label='分布ペア３', color='green')

ax2.set_title('各指標における分布ペアの距離')
ax2.set_xticks(x)
ax2.set_xticklabels(metrics)
ax2.legend()
ax2.set_ylim(0, max_distance)

plt.tight_layout()
plt.savefig('dist_metrics.png')
# plt.show()
