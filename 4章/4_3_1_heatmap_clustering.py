import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from sklearn.datasets import load_wine  # ワインデータセット
import pandas as pd  # データフレーム操作のためのPandas
from scipy.stats import zscore  # Zスコア正規化のための関数
import seaborn as sns  # グラフ作成のためのSeaborn
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams['font.size'] = 14  # プロットのフォントサイズを14に設定

# Wineデータセットのロード
wine = load_wine()

# データフレームの作成
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df = df.apply(zscore)  # Zスコア正規化

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
g = sns.clustermap(
    df.transpose(), method='ward',
    metric='euclidean', cmap='jet', figsize=(10, 6),
    cbar_pos=(0.02, 0.78, 0.05, 0.2),
    cbar_kws={'ticks': [-3, 0, 3], 'label': '相対スコア'},
    dendrogram_ratio=(0.1, 0.3)
)  # ヒートマップを描画


# y軸ラベルの回転を解除
plt.setp(g.ax_heatmap.get_yticklabels(), rotation=0)

# x軸のラベルを非表示
plt.setp(g.ax_heatmap.get_xticklabels(), visible=False)  # x軸のラベルを非表示
g.ax_heatmap.set_xticks([])  # x軸の目盛りを非表示

# カラーバーを左側に表示
g.cax.yaxis.set_ticks_position('left')  # カラーバーの位置を左側に指定
g.cax.yaxis.set_label_position('left')  # カラーバーのラベルを左側に指定

# ヒートマップに枠を追加
g.ax_heatmap.axhline(y=0, color='k', linewidth=1)
g.ax_heatmap.axhline(y=df.shape[1], color='k', linewidth=1)
g.ax_heatmap.axvline(x=0, color='k', linewidth=1)
g.ax_heatmap.axvline(x=df.shape[0], color='k', linewidth=1)


plt.tight_layout()  # レイアウトの調整
plt.savefig('4_3_1_heatmap_clustering.png', dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
