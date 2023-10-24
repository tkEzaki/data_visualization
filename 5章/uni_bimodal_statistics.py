import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Yu Gothic'
plt.rcParams['font.size'] = 12

# 乱数のシード設定
np.random.seed(42)

# 単峰性の分布
single_peak_distribution = np.random.normal(loc=0, scale=1, size=1000)

# 二峰性の分布
bimodal_distribution = np.concatenate([
    np.random.normal(loc=-1, scale=0.2, size=500),
    np.random.normal(loc=1, scale=0.2, size=500)
])
# 単峰性の分布の平均値と標準偏差
single_peak_mean = np.mean(single_peak_distribution)
single_peak_std = np.std(single_peak_distribution)

# 二峰性の分布の平均値と標準偏差
bimodal_mean = np.mean(bimodal_distribution)
bimodal_std = np.std(bimodal_distribution)

# サブプロットの設定
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# 単峰性の分布のヒストグラム
axs[0].hist(single_peak_distribution, bins=20, color='gold', alpha=0.7)
axs[0].set_title(f'単峰性の分布 (平均={single_peak_mean:.2f}, 標準偏差={single_peak_std:.2f})')
axs[0].set_ylabel('頻度')

# 二峰性の分布のヒストグラム
axs[1].hist(bimodal_distribution, bins=20, color='blue', alpha=0.5)
axs[1].set_title(f'二峰性の分布 (平均={bimodal_mean:.2f}, 標準偏差={bimodal_std:.2f})')
axs[1].set_ylabel('頻度')

plt.tight_layout()
plt.savefig('uni_bimodal_statistics.png')
plt.show()
