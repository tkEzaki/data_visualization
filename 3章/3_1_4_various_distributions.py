import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ
from scipy.stats import norm, binom, poisson, expon, uniform, gamma, lognorm, weibull_min, pareto  # 分布描画のための関数

plt.rcParams['font.size'] = 16  # フォントサイズを16に設定

colors = ['red', 'blue', 'green', 'purple',
          'orange', 'brown', 'pink', 'grey', 'cyan']  # グラフの色

fig, axs = plt.subplots(3, 3, figsize=(14, 10))  # 3行3列のグラフを作成

#  一様分布
x_values = np.linspace(-1, 1, 1000)  # x軸の値
axs[0, 0].plot(x_values, uniform.pdf(x_values, -1, 2),
               color=colors[4], label="$f(x) = \\frac{1}{b - a}$")  # 一様分布を描画
axs[0, 0].set_ylim(0, 1)  # y軸の範囲を設定
axs[0, 0].legend()  # 凡例を表示
axs[0, 0].set_title("一様分布", fontsize=20)  # タイトル

# 正規分布
x_values = np.linspace(-4, 4, 1000)  # x軸の値
axs[0, 1].plot(x_values, norm.pdf(x_values, 0, 1), color=colors[0],
               label="$f(x) = \\frac{1}{\\sqrt{2\\pi\\sigma^2}} e^{ -\\frac{(x-\\mu)^2}{2\\sigma^2} }$")  # 正規分布を描画
axs[0, 1].set_ylim(0, 0.65)  # y軸の範囲を設定
axs[0, 1].legend()  # 凡例を表示
axs[0, 1].set_title("正規分布", fontsize=20)  # タイトル

# 二項分布
n, p = 10, 0.5  # パラメータ
x_values = range(n + 1)  # x軸の値
axs[0, 2].plot(x_values, binom.pmf(x_values, n, p), 'o', color=colors[1],
               label="$P(k; n, p)=$" + "\n" + "  $C(n, k) p^k (1-p)^{n-k}$")  # 二項分布を描画
axs[0, 2].set_ylim(0, 0.4)  # y軸の範囲を設定
axs[0, 2].legend()  # 凡例を表示
axs[0, 2].set_title("二項分布", fontsize=20)  # タイトル

# ポアソン分布
mu = 3  # パラメータ
x_values = range(10)  # x軸の値
axs[1, 0].plot(x_values, poisson.pmf(x_values, mu), 'o', color=colors[2],
               label="$P(k; \\mu) = \\frac{e^{-\\mu} \\mu^k}{k!}$")  # ポアソン分布を描画
axs[1, 0].set_ylim(0, 0.3)  # y軸の範囲を設定
axs[1, 0].legend()  # 凡例を表示
axs[1, 0].set_title("ポアソン分布", fontsize=20)  # タイトル

# 指数分布
x_values = np.linspace(0, 10, 1000)  # x軸の値
axs[1, 1].plot(x_values, expon.pdf(x_values), color=colors[3],
               label="$f(x; \\lambda) = \\lambda e^{-\\lambda x}$")  # 指数分布を描画
axs[1, 1].set_ylim(0, 1.0)  # y軸の範囲を設定
axs[1, 1].legend(loc='lower right')  # 凡例を表示
axs[1, 1].set_title("指数分布", fontsize=20)  # タイトル

# 指数分布の挿入図
axins_exp = axs[1, 1].inset_axes([0.5, 0.5, 0.47, 0.47])  # 挿入図の軸を作成
x_values_large = np.linspace(0.01, 10, 1000)  # x軸の値
axins_exp.plot(x_values_large, expon.pdf(
    x_values_large), color=colors[3])  # 指数分布を描画
axins_exp.set_yscale('log')  # y軸を対数スケールに設定
axins_exp.set_yticks([0.0001, 0.01, 1])  # y軸の目盛りを設定
axins_exp.set_yticklabels(
    ['$10^{-4}$', '$10^{-2}$', '$10^{0}$'])  # y軸の目盛りのラベルを設定


