import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
import pandas as pd
from scipy.stats import zscore
import numpy as np
import matplotlib.patches as mpatches

plt.rcParams['font.family'] = 'Yu Gothic'

# Wineデータセットのロード
wine = load_wine()

# データフレームの作成
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df = df.apply(zscore)  # z-score normalization

# targetに名前を付ける
target_names = np.array(['品種1', '品種2', '品種3'])[wine.target]

# 列名を日本語に変更
df.columns = [
    'アルコール度数',
    'リンゴ酸',
    'ミネラル分',
    'ミネラル分のアルカリ度',
    'マグネシウム',
    '全フェノール類',
    'フラバノイド',
    '非フラバノイドフェノール類',
    'プロアントシアニン',
    '色の強さ',
    '色相',
    'OD280/OD315値',
    'プロリン'
]

# ヒートマップの描画
fig, ax = plt.subplots(figsize=(9, 6))
im = ax.imshow(df.transpose(), aspect='auto', cmap='jet')

# カテゴリの色を設定
colors = {'品種1': 'gray', '品種2': 'gold', '品種3': 'blue'}
color_map = [colors[target] for target in target_names]

# Create legend
# patches = [mpatches.Patch(color=colors[key], label=key) for key in colors]
# plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# バーコードを追加
ax2 = fig.add_axes([0.092, 0.88, 0.7175, 0.025])
for sp in ax2.spines.values():
    sp.set_visible(False)
ax2.tick_params(left=False, bottom=False)
ax2.set_xticks(np.arange(len(color_map)))
ax2.set_yticks([])
ax2.set_xticklabels([''] * len(color_map))
ax2.bar(range(len(color_map)), [1] * len(color_map), color=color_map, width=1.0)

# ax.yaxis.tick_right()
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_tick_params(length=0)

plt.colorbar(im, ax=ax, label='', pad=0.01)
ax.set_yticks(range(df.shape[1]))
ax.set_yticklabels(df.columns, fontsize=10)
# ax.set_xlabel('Samples')
# ax.set_ylabel('Features')
# plt.title('Heatmap of wine data (z-score normalized)', pad=100)
plt.savefig('heatmap.png', bbox_inches='tight', pad_inches=0.1, dpi=300)
plt.show()
