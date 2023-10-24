
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.stats import norm

plt.rcParams['font.size'] = 14

np.random.seed(1)
# 正規分布のパラメータ
mu, sigma = 0, 1

# 正規分布から100点と500点をサンプル
sample_sizes = [100, 500]
samples = [np.random.normal(mu, sigma, size) for size in sample_sizes]

# 正規分布の累積分布関数のプロット用のデータ
x = np.linspace(-3, 3, 100)
y = norm.cdf(x, mu, sigma)

# サブプロットを2x2で生成
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# 1つ目のサブプロットで80パーセンタイル点以下の領域を別の色で示すヒストグラムを表示
percentile_80 = np.percentile(samples[0], 80)
bins = np.linspace(-3, 3, 30)
axs[0, 0].hist(samples[0], bins=bins, color='blue', alpha=0.3, label='Whole data')
axs[0, 0].hist(samples[0][samples[0] <= percentile_80], bins=bins, color='blue', alpha=1, label='Below 80 percentile')
axs[0, 0].set_ylabel('頻度')
axs[0, 0].set_xlabel('観測値')
axs[0, 0].set_xlim([-3, 3])

# 二枚目は空白にする
axs[0, 1].axis('off')

# 下段の累積分布を描画
titles = ["サンプルサイズ=100", "サンプルサイズ=500"]
for i, sample in enumerate(samples):
    sample_sorted = np.sort(sample)
    p = 1. * np.arange(len(sample)) / (len(sample) - 1)  # calculate empirical CDF
    axs[1, i].step(sample_sorted, p, label="Empirical CDF")
    axs[1, i].plot(x, y, 'r--', label="Theoretical CDF")
    axs[1, i].set_xlim([-3, 3])
    axs[1, i].set_ylabel('累積相対頻度')
    axs[1, i].set_xlabel('観測値')
    axs[1, i].set_title(titles[i], fontsize=14)

# プロットを表示
plt.tight_layout()
plt.savefig('3_1_5_cumulative_dist.png', dpi=300)
plt.savefig('3_1_5_cumulative_dist.svg')

plt.show()
