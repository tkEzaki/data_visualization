import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from scipy.stats import wasserstein_distance, entropy, ks_2samp, chisquare  # 距離指標のためのSciPy
from sklearn.metrics import mutual_info_score  # 相互情報量のためのscikit-learn
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 15  # フォントサイズを設定

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


sample_size = 1000  # サンプルサイズ
mean1, std1 = 0, 1  # 分布１のパラメータ
mean2, std2 = 1, 1  # 分布２のパラメータ
dist1_1 = np.random.normal(mean1, std1, sample_size)  # 分布１のサンプルデータ
dist1_2 = np.random.normal(mean2, std2, sample_size)  # 分布２のサンプルデータ

mean3, std3 = -1, 0.5  # 分布３のパラメータ
mean4, std4 = 1, 1.5  # 分布４のパラメータ
dist2_1 = np.random.normal(mean3, std3, sample_size)  # 分布３のサンプルデータ
dist2_2 = np.random.normal(mean4, std4, sample_size)  # 分布４のサンプルデータ

mean5, std5 = -2, 1  # 分布５のパラメータ
mean6, std6 = 2, 1  # 分布６のパラメータ
mean7, std7 = 0, 1.5  # 分布７のパラメータ
dist3_1 = np.concatenate([np.random.normal(mean5, std5, sample_size // 2),
                          np.random.normal(mean6, std6, sample_size // 2)])
dist3_2 = np.random.normal(mean7, std7, sample_size)

# 全体で使用する色
common_colors = ['darkblue', 'darkorange']

# ビンの幅をすべての分布で同じにするためにすべてのデータから最小値と最大値を取得
all_data = np.concatenate([dist1_1, dist1_2, dist2_1, dist2_2, dist3_1, dist3_2])
min_val = np.min(all_data)
max_val = np.max(all_data)

# ビンのエッジを計算
bin_edges = np.linspace(min_val, max_val, 21)

# 各距離指標を計算
metrics = ['コルモゴロフ・スミルノフ統計量', '全変動距離', 'ワッサースタイン距離', 'JS情報量']
distances1 = compute_metrics(dist1_1, dist1_2, bin_edges)
distances2 = compute_metrics(dist2_1, dist2_2, bin_edges)
distances3 = compute_metrics(dist3_1, dist3_2, bin_edges)

# 棒グラフのY軸のスケールを調整
max_distance = 2.5

# 分布ペアのヒストグラムを描画
fig1, axes1 = plt.subplots(1, 3, figsize=(10, 3.3))

axes1[0].hist(dist1_1, alpha=0.5, label=f'N({mean1},{std1}^2)', bins=bin_edges, color=common_colors[0])
axes1[0].hist(dist1_2, alpha=0.5, label=f'N({mean2},{std2}^2)', bins=bin_edges, color=common_colors[1])
axes1[0].set_title('分布ペア１')

axes1[1].hist(dist2_1, alpha=0.5, label=f'N({mean3},{std3}^2)', bins=bin_edges, color=common_colors[0])
axes1[1].hist(dist2_2, alpha=0.5, label=f'N({mean4},{std4}^2)', bins=bin_edges, color=common_colors[1])
axes1[1].set_title('分布ペア２')

axes1[2].hist(dist3_1, alpha=0.5, label=f'GMM', bins=bin_edges, color=common_colors[0])
axes1[2].hist(dist3_2, alpha=0.5, label=f'N({mean7},{std7}^2)', bins=bin_edges, color=common_colors[1])
axes1[2].set_title('分布ペア３')

plt.tight_layout()  # レイアウトの設定
plt.savefig('6_2_5_1_dist_pairs.png', dpi=300)  # 図の保存
plt.show()  # 図の表示


# 各指標の距離をグループ棒グラフとして描画
fig2, ax2 = plt.subplots(figsize=(10, 3.3))
x = np.arange(len(metrics))  # x軸の値
width = 0.15  # 棒の幅

# 各指標の描画
ax2.bar(x - width * 1.2, distances1, width, label='分布ペア１', color=common_colors[0])
ax2.bar(x, distances2, width, label='分布ペア２', color=common_colors[1])
ax2.bar(x + width * 1.2, distances3, width, label='分布ペア３', color='green')

ax2.set_title('各指標における分布ペアの距離')  # タイトルを設定
ax2.set_xticks(x)  # x軸の目盛りを設定
ax2.set_xticklabels(metrics)  # x軸の目盛りのラベルを設定
ax2.legend()  # 凡例を表示
ax2.set_ylim(0, max_distance)  # y軸の範囲を設定

plt.tight_layout()  # レイアウトの設定
plt.savefig('6_2_5_2_dist_metrics.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
