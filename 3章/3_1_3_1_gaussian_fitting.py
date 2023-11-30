import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ
from scipy.stats import norm  # 正規分布のためのSciPy
from scipy.stats import gumbel_r  # ガンベル分布のためのSciPy

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定
np.random.seed(0)  # 乱数のシードを設定（再現性のため）


def roll_dice(n=100, repeat=100):
    # サイコロをn回振った時の出目の総和をrepeat回サンプリングする
    return np.array([np.sum(np.random.randint(1, 7, size=n)) for _ in range(repeat)])


# サイコロを100回振った時の出目の総和を1000回サンプリングする
dice_sums = np.array([roll_dice() for _ in range(1000)]).flatten()

# 図の作成
plt.figure(figsize=(5, 4))  # グラフのサイズを指定

# ヒストグラムを作成
plt.hist(dice_sums, bins=range(280, 420), density=True, alpha=0.7,
         label='Experimental', color="white", edgecolor='gray')  # ヒストグラムを描画

# 正規分布のパラメータを推定
mu, std = norm.fit(dice_sums)  # 平均と標準偏差を推定
print(mu, std)

# 正規分布を描画
xmin, xmax = plt.xlim()  # x軸の最小値と最大値
x = np.linspace(xmin, xmax, 100)  # x軸の値
p = norm.pdf(x, mu, std)  # 正規分布の値

plt.plot(x, p, 'r--', linewidth=2, label='Normal Distribution')  # 正規分布を描画
plt.xlabel('サイコロを100回振って出た目の総和')  # x軸ラベル
plt.ylabel('相対頻度')  # y軸ラベル

plt.tight_layout()  # レイアウトの設定
plt.savefig('3_1_3_1_gaussian_fitting.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示
