import numpy as np  # 数値演算のためのNumPy
import seaborn as sns  # グラフ描画のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from scipy.stats import norm, lognorm  # 確率分布のためのSciPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# シード値を固定
np.random.seed(42)

# サンプルサイズ
sample_size = 20

# 図の準備
fig, axes = plt.subplots(
    1, 2, figsize=(10, 5), gridspec_kw={'width_ratios': [1, 1]}
)

# 理論分布と基準線の描画位置のオフセット
offset = 1

# 正規分布からのサンプリング
normal_sample = np.random.normal(size=sample_size)
sns.boxplot(y=normal_sample, ax=axes[0],
            color='white', showfliers=False)  # 外れ値非表示
sns.swarmplot(y=normal_sample, ax=axes[0], color='magenta')
axes[0].scatter([0], [np.mean(normal_sample)], marker='x',
                color='black', s=100, zorder=3)  # 平均値のバツマーク

# 正規分布の理論分布
x_normal = np.linspace(min(normal_sample), max(normal_sample), 100)  # x軸の値
y_normal = norm.pdf(x_normal, 0, 1)  # 正規分布の確率密度関数
axes[0].plot(y_normal * 1 + offset, x_normal, color='magenta')  # オフセットを加える
axes[0].axvline(offset, color='gray', linestyle='-')  # 基準線


# 対数正規分布からのサンプリング
lognormal_sample = np.random.lognormal(size=sample_size)  # 対数正規分布からサンプリング
sns.boxplot(y=lognormal_sample, ax=axes[1],
            color='white', showfliers=False)  # 外れ値非表示
sns.swarmplot(y=lognormal_sample, ax=axes[1], color='cyan')
axes[1].scatter([0], [np.mean(lognormal_sample)], marker='x',
                color='black', s=100, zorder=3)  # 平均値のバツマーク

# 対数正規分布の理論分布
x_lognormal = np.linspace(min(lognormal_sample),
                          max(lognormal_sample), 100)  # x軸の値
y_lognormal = lognorm.pdf(x_lognormal, 1)  # 対数正規分布の確率密度関数
axes[1].plot(y_lognormal * 1 + offset, x_lognormal, color='cyan')  # オフセットを加える
axes[1].axvline(offset, color='gray', linestyle='-')  # 基準線


# 軸ラベルの設定
for ax in axes:
    ax.set_ylabel('観測値')

plt.savefig('5_1_1_sampling_experiment.png', dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
