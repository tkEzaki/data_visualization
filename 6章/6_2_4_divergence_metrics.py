import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# シード値を固定
np.random.seed(42)

# KL情報量を計算する関数
def kl_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))


# 正規分布のパラメータ (平均と標準偏差)
mu1, sigma1 = 0, 0.5
mu2, sigma2 = 2, 1

# サンプルデータの生成
num_samples = 10000
samples1 = np.random.normal(mu1, sigma1, num_samples)
samples2 = np.random.normal(mu2, sigma2, num_samples)

# サンプルを[-1, 3]の範囲に絞り込む
filtered_samples1 = samples1[(samples1 >= -1) & (samples1 <= 3)]
filtered_samples2 = samples2[(samples2 >= -1) & (samples2 <= 3)]

# 非ゼロのビンを確保するために、限られた範囲でヒストグラムを生成
limited_bins = np.linspace(-1, 3, 50)
hist1, _ = np.histogram(filtered_samples1, bins=limited_bins, density=True)
hist2, _ = np.histogram(filtered_samples2, bins=limited_bins, density=True)

# ヒストグラムを正規化
hist1 /= np.sum(hist1 * (limited_bins[1] - limited_bins[0]))
hist2 /= np.sum(hist2 * (limited_bins[1] - limited_bins[0]))

# KLダイバージェンスを再計算
kl_1_to_2 = kl_divergence(hist1, hist2)
kl_2_to_1 = kl_divergence(hist2, hist1)

# JSダイバージェンスを再計算
js_divergence = 0.5 * (kl_divergence(hist1, 0.5 * (hist1 + hist2)) +
                       kl_divergence(hist2, 0.5 * (hist1 + hist2)))

# ヒストグラムを再描画し、ダイバージェンスを表示
plt.figure(figsize=(8, 5))
plt.hist(filtered_samples1, bins=limited_bins, alpha=0.5, label=f'Filtered Sample Distribution 1',
         density=False, weights=np.ones(len(filtered_samples1)) / len(filtered_samples1))
plt.hist(filtered_samples2, bins=limited_bins, alpha=0.5, label=f'Filtered Sample Distribution 2',
         density=False, weights=np.ones(len(filtered_samples2)) / len(filtered_samples2))

# タイトルを設定
plt.title(f'KL情報量: {kl_1_to_2:.4f} (1→2), ∞ (2→1), JS情報量: {js_divergence:.4f}')
plt.ylabel('相対頻度')  # y軸ラベルを設定

plt.savefig('6_2_4_kl_js_divergence.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
