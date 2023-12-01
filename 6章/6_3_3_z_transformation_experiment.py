import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from scipy.stats import norm  # 正規分布のためのSciPy
from scipy.stats import multivariate_normal  # 多変量正規分布のためのSciPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# 正規分布からランダムに30点からなるサンプルを二つ生成して相関係数を計算する関数
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
    correlation = generate_correlation()  # 相関係数を計算
    correlations.append(correlation)  # 相関係数を保存
    fisher_z.append(0.5 * np.log((1 + correlation) /
                    (1 - correlation)))  # フィッシャーのz変換した値を保存

# 共通のビンを設定（-1から+1を40分割）
bins_orig = np.linspace(0.6, 1.0, 41)
bins_z = np.linspace(0.6, 1.5, 41)

# ヒストグラムを描画
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# 相関係数のヒストグラム
axes[0].hist(correlations, bins=bins_orig, density=True, alpha=0.6,
             color='b', label='Observed Data')  # ヒストグラムを描画
xmin, xmax = axes[0].get_xlim()  # x軸の範囲を取得
x = np.linspace(xmin, xmax, 100)  # x軸の範囲を100分割した配列を生成
p = norm.pdf(x, np.mean(correlations), np.std(correlations))  # 正規分布の確率密度関数を計算
axes[0].plot(x, p, 'darkblue', linestyle="--",
             linewidth=1, label='Fitted Normal')  # 正規分布を描画
axes[0].set_title('サンプリングされた相関係数')  # タイトルを設定
axes[0].set_xlabel('$r$')  # x軸ラベルを設定

# フィッシャーのz変換した値のヒストグラム
axes[1].hist(fisher_z, bins=bins_z, density=True, alpha=0.6,
             color='r', label='Observed Data')  # ヒストグラムを描画
xmin, xmax = axes[1].get_xlim()  # x軸の範囲を取得
x = np.linspace(xmin, xmax, 100)  # x軸の範囲を100分割した配列を生成
p = norm.pdf(x, np.mean(fisher_z), np.std(fisher_z))  # 正規分布の確率密度関数を計算
axes[1].plot(x, p, 'darkred', linestyle="--", linewidth=1,
             label='Fitted Normal')  # 正規分布を描画
axes[1].set_title('フィッシャー変換後の相関係数')  # タイトルを設定
axes[1].set_xlabel('$z$')  # x軸ラベルを設定


plt.savefig('6_3_3_z_transformation_experiment.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
