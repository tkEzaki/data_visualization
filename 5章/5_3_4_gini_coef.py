import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from scipy.stats import lognorm  # 対数正規分布のためのSciPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 12  # フォントサイズを設定

# シード値を固定
np.random.seed(42)

# サンプルサイズ
n_samples = 100

# 正規分布からのサンプリング（平均400万、標準偏差20万）
normal_samples = np.random.normal(400, 20, n_samples)

# 平均400万の対数正規分布からのサンプリング
mean_lognormal = 400
sigma_lognormal = 0.5  # 任意の標準偏差
lognormal_samples = lognorm(s=sigma_lognormal, scale=np.exp(
    np.log(mean_lognormal) - 0.5 * sigma_lognormal**2)).rvs(n_samples)


# ローレンツ曲線とジニ係数の計算を行う関数
def calculate_lorenz_curve(samples):
    sorted_samples = np.sort(samples)  # サンプルを昇順に並び替える
    cum_frequencies = np.cumsum(sorted_samples) / \
        np.sum(sorted_samples)  # 累積相対度数
    cum_population = np.arange(1, n_samples + 1) / n_samples  # 累積人口の割合
    gini = np.mean(cum_population - cum_frequencies) * 2  # ジニ係数
    return cum_population, cum_frequencies, gini


# 正規分布のローレンツ曲線とジニ係数
cum_population_normal, cum_frequencies_normal, gini_normal = calculate_lorenz_curve(
    normal_samples)

# 対数正規分布のローレンツ曲線とジニ係数
cum_population_lognormal, cum_frequencies_lognormal, gini_lognormal = calculate_lorenz_curve(
    lognormal_samples)


# 図の描画
plt.figure(figsize=(8, 6))  # 図の準備
plt.subplot(2, 2, 1)  # 2行2列の左上を指定
plt.hist(normal_samples, bins=20, color='skyblue', edgecolor='k')  # ヒストグラム描画
plt.title('年収分布その１')  # タイトル
plt.xlabel('年収（万円）')  # x軸ラベル
plt.ylabel('頻度')  # y軸ラベル
plt.subplot(2, 2, 2)  # 2行2列の右上を指定
plt.hist(lognormal_samples, bins=20, color='salmon', edgecolor='k')  # ヒストグラム描画
plt.title('年収分布その２')  # タイトル
plt.xlabel('年収（万円）')  # x軸ラベル

plt.subplot(2, 2, 3)  # 2行2列の左下を指定
plt.plot(cum_population_normal, cum_frequencies_normal,
         label='ローレンツ曲線')  # ローレンツ曲線の描画
plt.fill_between(cum_population_normal, cum_frequencies_normal,
                 cum_population_normal, color='skyblue', alpha=0.5)  # 領域の塗りつぶし
plt.plot([0, 1], [0, 1], linestyle='--', label='全員同じ年収の場合')  # 基準線の描画
plt.plot([0, 1, 1], [0, 0, 1], linestyle=':', label='一人が独占の場合')  # 基準線の描画
plt.title(f'ジニ係数: {gini_normal:.3f}')  # タイトル
plt.xlabel('累積人数の割合')  # x軸ラベル
plt.ylabel('累積年収の割合')  # y軸ラベル
plt.legend(frameon=False, facecolor='none')  # 凡例の表示

plt.subplot(2, 2, 4)  # 2行2列の右下を指定
plt.plot(cum_population_lognormal, cum_frequencies_lognormal,
         label='ローレンツ曲線')  # ローレンツ曲線の描画
plt.fill_between(cum_population_lognormal, cum_frequencies_lognormal,
                 cum_population_lognormal, color='skyblue', alpha=0.5)  # 領域の塗りつぶし
plt.plot([0, 1], [0, 1], linestyle='--', label='全員同じ年収の場合')  # 基準線の描画
plt.plot([0, 1, 1], [0, 0, 1], linestyle=':', label='一人が独占の場合')  # 基準線の描画
plt.title(f'ジニ係数: {gini_lognormal:.3f}')  # タイトル
plt.xlabel('累積人数の割合')  # x軸ラベル
plt.legend(frameon=False, facecolor='none')   # 凡例の表示

plt.tight_layout()  # レイアウトの調整
plt.savefig('5_3_4_gini_coef.png', dpi=300)  # 画像を保存
plt.show()  # 画面に表示
