import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# 乱数のシード値を設定
np.random.seed(0)

# ランダムな体重データを生成
weights_1 = np.random.normal(60, 2, 50)  # 平均60、分散10の正規分布
weights_2 = weights_1 + np.random.normal(-1, 0.5, 50)  # 平均-1、分散0.5の正規分布

# データフレームを作成
df1 = pd.DataFrame({'Weight': weights_1, 'Group': ['実験開始時'] * 50, 'Person': np.arange(50)})
df2 = pd.DataFrame({'Weight': weights_2, 'Group': ['一か月後'] * 50, 'Person': np.arange(50)})
df = pd.concat([df1, df2])

# 図の描画
fig, axes = plt.subplots(1, 3, figsize=(10, 5))

# スロープグラフ（線なし、固定色）
axes[0].scatter([0.25] * 50, weights_1, color='gray', alpha=0.5)
axes[0].scatter([0.75] * 50, weights_2, color='gray', alpha=0.5)
# axes[0].set_title('Slope graph without lines')
axes[0].set_xticks([0.25, 0.75])
axes[0].set_xticklabels(['実験開始時', '一か月後'], fontsize=14)
axes[0].set_xlim([0, 1])
axes[0].set_ylabel('体重 [kg]')
# スロープグラフ
differences = weights_2 - weights_1
cmap = cm.get_cmap('coolwarm')
norm = colors.Normalize(-2, 2)  # 正規化を作成
for i in range(50):
    axes[2].plot([0.25, 0.75], [weights_1[i], weights_2[i]], marker='o', color=cmap(norm(differences[i])), alpha=0.5)
# axes[1].set_title('Slope graph')
axes[2].set_xticks([0.25, 0.75])
axes[2].set_xticklabels(['実験開始時', '一か月後'], fontsize=14)
axes[2].set_xlim([0, 1])

# スロープグラフ（ランダム）
np.random.shuffle(weights_2)
differences = weights_2 - weights_1
for i in range(50):
    axes[1].plot([0.25, 0.75], [weights_1[i], weights_2[i]], marker='o', color=cmap(norm(differences[i])), alpha=0.5)
# axes[2].set_title('Slope graph (shuffled)')
axes[1].set_xticks([0.25, 0.75])
axes[1].set_xticklabels(['実験開始時', '一か月後'], fontsize=14)
axes[1].set_xlim([0, 1])

fig.subplots_adjust(right=0.85)  # プロットエリアを狭めてカラーバーにスペースを作る
cbar_ax = fig.add_axes([0.9, 0.15, 0.02, 0.7])  # カラーバーの位置とサイズを指定
cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), cax=cbar_ax)
cbar.set_label('差 [kg]')
plt.savefig('3_2_3_slope.png', dpi=300)
plt.savefig('3_2_3_slope.svg', dpi=300)

plt.show()
