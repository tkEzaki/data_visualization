import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
from scipy.stats import norm  # 正規分布のためのSciPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 16  # フォントサイズを設定

# シード値を固定
np.random.seed(42)

# 正規分布のパラメータ（平均と標準偏差）
mu1, sigma1 = -1, 1
mu2, sigma2 = 1, 1

# サンプルデータの生成
num_samples = 10000
samples1 = np.random.normal(mu1, sigma1, num_samples)
samples2 = np.random.normal(mu2, sigma2, num_samples)

# ビンの設定
bins = np.linspace(-5, 5, 50)

# ヒストグラムを計算
hist1, bin_edges = np.histogram(samples1, bins=bins, density=True)
hist2, _ = np.histogram(samples2, bins=bins, density=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# 全変動距離（TVD）を計算
tvd_sample = 0.5 * np.sum(np.abs(hist1 - hist2)) * \
    (bin_centers[1] - bin_centers[0])

# サンプルデータに対する全変動距離と面積を表示
plt.figure(figsize=(6, 4))  # 図の準備
plt.hist(samples1, bins=bins, color='gray', alpha=0.3,
         label='Sample Distribution 1', density=True)
plt.hist(samples2, bins=bins, color='gray', alpha=0.3,
         label='Sample Distribution 2', density=True)
plt.plot(bin_centers, hist1, 'r-', lw=2,
         label=f'Sample Distribution 1 (mu={mu1}, sigma={sigma1})')
plt.plot(bin_centers, hist2, 'b-', lw=2,
         label=f'Sample Distribution 2 (mu={mu2}, sigma={sigma2})')
# 間を塗りつぶす
plt.fill_between(bin_centers, hist1, hist2, where=(hist1 > hist2),
                 interpolate=True, color='red', alpha=0.2, label='TVD Area (dist1 > dist2)')
plt.fill_between(bin_centers, hist1, hist2, where=(hist1 <= hist2),
                 interpolate=True, color='blue', alpha=0.2, label='TVD Area (dist1 <= dist2)')

# タイトルと軸ラベルを設定
plt.title(f'全変動距離: {tvd_sample:.4f}', fontsize=16)
plt.ylabel('確率密度')

plt.tight_layout()  # レイアウトの設定
plt.savefig('6_2_2_total_variation.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
