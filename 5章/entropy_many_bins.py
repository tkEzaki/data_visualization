import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

plt.rcParams['font.family'] = 'Yu Gothic'
np.random.seed(42)
# サンプル数
n_samples = 50

# ビンの設定
bins = np.linspace(-5, 5, 400)

# 一様分布からのサンプリング
uniform_samples = np.random.uniform(-5, 5, n_samples)
uniform_hist, _ = np.histogram(uniform_samples, bins=bins)
uniform_entropy = entropy(uniform_hist)

# 正規分布からのサンプリング
normal_samples = np.random.normal(0, 1, n_samples)
normal_hist, _ = np.histogram(normal_samples, bins=bins)
normal_entropy = entropy(normal_hist)

# 2つの正規分布からサンプリング
gmm_samples1 = np.random.normal(-2, 0.25, n_samples // 2)
gmm_samples2 = np.random.normal(2, 0.25, n_samples // 2)
gmm_samples = np.concatenate([gmm_samples1, gmm_samples2])
gmm_hist, _ = np.histogram(gmm_samples, bins=bins)
gmm_entropy = entropy(gmm_hist)

# ヒストグラムの描画
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.hist(uniform_samples, bins=bins, color='skyblue', edgecolor='skyblue')
plt.title(f'一様分布\nエントロピー: {uniform_entropy:.2f}')
plt.ylabel('頻度')

plt.subplot(1, 3, 2)
plt.hist(normal_samples, bins=bins, color='salmon', edgecolor='salmon')
plt.title(f'正規分布\nエントロピー: {normal_entropy:.2f}')

plt.subplot(1, 3, 3)
plt.hist(gmm_samples, bins=bins, color='lightgreen', edgecolor='lightgreen')
plt.title(f'2つの正規分布の混合\nエントロピー: {gmm_entropy:.2f}')


plt.tight_layout()
plt.savefig('entropy_many_bins.png', dpi=300)
plt.show()
