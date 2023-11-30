import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# シード値を固定
np.random.seed(42)

# サンプリング数
sample_sizes = [20, 100, 500]

# 図の準備
fig, axes = plt.subplots(3, 2, figsize=(10, 10))

# 正規分布と対数正規分布をループ
for idx, distribution in enumerate(['normal', 'lognormal']):
    # サンプリング数ごとのループ
    for sample_size in sample_sizes:
        means = []
        medians = []
        max_values = []
        percentiles_95 = []
        std_devs = []
        iqr_values = []

        # 100回のサンプリング
        for _ in range(100):
            if distribution == 'normal':
                sample = np.random.normal(size=sample_size)
            else:
                sample = np.random.lognormal(size=sample_size)

            means.append(np.mean(sample))
            medians.append(np.median(sample))
            max_values.append(np.max(sample))
            percentiles_95.append(np.percentile(sample, 95))
            std_devs.append(np.std(sample))
            iqr_values.append(np.percentile(sample, 75) - np.percentile(sample, 25))

        # 平均値とメディアンのプロット
        sns.swarmplot(x=[f'N={sample_size}\n平均'] * 100 + [f'N={sample_size}\n中央値'] * 100, y=means + medians, ax=axes[0, idx])

        # 標準偏差とIQRのプロット
        sns.swarmplot(x=[f'N={sample_size}\n標準偏差'] * 100 + [f'N={sample_size}\nIQR'] * 100, y=std_devs + iqr_values, ax=axes[1, idx])

        # 最大値と95パーセンタイルのプロット
        sns.swarmplot(x=[f'N={sample_size}\n最大値'] * 100 + [f'N={sample_size}'+'\n95%ile'] * 100, y=max_values + percentiles_95, ax=axes[2, idx])

# タイトルとラベルの設定
for i in range(3):
    axes[i, 0].set_ylabel(['平均値・中央値', '標準偏差・四分位範囲', '最大値・95パーセンタイル点'][i], fontsize=14)
    axes[i, 1].set_ylabel('')

    if i > 0:
        continue

    # axes[i, 0].set_title('正規分布')
    # axes[i, 1].set_title('対数正規分布')

plt.tight_layout()
plt.savefig('5_1_2_compare_statistics.png', dpi=300)
plt.savefig('5_1_2_compare_statistics.svg', dpi=300)


plt.show()
