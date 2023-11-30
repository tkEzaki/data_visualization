import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib

plt.rcParams['font.size'] = 14
np.random.seed(42)

# サンプルサイズ
sample_sizes = [20, 100, 500]

# 指標
metrics = ['標準偏差', '平均絶対偏差', '中央絶対偏差']

# 図の準備
fig, axes = plt.subplots(2, 1, figsize=(8, 8))

# 正規分布と対数正規分布をループ
for idx_distribution, distribution in enumerate(['normal', 'lognormal']):
    data_pd = pd.DataFrame()
    # 指標ごとのループ
    for idx_metric, metric in enumerate(metrics):
        values = []
        labels = []
        sample_size_labels = []

        # サンプルサイズごとのループ
        for sample_size in sample_sizes:
            for _ in range(100):
                if distribution == 'normal':
                    sample = np.random.normal(size=sample_size)
                else:
                    sample = np.random.lognormal(size=sample_size)

                if metric == '標準偏差':
                    values.append(np.std(sample))
                elif metric == '平均絶対偏差':
                    values.append(np.mean(np.abs(sample - np.mean(sample))))
                elif metric == '中央絶対偏差':
                    values.append(np.mean(np.abs(sample - np.median(sample))))

                labels.append(metric)
                sample_size_labels.append(f'{metric}\nN={sample_size}')

        # DataFrameを作成してプロット
        data = {
            'Values': values,
            'Metrics': labels,
            'Sample Sizes': sample_size_labels
        }
        data_pd = data_pd.append(pd.DataFrame(data))

    sns.swarmplot(x='Sample Sizes', y='Values', hue='Metrics', data=data_pd, ax=axes[idx_distribution])

    # # タイトルの設定
    # if idx_distribution == 0:
    #     axes[idx_distribution].set_title('正規分布')
    # else:
    #     axes[idx_distribution].set_title('対数正規分布')

    axes[idx_distribution].set_xticklabels([])  # x軸の目盛ラベルを非表示
    axes[idx_distribution].set_xlabel('')
    axes[idx_distribution].set_ylabel('')
    axes[idx_distribution].get_legend().remove()  # 凡例を非表示


# plt.tight_layout()
plt.savefig('5_3_4_compare_deviation_statistics.png', dpi=300)
plt.savefig('5_3_4_compare_deviation_statistics.svg', dpi=300)

plt.show()
