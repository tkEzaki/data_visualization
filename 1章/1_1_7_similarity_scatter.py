import numpy as np  # NumPyをインポートする（数値計算ライブラリ）
import matplotlib.pyplot as plt  # Matplotlibのpyplotをインポートする（グラフ描画ライブラリ）
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする
from scipy import stats  # SciPyからstatsをインポートする（統計関連の機能を利用）


n = 190  # データ点の数
low, high = -0.45, 0.95  # データの範囲
rho = 0.7  # 相関係数
mean = [0, 0]  # 平均（二変数）
cov = [[1, rho], [rho, 1]]  # 共分散行列
rng = np.random.default_rng(seed=42)  # 乱数生成器
x, y = rng.multivariate_normal(mean, cov, n - 1).T  # 多変量正規分布からデータ生成
x = low + (high - low) * (x - x.min()) / (x.max() - x.min())  # xデータの正規化
y = low + (high - low) * (y - y.min()) / (y.max() - y.min())  # yデータの正規化
x = np.append(x, 0.80)  # 特定の点を追加
y = np.append(y, 0.72)  # 特定の点を追加
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)  # 線形回帰分析

plt.scatter(x, y, c="orange", alpha=0.5)  # 散布図の描画
plt.plot(x, intercept + slope * x, 'orange')  # 回帰直線の描画
plt.scatter([0.80], [0.72], c="r")  # 特定の点を赤色で描画
plt.gca().set_aspect('equal', adjustable='box')  # アスペクト比を等しく設定
plt.xticks([-0.5, 0.0, 0.5, 1])  # X軸の目盛り
plt.yticks([-0.5, 0.0, 0.5, 1])  # Y軸の目盛り
plt.xlim([-0.5, 1.0])  # X軸の表示範囲
plt.ylim([-0.5, 1.0])  # Y軸の表示範囲
plt.tick_params(axis='both', which='major', labelsize=15)  # 目盛りの設定
plt.savefig('1_1_7_similarity_scatter.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示

