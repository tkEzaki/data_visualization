import matplotlib.pyplot as plt

# データ生成
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# プロット作成
plt.plot(x, y)

# タイトルと軸ラベル
plt.title("Using plt.plot()")
plt.xlabel("x")
plt.ylabel("y")

# グラフ表示
plt.show()
