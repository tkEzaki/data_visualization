import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams["font.size"] = "14"

# データ生成
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# フィギュアとサブプロットの生成
fig, ax = plt.subplots(figsize=(5, 5))

# プロット作成
ax.plot(x, y)

# タイトルと軸ラベル
ax.set_title("Using ax.plot()")
ax.set_xlabel("x")
ax.set_ylabel("y")

# グラフ表示
plt.savefig("9_1_3_1_show_fig_ax_sample.png", dpi=300)
plt.show()
