import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.stats import norm
from scipy.stats import gumbel_r

plt.rcParams['font.size'] = 14
np.random.seed(0)

# この操作を100回繰り返す


def roll_dice(n=100, repeat=100):
    return np.array([np.sum(np.random.randint(1, 7, size=n)) for _ in range(repeat)])


# この操作を1000回サンプリングする
dice_sums = np.array([roll_dice() for _ in range(1000)]).flatten()


# set size of figure
plt.figure(figsize=(5, 4))


# ヒストグラムを作成
plt.hist(dice_sums, bins=range(280, 420), density=True, alpha=0.7, label='Experimental', color="white", edgecolor='gray')

# 正規分布のパラメータを推定
mu, std = norm.fit(dice_sums)
print(mu, std)

# 正規分布を描画
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'r--', linewidth=2, label='Normal Distribution')
plt.xlabel('サイコロを100回振って出た目の総和')
plt.ylabel('相対頻度')
# plt.legend()
plt.tight_layout()
plt.savefig('3_1_3_1_gaussian_fitting.png', dpi=300)
plt.savefig('3_1_3_1_gaussian_fitting.svg', dpi=300)

plt.show()
