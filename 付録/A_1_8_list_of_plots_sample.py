import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# ラインプロット
ax.plot(x, y1)
# 棒グラフ
ax.bar(x, y2)
# 散布図
ax.scatter(scatter_x, scatter_y1)
# ヒストグラム
ax.hist(data)
# 等高線図
c = ax.contour(X, Y, Z)
ax.clabel(c, inline=1, fontsize=10)
# 画像の表示
ax.imshow(image_data)
# 円グラフ
ax.pie(sizes)
# 箱ひげ図
ax.boxplot(data)
# エラーバー付きのバー
ax.errorbar(x, y, yerr=y_error)
