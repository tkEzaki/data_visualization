import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import pareto
from scipy.stats import cauchy
import japanize_matplotlib


fontsize = 14


def plot_norm():
    # 平均0、標準偏差1の正規分布から10000個のサンプルを生成
    mu = 0
    sigma = 1
    samples = np.random.normal(mu, sigma, 10000)

    plt.figure(figsize=(5, 3))
    # ヒストグラム（頻度分布）をプロット
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='gray')

    # 正規分布の理論的な確率密度関数をプロット
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)
    plt.plot(x, p, 'r', linewidth=2)

    # title = "Fit results: mu = %.2f,  std = %.2f" % (mu, sigma)
    # plt.title(title)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.yticks(np.arange(0, 0.45, 0.1), fontsize=fontsize)  # y軸の目盛りを0-0.45、0.1刻みに設定
    plt.ylim([0, 0.45])  # y軸の範囲を0-0.45に設定
    plt.tight_layout()
    plt.savefig("1_3_4_normal_dist.png", dpi=300)
    plt.savefig("1_3_4_normal_dist.svg", dpi=300)

    # plt.show()


def plot_cauchy():
    # 標準コーシー分布から10000個のサンプルを生成
    samples = np.random.standard_cauchy(100000)

    # サンプリングデータを適切に描画するためには、あまりにも外れた値を切り捨てることがよく行われます。
    samples = samples[(samples > -10) & (samples < 10)]

    plt.figure(figsize=(5, 3))

    # ヒストグラム（頻度分布）をプロット
    plt.hist(samples, bins=50, density=True, alpha=0.6, color='gray')

    # コーシー分布の理論的な確率密度関数をプロット
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 1000)
    p = cauchy.pdf(x)
    plt.plot(x, p, 'b', linewidth=2)

    # plt.title("Standard Cauchy Distribution")
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.yticks(np.arange(0, 0.45, 0.1), fontsize=fontsize)  # y軸の目盛りを0-0.45、0.1刻みに設定
    plt.ylim([0, 0.45])  # y軸の範囲を0-0.45に設定
    plt.tight_layout()
    plt.savefig("1_3_4_cauchy_dist.png", dpi=300)
    plt.savefig("1_3_4_cauchy_dist.svg", dpi=300)

    # plt.show()


def plot_tail_comparison():
    # 標準コーシー分布から100000個のサンプルを生成
    samples_cauchy = np.random.standard_cauchy(100000)
    samples_cauchy = samples_cauchy[(samples_cauchy > -50) & (samples_cauchy < 50)]  # データを制限

    # 標準正規分布から100000個のサンプルを生成
    samples_normal = np.random.normal(size=100000)
    samples_normal = samples_normal[(samples_normal > -50) & (samples_normal < 50)]  # データを制限

    # コーシー分布のヒストグラムを作成し、値と頻度を取得
    counts_cauchy, bin_edges_cauchy = np.histogram(samples_cauchy, bins=100, density=True)
    bins_cauchy = (bin_edges_cauchy[1:] + bin_edges_cauchy[:-1]) / 2
    non_zero_counts_cauchy = counts_cauchy > 0
    counts_cauchy = counts_cauchy[non_zero_counts_cauchy]
    bins_cauchy = bins_cauchy[non_zero_counts_cauchy]
    idx_cauchy = np.argsort(np.abs(bins_cauchy))
    counts_cauchy = counts_cauchy[idx_cauchy]
    bins_cauchy = bins_cauchy[idx_cauchy]

    # 正規分布のヒストグラムを作成し、値と頻度を取得
    counts_normal, bin_edges_normal = np.histogram(samples_normal, bins=100, density=True)
    bins_normal = (bin_edges_normal[1:] + bin_edges_normal[:-1]) / 2
    non_zero_counts_normal = counts_normal > 0
    counts_normal = counts_normal[non_zero_counts_normal]
    bins_normal = bins_normal[non_zero_counts_normal]
    idx_normal = np.argsort(np.abs(bins_normal))
    counts_normal = counts_normal[idx_normal]
    bins_normal = bins_normal[idx_normal]

    # フィギュアの大きさを設定（ここで縦長に設定）
    plt.figure(figsize=(5, 3))

    # 両対数プロットによるヒストグラムの描画
    plt.loglog(bins_cauchy, counts_cauchy, marker='o', color='b', linestyle='none', label='Standard Cauchy')
    plt.loglog(bins_normal, counts_normal, marker='o', color='r', linestyle='none', label='Standard Normal')

    # plt.title("Log-Log plot of the tail of Standard Distributions")
    # plt.xlabel("Value (log scale)")
    # plt.ylabel("Frequency (log scale)")
    # plt.legend()

    # plt.show()
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.tight_layout()
    plt.savefig("1_3_4_tail_comparison.png", dpi=300)
    plt.savefig("1_3_4_tail_comparison.svg", dpi=300)



plot_norm()
plot_cauchy()
plot_tail_comparison()
