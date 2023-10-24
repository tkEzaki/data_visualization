import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.stats import norm

plt.rcParams['font.size'] = 14

np.random.seed(2)
# 正規分布から100点をサンプル
mu, sigma = 0, 1  # mean and standard deviation
s = np.random.normal(mu, sigma, 100)

# ビンのサイズ
bins_sizes = [5, 10, 50]

# 正規分布のプロット用のデータ
x = np.linspace(-4, 4, 200)
y = norm.pdf(x, mu, sigma)

# サブプロットとしてヒストグラムを生成
fig, axs = plt.subplots(1, 3, figsize=(8, 3))
for i, bins in enumerate(bins_sizes):
    axs[i].hist(s, bins=bins, density=True, alpha=0.6, color='b')
    axs[i].plot(x, y, 'r--')
    axs[i].set_title(f'ビン幅 = {4/bins}', fontsize=14)

axs[0].set_ylabel('相対頻度')
axs[1].set_xlabel('観測値')

# プロットを表示
plt.tight_layout()
plt.savefig('3_1_2_1_bin_size.png', dpi=300)
plt.savefig('3_1_2_1_bin_size.svg', dpi=300)



np.random.seed(2)
# 正規分布から100点をサンプル
s = np.random.normal(mu, sigma, 50)

# ビンのサイズとオフセット
bins_sizes = [20, 20, 20]
offsets = [0, 0.1, 0.2]

# 正規分布のプロット用のデータ
x = np.linspace(-4, 4, 200)
y = norm.pdf(x, mu, sigma)

# サブプロットとしてヒストグラムを生成
fig, axs = plt.subplots(1, 3, figsize=(8, 3))

for i, (bins, offset) in enumerate(zip(bins_sizes, offsets)):
    bins_list = np.linspace(-4 + offset, 4 + offset, bins + 1)  # ビンの範囲をずらす
    axs[i].hist(s, bins=bins_list, density=True, alpha=0.6, color='b')
    axs[i].plot(x, y, 'r--')
    axs[i].set_ylim([0, 0.6])
    axs[i].set_title(f'オフセット = {offset}', fontsize=14)

axs[0].set_ylabel('相対頻度')
axs[1].set_xlabel('観測値')

# プロットを表示
plt.tight_layout()
plt.savefig('3_1_2_2_bin_offset.png', dpi=300)
plt.savefig('3_1_2_2_bin_offset.svg')

plt.show()
