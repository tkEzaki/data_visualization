import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skewnorm, laplace, skew, kurtosis

plt.rcParams['font.family'] = 'Yu Gothic'
np.random.seed(42)

# 正規分布（歪度=0, 尖度=3）
mu, sigma = 0, 1
normal_dist = norm.rvs(loc=mu, scale=sigma, size=1000)

# 歪度がある分布（歪度>0, 尖度異なる）
a = 4
skewed_scale = 2
skewed_mu = 0
skewed_dist = skewnorm.rvs(a, loc=skewed_mu, scale=skewed_scale, size=1000)

# ラプラス分布（歪度=0, 尖度>3）
b = 1
laplace_dist = laplace.rvs(loc=mu, scale=b, size=1000)

# 上段のプロット（ヒストグラム）
fig, axes = plt.subplots(1, 3, figsize=(10, 4))
axes[0].hist(normal_dist, bins=30, density=True, alpha=0.6, color='blue')
axes[0].set_title('分布１（正規分布）')
axes[1].hist(skewed_dist, bins=30, density=True, alpha=0.6, color='green')
axes[1].set_title('分布２（歪正規分布）')
axes[2].hist(laplace_dist, bins=30, density=True, alpha=0.6, color='red')
axes[2].set_title('分布３（ラプラス分布）')
plt.tight_layout()
plt.savefig('histograms.png', dpi=300)
plt.show()
plt.close()  # プロットのクリア

# 統計量の計算
median_skews, skews, kurtoses, quartile_skews = [], [], [], []
for dist in [normal_dist, skewed_dist, laplace_dist]:
    median_skews.append((np.mean(dist)-np.median(dist)) / np.std(dist))
    kurtoses.append(kurtosis(dist) + 3)
    skews.append(skew(dist))
    q3, q1 = np.percentile(dist, [75, 25])
    quartile_skews.append((q3 + q1 - 2 * np.median(dist)) / (q3 - q1))

colors = ['blue', 'green', 'red']

# 下段のプロット（棒グラフ）
fig, axes = plt.subplots(1, 4, figsize=(10, 4))
axes[0].bar(['分布１', '分布２', '分布３'], skews, color=colors, alpha=0.6)
axes[0].set_title('歪度')
axes[1].bar(['分布１', '分布２', '分布３'], median_skews, color=colors, alpha=0.6)
axes[1].set_title('中央値歪度')
axes[2].bar(['分布１', '分布２', '分布３'], quartile_skews, color=colors, alpha=0.6)
axes[2].set_title('四分位歪度')
axes[3].bar(['分布１', '分布２', '分布３'], kurtoses, color=colors, alpha=0.6)
axes[3].set_title('尖度')
plt.tight_layout()
plt.savefig('bar_charts.png', dpi=300)  # 画像の保存
plt.show()
