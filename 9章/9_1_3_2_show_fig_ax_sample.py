import matplotlib.pyplot as plt
import japanize_matplotlib
plt.rcParams["font.size"] = "14"

# データ生成
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# フィギュアオブジェクトを作成
fig = plt.figure(figsize=(5, 5))

# フィギュアタイトルを設定
fig.suptitle('Figure and Axes Relationship', fontsize=16)

# 2x2のグリッドの1番目にax1を作成
ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title('Subplot 1')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.plot(x, y)

# 2x2のグリッドの2番目にax2を作成
ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title('Subplot 2')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.plot(x, y)

# 2x2のグリッドの3番目にax3を作成
ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title('Subplot 3')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.plot(x, y)

# 2x2のグリッドの4番目にax4を作成
ax4 = fig.add_subplot(2, 2, 4)
ax4.set_title('Subplot 4')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.plot(x, y)

print(ax4.axis)
# 図を表示
plt.tight_layout()
plt.savefig("9_1_3_2_show_fig_ax_sample.png", dpi=300)
plt.savefig("9_1_3_2_show_fig_ax_sample.svg", dpi=300)

plt.show()
