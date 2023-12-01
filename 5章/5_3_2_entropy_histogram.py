import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from scipy.stats import entropy  # エントロピーの計算のためのSciPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# シード値を固定
np.random.seed(42)

# サンプルサイズ
n_samples = 500

# ビンの設定
bins = np.linspace(-5, 5, 40)

# 一様分布
uniform_samples = np.random.uniform(-5, 5, n_samples)  # 一様分布からサンプリング
uniform_hist, _ = np.histogram(uniform_samples, bins=bins)  # ヒストグラムで集計する
uniform_entropy = entropy(uniform_hist)  # エントロピー計算

# 正規分布
normal_samples = np.random.normal(0, 1, n_samples)  # 正規分布からサンプリング
normal_hist, _ = np.histogram(normal_samples, bins=bins)  # ヒストグラムで集計する
normal_entropy = entropy(normal_hist)  # エントロピー計算

# 2つの正規分布
gmm_samples1 = np.random.normal(-2, 0.25, n_samples // 2)  # 正規分布からサンプリング
gmm_samples2 = np.random.normal(2, 0.25, n_samples // 2)  # 正規分布からサンプリング
gmm_samples = np.concatenate([gmm_samples1, gmm_samples2])  # 二つのサンプルを結合
gmm_hist, _ = np.histogram(gmm_samples, bins=bins)  # ヒストグラムで集計する
gmm_entropy = entropy(gmm_hist)  # エントロピー計算

# ヒストグラムの描画
plt.figure(figsize=(10, 4))  # 図の準備

plt.subplot(1, 3, 1)  # 1行3列の左
plt.hist(uniform_samples, bins=bins,
         color='skyblue', edgecolor='k')  # ヒストグラム描画
plt.title(f'一様分布\nエントロピー: {uniform_entropy:.2f}')  # タイトル
plt.ylabel('頻度')  # y軸ラベル

plt.subplot(1, 3, 2)  # 1行3列の中央
plt.hist(normal_samples, bins=bins, color='salmon', edgecolor='k')  # ヒストグラム描画
plt.title(f'正規分布\nエントロピー: {normal_entropy:.2f}')  # タイトル

plt.subplot(1, 3, 3)  # 1行3列の右
plt.hist(gmm_samples, bins=bins, color='lightgreen', edgecolor='k')  # ヒストグラム描画
plt.title(f'2つの正規分布の混合\nエントロピー: {gmm_entropy:.2f}')  # タイトル


plt.tight_layout()  # レイアウトの調整
plt.savefig('5_3_2_entropy_histogram.png', dpi=300)  # 画像を保存
plt.show()  # 画面に表示
