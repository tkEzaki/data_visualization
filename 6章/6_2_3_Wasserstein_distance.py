import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib

np.random.seed(42)
plt.rcParams['font.size'] = 14

# 正規分布のパラメータ（平均と標準偏差）
mu1, sigma1 = 0, 1
mu2, sigma2 = 2, 1

# サンプルデータの生成
num_samples = 10000
samples1 = np.random.normal(mu1, sigma1, num_samples)
samples2 = np.random.normal(mu2, sigma2, num_samples)

# サンプルデータのサブセットをランダムに選ぶ（非復元抽出）
num_subset = 50
np.random.seed(0)  # 再現性のためのランダムシード
subset_idx1 = np.random.choice(samples1.shape[0], num_subset, replace=True)
subset_idx2 = np.random.choice(samples2.shape[0], num_subset, replace=True)

subset_samples1 = samples1[subset_idx1]
subset_samples2 = samples2[subset_idx2]

# ソート
subset_samples1.sort()
subset_samples2.sort()

# 可視化
plt.figure(figsize=(8, 4))
plt.scatter(subset_samples1, np.ones(num_subset), color='red', label='分布１', zorder=2)
plt.scatter(subset_samples2, np.zeros(num_subset), color='blue', label='分布２', zorder=2)

# 最短距離の接続線を描画
for x1, x2 in zip(subset_samples1, subset_samples2):
    plt.plot([x1, x2], [1, 0], '-', color='gray', linewidth=1, zorder=1)

# plt.title('Wasserstein Distance Visualization')
plt.yticks([0, 1], ['分布２', '分布１'])
# plt.xlabel('Value')
# plt.legend()
# plt.grid(True)

plt.tight_layout()
plt.savefig('6_2_3_wasserstein_distance.png', dpi=300)
plt.savefig('6_2_3_wasserstein_distance.svg', dpi=300)

plt.show()
