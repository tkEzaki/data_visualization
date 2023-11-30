
import numpy as np  # 数値計算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ
from scipy.stats import norm  # 正規分布のためのSciPy

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定

np.random.seed(1)  # 乱数のシードを設定（再現性のため）
# 正規分布のパラメータ
mu, sigma = 0, 1  # 平均と標準偏差

# 正規分布から100点と500点をサンプル
sample_sizes = [100, 500]  # サンプルサイズ
samples = [np.random.normal(mu, sigma, size)
           for size in sample_sizes]  # サンプルを生成

# 正規分布の累積分布関数のプロット用のデータ
x = np.linspace(-3, 3, 100)  # x軸の値
y = norm.cdf(x, mu, sigma)  # 正規分布の累積分布関数の値

# サブプロットを2x2で生成
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# 1つ目のサブプロットで80パーセンタイル点以下の領域を別の色で示すヒストグラムを表示
percentile_80 = np.percentile(samples[0], 80)  # 80パーセンタイル点
bins = np.linspace(-3, 3, 30)  # ビンの設定
axs[0, 0].hist(samples[0], bins=bins, color='blue',
               alpha=0.3, label='Whole data')  # ヒストグラムを描画
axs[0, 0].hist(samples[0][samples[0] <= percentile_80], bins=bins,
               color='blue', alpha=1, label='Below 80 percentile')  # ヒストグラムを描画
axs[0, 0].set_ylabel('頻度')  # y軸ラベル
axs[0, 0].set_xlabel('観測値')  # x軸ラベル
axs[0, 0].set_xlim([-3, 3])  # x軸の範囲を設定


# 二枚目は空白にする
axs[0, 1].axis('off')  # グラフを表示しない


# 下段の累積分布を描画
titles = ["サンプルサイズ=100", "サンプルサイズ=500"]  # グラフのタイトル
for i, sample in enumerate(samples):
    sample_sorted = np.sort(sample)  # 観測値をソート
    p = 1. * np.arange(len(sample)) / (len(sample) - 1)  # 累積相対頻度を計算
    axs[1, i].step(sample_sorted, p, label="Empirical CDF")  # 累積相対頻度を描画
    axs[1, i].plot(x, y, 'r--', label="Theoretical CDF")  # 理論的な累積分布関数を描画
    axs[1, i].set_xlim([-3, 3])  # x軸の範囲を設定
    axs[1, i].set_ylabel('累積相対頻度')  # y軸ラベル
    axs[1, i].set_xlabel('観測値')  # x軸ラベル
    axs[1, i].set_title(titles[i], fontsize=14)  # グラフのタイトル


# プロットを表示
plt.tight_layout()  # レイアウトの設定
plt.savefig('3_1_5_cumulative_dist.png', dpi=300)  # 画像として保存
plt.show()
