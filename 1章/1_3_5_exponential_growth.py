import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams["font.size"] = 14
# 0から2までの範囲で等間隔に100個の数を生成
x = np.linspace(0, 30, 30)

# 指数関数と線形関数の値を計算
exp_y = np.exp(x / 10) * 100     # 指数関数
# ランダムなノイズを付加する
exp_y = exp_y * (1 + np.random.normal(0, 0.08, 30))

linear_y = 2 * x + 1  # 線形関数


# フィギュアの大きさを設定
plt.figure(figsize=(8, 4))

# 通常のプロット
plt.subplot(1, 2, 1)  # 1行2列の左側
plt.plot(x, exp_y, marker='o', linestyle='none', label='Exponential')

plt.xticks(np.arange(0, 31, 5))  # X軸のラベルを0.5刻みに設定

# plt.legend()
# plt.title("Normal plot")
# plt.xlabel("X")
# plt.ylabel("Y")

# 片対数プロット
plt.subplot(1, 2, 2)  # 1行2列の右側
plt.semilogy(x, exp_y, marker='o', linestyle='none', label='Exponential')
plt.xticks(np.arange(0, 31, 5))  # X軸のラベルを0.5刻みに設定

# plt.legend()
# plt.title("Semi-log plot (Y-axis in log scale)")
# plt.xlabel("X")
# plt.ylabel("Y (log scale)")

# プロットの表示
plt.tight_layout()  # タイトルとラベルが重ならないようにする
plt.savefig("1_3_5_exponential_growth.png", dpi=300)
plt.savefig("1_3_5_exponential_growth.svg", dpi=300)

# plt.show()
