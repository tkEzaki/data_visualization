import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
import pandas as pd
from scipy.stats import zscore
import seaborn as sns
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# Wineデータセットのロード
wine = load_wine()

# データフレームの作成
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df = df.apply(zscore)  # z-score normalization

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


# クラスタリングしたヒートマップ
g = sns.clustermap(df.transpose(), method='ward',
                   metric='euclidean', cmap='jet', figsize=(10, 6),
                   cbar_pos=(0.02, 0.78, 0.05, 0.2), cbar_kws={'ticks': [-3, 0, 3], 'label': '相対スコア'},
                   dendrogram_ratio=(0.1, 0.3))

# y軸ラベルの回転を解除
plt.setp(g.ax_heatmap.get_yticklabels(), rotation=0)

# x軸のラベルを非表示
plt.setp(g.ax_heatmap.get_xticklabels(), visible=False)
g.ax_heatmap.set_xticks([])
# カラーバーを左側に表示
g.cax.yaxis.set_ticks_position('left')
g.cax.yaxis.set_label_position('left')

# ヒートマップに枠を追加
g.ax_heatmap.axhline(y=0, color='k', linewidth=1)
g.ax_heatmap.axhline(y=df.shape[1], color='k', linewidth=1)
g.ax_heatmap.axvline(x=0, color='k', linewidth=1)
g.ax_heatmap.axvline(x=df.shape[0], color='k', linewidth=1)


# タイトル設定
# plt.title('Clustered Heatmap')

# ファイルに保存
plt.tight_layout()
plt.savefig('4_3_1_heatmap_clustering.png', dpi=300)
plt.savefig('4_3_1_heatmap_clustering.svg', dpi=300)


# プロットの表示
plt.show()
