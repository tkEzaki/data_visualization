import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ
from scipy.stats import norm  # 正規分布のためのSciPy

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定

np.random.seed(2)  # 乱数のシードを設定（再現性のため）

# 正規分布から100点をサンプル
mu, sigma = 0, 1  # mean and standard deviation
s = np.random.normal(mu, sigma, 100)  # 平均0、標準偏差1の正規分布に従う乱数を100個生成

# ビンのサイズ
bins_sizes = [5, 10, 50]

# 正規分布のプロット用のデータ
x = np.linspace(-4, 4, 200)
y = norm.pdf(x, mu, sigma)

# サブプロットとしてヒストグラムを生成
fig, axs = plt.subplots(1, 3, figsize=(8, 3))
for i, bins in enumerate(bins_sizes):
    axs[i].hist(s, bins=bins, density=True, alpha=0.6, color='b')  # ヒストグラムを描画
    axs[i].plot(x, y, 'r--')  # 正規分布を描画
    axs[i].set_title(f'ビン幅 = {4/bins}', fontsize=14)  # タイトル

axs[0].set_ylabel('相対頻度')  # y軸ラベル
axs[1].set_xlabel('観測値')  # x軸ラベル

plt.tight_layout()  # レイアウトの設定
plt.savefig('3_1_2_1_bin_size.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示


np.random.seed(2)  # 乱数のシードを設定（再現性のため）
# 正規分布から100点をサンプル
s = np.random.normal(mu, sigma, 50)  # 平均0、標準偏差1の正規分布に従う乱数を50個生成

# ビンのサイズとオフセット
bins_sizes = [20, 20, 20]
offsets = [0, 0.1, 0.2]

# 正規分布のプロット用のデータ
x = np.linspace(-4, 4, 200)  # x軸の値
y = norm.pdf(x, mu, sigma)  # 正規分布の値

# サブプロットとしてヒストグラムを生成
fig, axs = plt.subplots(1, 3, figsize=(8, 3))

for i, (bins, offset) in enumerate(zip(bins_sizes, offsets)):
    bins_list = np.linspace(-4 + offset, 4 + offset, bins + 1)  # ビンの範囲をずらす
    axs[i].hist(s, bins=bins_list, density=True,
                alpha=0.6, color='b')  # ヒストグラムを描画
    axs[i].plot(x, y, 'r--')  # 正規分布を描画
    axs[i].set_ylim([0, 0.6])  # y軸の範囲を設定
    axs[i].set_title(f'オフセット = {offset}', fontsize=14)  # タイトル

axs[0].set_ylabel('相対頻度')  # y軸ラベル
axs[1].set_xlabel('観測値')  # x軸ラベル

plt.tight_layout()  # レイアウトの設定
plt.savefig('3_1_2_2_bin_offset.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示
