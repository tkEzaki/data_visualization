import matplotlib.pyplot as plt

# データ生成
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# フィギュアとサブプロットの生成
fig, ax = plt.subplots()

# プロット作成
ax.plot(x, y)

# タイトルと軸ラベル
ax.set_title("Using ax.plot()")
ax.set_xlabel("x")
ax.set_ylabel("y")

# グラフ表示
plt.show()
