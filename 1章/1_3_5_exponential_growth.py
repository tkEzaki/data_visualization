import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams["font.size"] = 14  # フォントサイズを14に設定

x = np.linspace(0, 30, 30)  # 0から2までの範囲で等間隔に100個の数を生成

# 指数関数と線形関数の値を計算
exp_y = np.exp(x / 10) * 100  # 指数関数
exp_y = exp_y * (1 + np.random.normal(0, 0.08, 30))  # ランダムなノイズを付加する

linear_y = 2 * x + 1  # 線形関数

# プロットの設定
plt.figure(figsize=(8, 4))

# 通常のプロット
plt.subplot(1, 2, 1)  # 1行2列の左側
plt.plot(x, exp_y, marker='o', linestyle='none',
         label='Exponential')  # 指数関数をプロット
plt.xticks(np.arange(0, 31, 5))  # X軸のラベルを0.5刻みに設定

# 片対数プロット
plt.subplot(1, 2, 2)  # 1行2列の右側
plt.semilogy(x, exp_y, marker='o', linestyle='none',
             label='Exponential')  # 指数関数をプロット
plt.xticks(np.arange(0, 31, 5))  # X軸のラベルを0.5刻みに設定

# プロットの表示
plt.tight_layout()  # タイトルとラベルが重ならないようにする
plt.savefig("1_3_5_exponential_growth.png", dpi=300)  # 画像として保存
plt.show()  # グラフの表示