# ガンマ分布
x_values = np.linspace(0, 10, 1000)  # x軸の値
axs[1, 2].plot(x_values, gamma.pdf(x_values, a=5), color=colors[5],
               label="$f(x; \\alpha) = \\frac{1}{\\Gamma(\\alpha)} \\beta^{\\alpha} x^{\\alpha - 1} e^{-\\beta x}$")  # ガンマ分布を描画
axs[1, 2].set_ylim(0, 0.3)  # y軸の範囲を設定
axs[1, 2].legend()  # 凡例を表示
axs[1, 2].set_title("ガンマ分布", fontsize=20)  # タイトル

# ワイブル分布
x_values = np.linspace(0.01, 2, 1000)  # x軸の値
axs[2, 0].plot(x_values, weibull_min.pdf(x_values, c=1.5), color=colors[7],
               label="$f(x; k) = k (\\frac{x}{\\lambda})^{k - 1} e^{-(x/\\lambda)^{k}}$")  # ワイブル分布を描画
axs[2, 0].set_ylim(0, 1.1)  # y軸の範囲を設定
axs[2, 0].legend(loc='upper right', framealpha=0.5)  # 凡例を表示
axs[2, 0].set_title("ワイブル分布", fontsize=20)  # タイトル

# 対数正規分布
x_values = np.linspace(0.01, 10, 1000)  # x軸の値
axs[2, 1].plot(x_values, lognorm.pdf(x_values, s=1), color=colors[6],
               label="$f(x; \\mu, \\sigma) = \\frac{1}{x \\sigma \\sqrt{2\\pi}} e^{-\\frac{(\\ln x - \\mu)^2}{2\\sigma^2}}$")  # 対数正規分布を描画
axs[2, 1].set_ylim(0, 0.8)  # y軸の範囲を設定
axs[2, 1].legend(loc='lower right', framealpha=0.5)  # 凡例を表示
axs[2, 1].set_title("対数正規分布", fontsize=20)  # タイトル

# 対数正規分布の挿入図
axins_lognorm = axs[2, 1].inset_axes([0.5, 0.5, 0.47, 0.47])  # 挿入図の軸を作成
x_values_large = np.linspace(-5, 3, 100)  # x軸の値
x_values_large = np.exp(x_values_large)  # x軸の値を変換
axins_lognorm.plot(x_values_large, lognorm.pdf(
    x_values_large, s=1), color=colors[6])  # 対数正規分布を描画
axins_lognorm.set_xscale('log')  # x軸を対数スケールに設定

# パレート分布
x_values = np.linspace(1, 4, 1000)  # x軸の値
axs[2, 2].plot(x_values, pareto.pdf(x_values, b=5),
               color=colors[8])  # パレート分布を描画
axs[2, 2].set_ylim(0, 6)  # y軸の範囲を設定
axs[2, 2].legend(
    ["$f(x; \\alpha) = \\alpha x_m^{\\alpha} x^{-\\alpha - 1}$"], loc='lower right')  # 凡例を表示
axs[2, 2].set_title("パレート分布", fontsize=20)  # タイトル

# パレート分布の挿入図
axins = axs[2, 2].inset_axes([0.5, 0.5, 0.47, 0.47])  # 挿入図の軸を作成
x_values_large = np.linspace(1, 100, 1000)  # x軸の値
axins.plot(x_values_large, pareto.pdf(
    x_values_large, b=5), color=colors[8])  # パレート分布を描画
axins.set_xscale('log')  # x軸を対数スケールに設定
axins.set_yscale('log')  # y軸を対数スケールに設定
axins.set_yticks([0.0000000001, 0.0001])  # y軸の目盛りを設定
axins.get_yaxis().set_tick_params(
    which='both', direction='out', pad=5)  # y軸の目盛りの位置を設定
axins.set_yticklabels(['$10^{-10}$', '$10^{-4}$'])  # y軸の目盛りのラベルを設定
axins.xaxis.set_tick_params(which='minor', length=0)  # x軸の補助目盛りを非表示


plt.tight_layout()  # レイアウトの設定
plt.savefig('3_1_4_various_distributions.png', dpi=300)  # 画像ファイルの保存
plt.show()  # 画像の表示
