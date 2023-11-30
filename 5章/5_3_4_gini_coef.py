import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm
import japanize_matplotlib

plt.rcParams['font.size'] = 12
np.random.seed(42)

# サンプルサイズ
n_samples = 100

# 正規分布からのサンプリング（平均400万、標準偏差20万）
normal_samples = np.random.normal(400, 20, n_samples)

# 平均400万の対数正規分布からのサンプリング
mean_lognormal = 400
sigma_lognormal = 0.5  # 任意の標準偏差
lognormal_samples = lognorm(s=sigma_lognormal, scale=np.exp(np.log(mean_lognormal) - 0.5 * sigma_lognormal**2)).rvs(n_samples)


# ローレンツ曲線とジニ係数の計算
def calculate_lorenz_curve(samples):
    sorted_samples = np.sort(samples)
    cum_frequencies = np.cumsum(sorted_samples) / np.sum(sorted_samples)
    cum_population = np.arange(1, n_samples + 1) / n_samples
    gini = np.mean(cum_population - cum_frequencies) * 2
    return cum_population, cum_frequencies, gini


# 正規分布のローレンツ曲線とジニ係数
cum_population_normal, cum_frequencies_normal, gini_normal = calculate_lorenz_curve(normal_samples)

# 対数正規分布のローレンツ曲線とジニ係数
cum_population_lognormal, cum_frequencies_lognormal, gini_lognormal = calculate_lorenz_curve(lognormal_samples)


plt.figure(figsize=(8, 6))
plt.subplot(2, 2, 1)
plt.hist(normal_samples, bins=20, color='skyblue', edgecolor='k')
plt.title('年収分布その１')
plt.xlabel('年収（万円）')
plt.ylabel('頻度')
plt.subplot(2, 2, 2)
plt.hist(lognormal_samples, bins=20, color='salmon', edgecolor='k')
plt.title('年収分布その２')
plt.xlabel('年収（万円）')
plt.subplot(2, 2, 3)
plt.plot(cum_population_normal, cum_frequencies_normal, label='ローレンツ曲線')
plt.fill_between(cum_population_normal, cum_frequencies_normal, cum_population_normal, color='skyblue', alpha=0.5)  # 領域の塗りつぶし
plt.plot([0, 1], [0, 1], linestyle='--', label='全員同じ年収の場合')
plt.plot([0, 1, 1], [0, 0, 1], linestyle=':', label='一人が独占の場合')
plt.title(f'ジニ係数: {gini_normal:.3f}')
plt.xlabel('累積人数の割合')
plt.ylabel('累積年収の割合')
plt.legend(frameon=False, facecolor='none')

plt.subplot(2, 2, 4)
plt.plot(cum_population_lognormal, cum_frequencies_lognormal, label='ローレンツ曲線')
plt.fill_between(cum_population_lognormal, cum_frequencies_lognormal, cum_population_lognormal, color='skyblue', alpha=0.5)  # 領域の塗りつぶし
plt.plot([0, 1], [0, 1], linestyle='--', label='全員同じ年収の場合')
plt.plot([0, 1, 1], [0, 0, 1], linestyle=':', label='一人が独占の場合')
plt.title(f'ジニ係数: {gini_lognormal:.3f}')
plt.xlabel('累積人数の割合')
plt.legend(frameon=False, facecolor='none')

plt.tight_layout()
plt.savefig('5_3_4_gini_coef.png', dpi=300)
plt.savefig('5_3_4_gini_coef.svg', dpi=300)

plt.show()
