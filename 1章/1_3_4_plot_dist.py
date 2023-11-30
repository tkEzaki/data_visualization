import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from scipy.stats import norm  # 正規分布のためのSciPy
from scipy.stats import pareto  # パレート分布のためのSciPy
from scipy.stats import cauchy  # コーシー分布のためのSciPy
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

fontsize = 14

def plot_norm():
    # 平均0、標準偏差1の正規分布から10000個のサンプルを生成
    mu = 0  # 平均
    sigma = 1  # 標準偏差
    samples = np.random.normal(mu, sigma, 10000)  # 正規分布から10000個のサンプルを生成

    plt.figure(figsize=(5, 3))  # 新しい図の作成
    # ヒストグラム（頻度分布）をプロット
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='gray')

    # 正規分布の理論的な確率密度関数をプロット
    xmin, xmax = plt.xlim()  # x軸の範囲を取得
    x = np.linspace(xmin, xmax, 100)  # x軸の範囲を100分割したデータを生成
    p = norm.pdf(x, mu, sigma)  # 正規分布の確率密度関数を計算
    plt.plot(x, p, 'r', linewidth=2)  # 確率密度関数をプロット

    plt.xticks(fontsize=fontsize)  # x軸の目盛りの設定
    plt.yticks(fontsize=fontsize)  # y軸の目盛りの設定
    plt.yticks(np.arange(0, 0.45, 0.1), fontsize=fontsize)  # y軸の目盛りを0-0.45、0.1刻みに設定
    plt.ylim([0, 0.45])  # y軸の範囲を0-0.45に設定
    plt.tight_layout()  # レイアウトの調整
    plt.savefig("1_3_4_normal_dist.png", dpi=300)  # 画像として保存
    plt.show()  # グラフの表示


def plot_cauchy():
    # 標準コーシー分布から10000個のサンプルを生成
    samples = np.random.standard_cauchy(100000)

    # ここでは外れ値を捨てて描画
    samples = samples[(samples > -10) & (samples < 10)]

    plt.figure(figsize=(5, 3))  # 新しい図の作成 
    plt.hist(samples, bins=50, density=True, alpha=0.6, color='gray')  # ヒストグラム（頻度分布）をプロット

    # コーシー分布の理論的な確率密度関数をプロット
    xmin, xmax = plt.xlim()  # x軸の範囲を取得
    x = np.linspace(xmin, xmax, 1000)  # x軸の範囲を1000分割したデータを生成
    p = cauchy.pdf(x)  # コーシー分布の確率密度関数を計算
    plt.plot(x, p, 'b', linewidth=2)  # 確率密度関数をプロット

    plt.xticks(fontsize=fontsize)  # x軸の目盛りの設定
    plt.yticks(fontsize=fontsize)  # y軸の目盛りの設定
    plt.yticks(np.arange(0, 0.45, 0.1), fontsize=fontsize)  # y軸の目盛りを0-0.45、0.1刻みに設定
    plt.ylim([0, 0.45])  # y軸の範囲を0-0.45に設定
    plt.tight_layout()  # レイアウトの調整
    plt.savefig("1_3_4_cauchy_dist.png", dpi=300)  # 画像として保存
    plt.show()  # グラフの表示


def plot_tail_comparison():
    samples_cauchy = np.random.standard_cauchy(100000)  # 標準コーシー分布から100000個のサンプルを生成
    samples_cauchy = samples_cauchy[(samples_cauchy > -50) & (samples_cauchy < 50)]  # データを制限

    samples_normal = np.random.normal(size=100000)  # 標準正規分布から100000個のサンプルを生成
    samples_normal = samples_normal[(samples_normal > -50) & (samples_normal < 50)]  # データを制限

    # コーシー分布のヒストグラムを作成し、値と頻度を取得
    counts_cauchy, bin_edges_cauchy = np.histogram(samples_cauchy, bins=100, density=True)  # ヒストグラムを作成
    bins_cauchy = (bin_edges_cauchy[1:] + bin_edges_cauchy[:-1]) / 2  # ヒストグラムのビンの中心値を計算
    non_zero_counts_cauchy = counts_cauchy > 0  # 頻度が0のデータを除外
    counts_cauchy = counts_cauchy[non_zero_counts_cauchy]   # 頻度が0のデータを除外
    bins_cauchy = bins_cauchy[non_zero_counts_cauchy]  # 頻度が0のデータを除外
    idx_cauchy = np.argsort(np.abs(bins_cauchy))  # 絶対値の大きい順にソート
    counts_cauchy = counts_cauchy[idx_cauchy]  # 絶対値の大きい順にソート
    bins_cauchy = bins_cauchy[idx_cauchy]  # 絶対値の大きい順にソート

    # 正規分布のヒストグラムを作成し、値と頻度を取得
    counts_normal, bin_edges_normal = np.histogram(samples_normal, bins=100, density=True)  # ヒストグラムを作成
    bins_normal = (bin_edges_normal[1:] + bin_edges_normal[:-1]) / 2  # ヒストグラムのビンの中心値を計算
    non_zero_counts_normal = counts_normal > 0  # 頻度が0のデータを除外
    counts_normal = counts_normal[non_zero_counts_normal]  # 頻度が0のデータを除外
    bins_normal = bins_normal[non_zero_counts_normal]  # 頻度が0のデータを除外
    idx_normal = np.argsort(np.abs(bins_normal))  # 絶対値の大きい順にソート
    counts_normal = counts_normal[idx_normal]  # 絶対値の大きい順にソート
    bins_normal = bins_normal[idx_normal]  # 絶対値の大きい順にソート

    # 図の大きさを設定
    plt.figure(figsize=(5, 3))

    # 両対数プロットによるヒストグラムの描画
    plt.loglog(bins_cauchy, counts_cauchy, marker='o', color='b', linestyle='none', label='Standard Cauchy')
    plt.loglog(bins_normal, counts_normal, marker='o', color='r', linestyle='none', label='Standard Normal')

    plt.xticks(fontsize=fontsize)  # x軸の目盛りの設定
    plt.yticks(fontsize=fontsize)  # y軸の目盛りの設定
    plt.tight_layout()  # レイアウトの調整
    plt.savefig("1_3_4_tail_comparison.png", dpi=300)  # 画像として保存
    plt.show()  # グラフの表示




plot_norm()
plot_cauchy()
plot_tail_comparison()
