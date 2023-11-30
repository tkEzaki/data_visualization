import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp, cumfreq
import japanize_matplotlib

plt.rcParams["font.size"] = 14
np.random.seed(42)

# サンプルサイズを設定します。
sample_size = 1000

# 一つ目と二つ目の分布ペアを生成します。
mean1, std1 = 0, 1
mean2, std2 = 0.1, 1
dist1 = np.random.normal(mean1, std1, sample_size)
dist2 = np.random.normal(mean2, std2, sample_size)

# Kolmogorov-Smirnov 統計量を計算します。
ks_stat, p_value = ks_2samp(dist1, dist2)

# 累積分布関数 (CDF) を計算します。
dist1_sorted = np.sort(dist1)
dist2_sorted = np.sort(dist2)
cdf1 = np.arange(1, sample_size + 1) / sample_size
cdf2 = np.arange(1, sample_size + 1) / sample_size


# ヒストグラムとCDFを再プロットしますが、今度はヒストグラムのビンを共通にし、KS statisticがCDFの差と一致する場所を明示します。
fig, axes = plt.subplots(2, 1, figsize=(8, 8))

# 共通のビンエッジを生成します。
bin_edges = np.linspace(min(dist1.min(), dist2.min()), max(dist1.max(), dist2.max()), 51)

# ヒストグラムをプロットします。
axes[0].hist(dist1, alpha=0.5, bins=bin_edges, label='分布１', color='blue')
axes[0].hist(dist2, alpha=0.5, bins=bin_edges, label='分布２', color='orange')
# axes[0].set_title('ヒストグラム')
axes[0].legend()
axes[0].set_ylabel('頻度')

# CDFをプロットします。
axes[1].plot(dist1_sorted, cdf1, label='分布１', color='blue')
axes[1].plot(dist2_sorted, cdf2, label='分布２', color='orange')

# CDFの差がKS statisticと一致する場所を見つけます。
# dist1_sortedとdist2_sortedをマージしてソートします。
merged_sorted_dists = np.sort(np.concatenate([dist1_sorted, dist2_sorted]))

# 新しいCDFを計算するために、マージされた配列に対応するインデックスを見つけます。
idx1 = np.searchsorted(dist1_sorted, merged_sorted_dists, side='right') / sample_size
idx2 = np.searchsorted(dist2_sorted, merged_sorted_dists, side='right') / sample_size

# y方向の差の最大値とその位置を求めます。
max_diff_y = np.max(np.abs(idx1 - idx2))
max_diff_y_idx = np.argmax(np.abs(idx1 - idx2))

# 最大差に対応する場所に線を引きます。
x_max_diff = merged_sorted_dists[max_diff_y_idx]
y1_max_diff = idx1[max_diff_y_idx]
y2_max_diff = idx2[max_diff_y_idx]

axes[1].plot([x_max_diff, x_max_diff], [y1_max_diff, y2_max_diff], color='gray', linestyle='-', linewidth=2)
axes[1].annotate(f'最大差: {max_diff_y:.3f}',
                 xy=(x_max_diff, (y1_max_diff + y2_max_diff) / 2),
                 xytext=(x_max_diff + 0.5, (y1_max_diff + y2_max_diff) / 2),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=14)

# CDFプロットの設定を行います。
axes[1].set_title(f"コルモゴロフ・スミルノフ統計量: {ks_stat:.3f}, p値: {p_value:.3f}", fontsize=14)
axes[1].legend()
axes[1].set_ylabel('累積分布')

# グラフを表示します。
plt.tight_layout()
plt.savefig('6_2_1_Kolmogorov_Smirnov.png', dpi=300)
plt.savefig('6_2_1_Kolmogorov_Smirnov.svg', dpi=300)

plt.show()
