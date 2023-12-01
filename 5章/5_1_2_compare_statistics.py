import numpy as np  # 数値演算のためのNumPy
import seaborn as sns  # グラフ描画のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import scipy.stats as stats  # 確率分布のためのSciPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# シード値を固定
np.random.seed(42)

# サンプルサイズ
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
                sample = np.random.normal(size=sample_size)  # 正規分布からサンプリング
            else:
                sample = np.random.lognormal(
                    size=sample_size)  # 対数正規分布からサンプリング

            means.append(np.mean(sample))  # 平均値
            medians.append(np.median(sample))  # 中央値
            max_values.append(np.max(sample))  # 最大値
            percentiles_95.append(np.percentile(sample, 95))  # 95パーセンタイル点
            std_devs.append(np.std(sample))  # 標準偏差
            iqr_values.append(np.percentile(sample, 75) -
                              np.percentile(sample, 25))  # 四分位範囲

        # 平均値とメディアンのプロット
        sns.swarmplot(x=[f'N={sample_size}\n平均'] * 100 +
                      [f'N={sample_size}\n中央値'] * 100, y=means + medians, ax=axes[0, idx])

        # 標準偏差とIQRのプロット
        sns.swarmplot(x=[f'N={sample_size}\n標準偏差'] * 100 + [f'N={sample_size}\nIQR']
                      * 100, y=std_devs + iqr_values, ax=axes[1, idx])

        # 最大値と95パーセンタイルのプロット
        sns.swarmplot(x=[f'N={sample_size}\n最大値'] * 100 + [f'N={sample_size}' +
                      '\n95%ile'] * 100, y=max_values + percentiles_95, ax=axes[2, idx])

# タイトルとラベルの設定
for i in range(3):
    axes[i, 0].set_ylabel(
        ['平均値・中央値', '標準偏差・四分位範囲', '最大値・95パーセンタイル点'][i], fontsize=14)
    axes[i, 1].set_ylabel('')

    if i > 0:
        continue


plt.tight_layout()  # レイアウトの調整
plt.savefig('5_1_2_compare_statistics.png', dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
