import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# シード値を固定
np.random.seed(42)

# 正規分布のパラメータ（平均と標準偏差）
mu1, sigma1 = 0, 1
mu2, sigma2 = 2, 1

# サンプルデータの生成
num_samples = 50
samples1 = np.random.normal(mu1, sigma1, num_samples)
samples2 = np.random.normal(mu2, sigma2, num_samples)

# ソート
samples1.sort()
samples2.sort()

# 可視化
plt.figure(figsize=(8, 4))  # 図の準備
plt.scatter(samples1, np.ones(num_samples), color='red', label='分布１', zorder=2)
plt.scatter(samples2, np.zeros(num_samples),
            color='blue', label='分布２', zorder=2)

# 最短距離を繋ぐ線を描画
for x1, x2 in zip(samples1, samples2):
    plt.plot([x1, x2], [1, 0], '-', color='gray', linewidth=1, zorder=1)

plt.yticks([0, 1], ['分布２', '分布１'])  # y軸の目盛りを設定
plt.tight_layout()  # レイアウトの設定
plt.savefig('6_2_3_wasserstein_distance.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
