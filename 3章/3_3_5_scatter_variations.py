import numpy as np  # 数値計算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import matplotlib.gridspec as gridspec  # グラフレイアウトのためのgridpec
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams["font.size"] = 16  # フォントサイズの設定

# 相関の少ないデータの生成
np.random.seed(42)  # 同じ乱数が生成されるようにシードを設定
x1 = np.random.normal(25, 10, 100)  # 平均25、分散10の正規分布
y1 = np.random.normal(75, 10, 100)  # 平均75、分散10の正規分布

# 相関の多いデータの生成
x2 = np.random.normal(50, 30, 500)  # 平均50、分散30の正規分布
y2 = 0.5 * x2 + np.random.normal(0, 10, 500)  # y = 0.5x + ノイズ

x3 = np.random.normal(25, 20, 400)  # 平均25、分散20の正規分布
y3 = np.random.normal(25, 30, 400)  # 平均25、分散30の正規分布

# データの統合
x = np.concatenate([x1, x2, x3])  # xを統合
y = np.concatenate([y1, y2, y3])  # yを統合

# GridSpecを作成
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 0.1])  # 2行3列のグラフを作成

# プロット領域を作成
fig = plt.figure(figsize=(12, 10))  # グラフのサイズを指定

ax1 = plt.subplot(gs[0, 0])  # 左上のプロット領域を作成
ax2 = plt.subplot(gs[0, 1])  # 右上のプロット領域を作成
ax3 = plt.subplot(gs[1, 0])  # 左下のプロット領域を作成
cbar_ax = plt.subplot(gs[1, 2])  # カラーバーのプロット領域を作成

# 左側のサブプロットに統合データの散布図をプロット
ax1.scatter(x, y, alpha=1)  # 散布図を描画
ax1.set_xlabel('X')  # x軸ラベル
ax1.set_ylabel('Y')  # y軸ラベル

# 中央のサブプロットに統合データの半透明なマーカー散布図をプロット
ax2.scatter(x, y, alpha=0.2)  # 散布図を描画
ax2.set_xlabel('X')  # x軸ラベル
ax2.set_ylabel('Y')  # y軸ラベル

# 右側のサブプロットに統合データのヒートマップをプロット
heatmap, xedges, yedges = np.histogram2d(x, y, bins=20)  # 2次元ヒストグラムを計算
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]  # ヒストグラムの範囲を取得
im = ax3.imshow(heatmap.T, origin='lower', extent=extent, aspect='auto', cmap='jet')  # ヒートマップを描画
ax3.set_xlabel('X')  # x軸ラベル
ax3.set_ylabel('Y')  # y軸ラベル

# カラーバーを描画
fig.colorbar(im, cax=cbar_ax)  # カラーバーを描画
cbar_ax.set_ylabel('頻度', fontsize=20)  # カラーバーのラベルを設定

# サブプロット間のスペースを調整
plt.tight_layout()  # レイアウトの設定
plt.savefig('3_3_5_scatter_variations.png', dpi=300)  # 画像として保存
plt.show()  # グラフを表示
