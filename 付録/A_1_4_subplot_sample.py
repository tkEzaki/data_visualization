import matplotlib.pyplot as plt

# フィギュアオブジェクトと4つのサブプロットを作成
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 6))

# フィギュアタイトルを設定
fig.suptitle('Figure and Axes Relationship', fontsize=16)

# 各サブプロットにタイトルを設定
ax1.set_title('Subplot 1')
ax2.set_title('Subplot 2')
ax3.set_title('Subplot 3')
ax4.set_title('Subplot 4')

# 図を表示
plt.show()