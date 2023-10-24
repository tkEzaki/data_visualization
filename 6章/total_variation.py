import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

plt.rcParams['font.size'] = 14
plt.rcParams['font.family'] = 'Yu Gothic'

# 正規分布のパラメータ（平均と標準偏差）
mu1, sigma1 = -1, 1
mu2, sigma2 = 1, 1

# サンプルデータの生成
num_samples = 10000
samples1 = np.random.normal(mu1, sigma1, num_samples)
samples2 = np.random.normal(mu2, sigma2, num_samples)

# ビンの設定
bins = np.linspace(-5, 5, 50)

# ヒストグラムを計算
hist1, bin_edges = np.histogram(samples1, bins=bins, density=True)
hist2, _ = np.histogram(samples2, bins=bins, density=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# 全変動距離（TVD）を計算
tvd_sample = 0.5 * np.sum(np.abs(hist1 - hist2)) * (bin_centers[1] - bin_centers[0])

# サンプルデータに対する全変動距離と面積を表示（ヒストグラムで）
plt.figure(figsize=(8, 5))
plt.hist(samples1, bins=bins, color='gray', alpha=0.3, label='Sample Distribution 1', density=True)
plt.hist(samples2, bins=bins, color='gray', alpha=0.3, label='Sample Distribution 2', density=True)
plt.plot(bin_centers, hist1, 'r-', lw=2, label=f'Sample Distribution 1 (mu={mu1}, sigma={sigma1})')
plt.plot(bin_centers, hist2, 'b-', lw=2, label=f'Sample Distribution 2 (mu={mu2}, sigma={sigma2})')
plt.fill_between(bin_centers, hist1, hist2, where=(hist1 > hist2), interpolate=True, color='red', alpha=0.2, label='TVD Area (dist1 > dist2)')
plt.fill_between(bin_centers, hist1, hist2, where=(hist1 <= hist2), interpolate=True, color='blue', alpha=0.2, label='TVD Area (dist1 <= dist2)')
plt.title(f'全変動距離: {tvd_sample:.4f}')
# plt.xlabel('Value')
plt.ylabel('確率密度')
# plt.legend()

plt.tight_layout()
plt.savefig('total_variation_sample.png', dpi=300)
plt.show()
