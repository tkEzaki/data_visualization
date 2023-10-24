import numpy as np
from scipy.stats import lognorm, norm
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# 対数正規分布のパラメータ
lognorm_params = (0.954, 0, np.exp(0.65))

# サンプルを生成
np.random.seed(0)
lognorm_samples = lognorm.rvs(*lognorm_params, size=10000)

# 対数変換
log_lognorm_samples = np.log(lognorm_samples)

# データを正規分布でフィット
lognorm_mu, lognorm_std = norm.fit(log_lognorm_samples)

# ヒストグラムとフィット結果をプロット
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# 対数正規分布
axs[0].hist(lognorm_samples, bins=30, alpha=0.5, color='blue', edgecolor='black', density=True)
# axs[0].set_title('Log-normal distribution')
axs[0].set_xlabel('観測値 $X$')
axs[0].set_ylabel('相対頻度')

# 対数変換後の対数正規分布
axs[1].hist(log_lognorm_samples, bins=30, alpha=0.5, color='blue', edgecolor='black', density=True)
x = np.linspace(log_lognorm_samples.min(), log_lognorm_samples.max(), 1000)
axs[1].plot(x, norm.pdf(x, lognorm_mu, lognorm_std), 'r--', lw=2)
axs[1].set_xlabel('log $X$')
# axs[1].set_title('Log-transformed Log-normal distribution')


plt.tight_layout()
plt.subplots_adjust(wspace=0.3, hspace=0.4)
plt.savefig('3_1_3_3_log_transform.png', dpi=300)
plt.savefig('3_1_3_3_log_transform.svg', dpi=300)

plt.show()
