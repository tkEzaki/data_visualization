import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from scipy.stats import norm, skewnorm, laplace, skew, kurtosis  # 確率分布のためのSciPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# 乱数のシード設定
np.random.seed(42)

# 正規分布（歪度=0, 尖度=3）
mu, sigma = 0, 1
normal_dist = norm.rvs(loc=mu, scale=sigma, size=1000)  # 正規分布からサンプリング

# 歪度がある分布（歪度>0, 尖度異なる）
a = 4
skewed_scale = 2
skewed_mu = 0
skewed_dist = skewnorm.rvs(
    a, loc=skewed_mu, scale=skewed_scale, size=1000)  # 歪度がある分布からサンプリング

# ラプラス分布（歪度=0, 尖度>3）
b = 1
laplace_dist = laplace.rvs(loc=mu, scale=b, size=1000)  # ラプラス分布からサンプリング

# 上段のプロット（ヒストグラム）
fig, axes = plt.subplots(1, 3, figsize=(10, 4))  # 図の準備
axes[0].hist(normal_dist, bins=30, density=True,
             alpha=0.6, color='blue')  # ヒストグラム描画
axes[0].set_title('分布１（正規分布）')
axes[1].hist(skewed_dist, bins=30, density=True,
             alpha=0.6, color='green')  # ヒストグラム描画
axes[1].set_title('分布２（歪正規分布）')
axes[2].hist(laplace_dist, bins=30, density=True,
             alpha=0.6, color='red')  # ヒストグラム描画
axes[2].set_title('分布３（ラプラス分布）')

plt.tight_layout()  # レイアウトの調整
plt.savefig('5_3_1_1_distorted_dist_histograms.png', dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
plt.close()  # プロットをクリアして次の図を描画していく


# 統計量の計算
median_skews, skews, kurtoses, quartile_skews = [], [], [], []
for dist in [normal_dist, skewed_dist, laplace_dist]:
    median_skews.append(
        (np.mean(dist) - np.median(dist)) / np.std(dist))  # 中央値歪度
    kurtoses.append(kurtosis(dist) + 3)  # 尖度
    skews.append(skew(dist))  # 歪度
    q3, q1 = np.percentile(dist, [75, 25])  # 第3四分位点と第1四分位点
    quartile_skews.append((q3 + q1 - 2 * np.median(dist)) / (q3 - q1))  # 四分位歪度

# グラフの設定
colors = ['blue', 'green', 'red']  # プロットの色

# 下段のプロット（棒グラフ）
fig, axes = plt.subplots(1, 4, figsize=(10, 4))  # 図の準備

for ax in axes:
    ax.set_xticklabels(['分布１', '分布２', '分布３'], rotation=45,
                       ha='right')  # x軸のラベル指定

axes[0].bar(['分布１', '分布２', '分布３'], skews, color=colors, alpha=0.6)  # 棒グラフ描画
axes[0].set_title('歪度')  # タイトル
axes[1].bar(['分布１', '分布２', '分布３'], median_skews,
            color=colors, alpha=0.6)  # 棒グラフ描画
axes[1].set_title('中央値歪度')  # タイトル
axes[2].bar(['分布１', '分布２', '分布３'], quartile_skews,
            color=colors, alpha=0.6)  # 棒グラフ描画
axes[2].set_title('四分位歪度')  # タイトル
axes[3].bar(['分布１', '分布２', '分布３'], kurtoses, color=colors, alpha=0.6)  # 棒グラフ描画
axes[3].set_title('尖度')  # タイトル

plt.tight_layout()  # レイアウトの調整
plt.savefig('5_3_1_2_dist_metric_bar_charts.png', dpi=300)  # 画像の保存
plt.show()  # 画像を画面に表示
