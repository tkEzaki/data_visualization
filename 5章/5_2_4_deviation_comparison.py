import numpy as np  # 数値演算のためのNumPy
import seaborn as sns  # グラフ描画のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import pandas as pd  # データフレーム作成のためのPandas
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# シード値を固定
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
                    sample = np.random.normal(size=sample_size)  # 正規分布からサンプリング
                else:
                    sample = np.random.lognormal(
                        size=sample_size)  # 対数正規分布からサンプリング

                if metric == '標準偏差':
                    values.append(np.std(sample))  # 標準偏差を記録
                elif metric == '平均絶対偏差':
                    # 平均絶対偏差を記録
                    values.append(np.mean(np.abs(sample - np.mean(sample))))
                elif metric == '中央絶対偏差':
                    # 中央絶対偏差を記録
                    values.append(np.mean(np.abs(sample - np.median(sample))))

                labels.append(metric)  # 指標の名前を記録
                sample_size_labels.append(
                    f'{metric}\nN={sample_size}')  # サンプルサイズの名前を記録

        # DataFrameを作成してプロット
        data = {
            'Values': values,
            'Metrics': labels,
            'Sample Sizes': sample_size_labels
        }
        data_pd = data_pd.append(pd.DataFrame(data))  # dataを追加

    sns.swarmplot(x='Sample Sizes', y='Values', hue='Metrics',
                  data=data_pd, ax=axes[idx_distribution])  # スウォームプロット

    axes[idx_distribution].set_xticklabels([])  # x軸の目盛ラベルを非表示
    axes[idx_distribution].set_xlabel('')  # x軸のラベルを非表示
    axes[idx_distribution].set_ylabel('')  # y軸のラベルを非表示
    axes[idx_distribution].get_legend().remove()  # 凡例を非表示


plt.savefig('5_3_4_compare_deviation_statistics.png', dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
