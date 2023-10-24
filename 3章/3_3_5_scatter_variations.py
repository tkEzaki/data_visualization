import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  # 追加
import japanize_matplotlib

plt.rcParams["font.size"] = 16

# 相関の少ないデータの生成
np.random.seed(42)
x1 = np.random.normal(25, 10, 100)
y1 = np.random.normal(75, 10, 100)

# 相関の多いデータの生成
x2 = np.random.normal(50, 30, 500)
y2 = 0.5 * x2 + np.random.normal(0, 10, 500)

x3 = np.random.normal(25, 20, 400)
y3 = np.random.normal(25, 30, 400)

# データの統合
x = np.concatenate([x1, x2, x3])
y = np.concatenate([y1, y2, y3])

# GridSpecを作成
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 0.1])  # 追加

# プロット領域を作成
fig = plt.figure(figsize=(12, 10))

ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[0, 1])
ax3 = plt.subplot(gs[1, 0])
cbar_ax = plt.subplot(gs[1, 2])  # 追加

# 左側のサブプロットに統合データの散布図をプロット
ax1.scatter(x, y, alpha=1)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

# 中央のサブプロットに統合データの半透明なマーカー散布図をプロット
ax2.scatter(x, y, alpha=0.2)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')

# 右側のサブプロットに統合データのヒートマップをプロット
heatmap, xedges, yedges = np.histogram2d(x, y, bins=20)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
im = ax3.imshow(heatmap.T, origin='lower', extent=extent, aspect='auto', cmap='jet')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')

# カラーバーを描画
fig.colorbar(im, cax=cbar_ax)
cbar_ax.set_ylabel('頻度', fontsize=20)

# サブプロット間のスペースを調整
plt.tight_layout()

plt.savefig('3_3_5_scatter_variations.png', dpi=300)
plt.savefig('3_3_5_scatter_variations.svg', dpi=300)

# グラフを表示
plt.show()
