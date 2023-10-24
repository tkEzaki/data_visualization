import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import multivariate_normal

plt.rcParams['font.family'] = 'Yu Gothic'
plt.rcParams['font.size'] = 12
# 正規分布からランダムに30点からなるサンプルを二つ生成し、その相関係数を計算する関数


def generate_correlation(target_corr=0.8):
    mean = [0, 0]
    cov = [[1, target_corr], [target_corr, 1]]  # 共分散行列
    samples = multivariate_normal.rvs(mean, cov, size=100)
    sample1 = samples[:, 0]
    sample2 = samples[:, 1]
    correlation = np.corrcoef(sample1, sample2)[0, 1]
    return correlation


# 相関係数とフィッシャーのz変換した値を保存するリスト
correlations = []
fisher_z = []

# 1000回繰り返し
for _ in range(100000):
    correlation = generate_correlation()
    correlations.append(correlation)
    fisher_z.append(0.5 * np.log((1 + correlation) / (1 - correlation)))

# 共通のビンを設定（-1から+1を40分割）
bins_orig = np.linspace(0.6, 1.0, 41)
bins_z = np.linspace(0.6, 1.5, 41)

# ヒストグラムを描画
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# 相関係数のヒストグラム
axes[0].hist(correlations, bins=bins_orig, density=True, alpha=0.6, color='b', label='Observed Data')
xmin, xmax = axes[0].get_xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, np.mean(correlations), np.std(correlations))
axes[0].plot(x, p, 'darkblue', linestyle="--", linewidth=1, label='Fitted Normal')
axes[0].set_title('サンプリングされた相関係数')
axes[0].set_xlabel('$r$')
# axes[0].legend(loc='upper left')

# フィッシャーのz変換した値のヒストグラム
axes[1].hist(fisher_z, bins=bins_z, density=True, alpha=0.6, color='r', label='Observed Data')
xmin, xmax = axes[1].get_xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, np.mean(fisher_z), np.std(fisher_z))
axes[1].plot(x, p, 'darkred', linestyle="--", linewidth=1, label='Fitted Normal')
axes[1].set_title('フィッシャー変換後の相関係数')
axes[1].set_xlabel('$z$')
# axes[1].legend(loc='upper left')

plt.savefig('correlation_exp.png')
plt.show()
