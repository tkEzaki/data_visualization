import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from sklearn.datasets import load_wine  # ワインデータセット
import pandas as pd  # データフレーム操作のためのPandas
from scipy.stats import zscore  # Zスコア正規化
import numpy as np  # 数値演算のためのNumPy
import matplotlib.patches as mpatches  # 図形描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams['font.size'] = 14  # プロットのフォントサイズを14に設定

# Wineデータセットのロード
wine = load_wine()

# データフレームの作成
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df = df.apply(zscore)  # Zスコア正規化

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
fig, ax = plt.subplots(figsize=(9, 6))  # サブプロットの作成
im = ax.imshow(df.transpose(), aspect='auto', cmap='jet')  # ヒートマップを描画

# カテゴリの色を設定
colors = {'品種1': 'gray', '品種2': 'gold', '品種3': 'blue'}
color_map = [colors[target] for target in target_names]

# バーコードを追加
ax2 = fig.add_axes([0.092, 0.88, 0.7175, 0.025])  # サブプロットの作成
for sp in ax2.spines.values():
    sp.set_visible(False)  # 枠線を非表示に

ax2.tick_params(left=False, bottom=False)  # 目盛りを非表示に
ax2.set_xticks(np.arange(len(color_map)))  # x軸の目盛りを設定
ax2.set_yticks([])  # y軸の目盛りを非表示に
ax2.set_xticklabels([''] * len(color_map))  # x軸の目盛りラベルを設定
ax2.bar(range(len(color_map)), [1] *
        len(color_map), color=color_map, width=1.0)  # バーコードを描画

ax.set_xlabel('ワイン銘柄番号')  # x軸ラベル

ax.yaxis.set_ticks_position('both')  # y軸の目盛りを両側に表示
ax.yaxis.set_tick_params(length=0)  # y軸の目盛り線を非表示に

plt.colorbar(im, ax=ax, label='相対スコア', pad=0.01)  # カラーバーを描画
ax.set_yticks(range(df.shape[1]))  # y軸の目盛りを設定
ax.set_yticklabels(df.columns, fontsize=14)  # y軸の目盛りラベルを設定

plt.savefig('4_1_4_heatmap.png', bbox_inches='tight',
            pad_inches=0.1, dpi=300)  # 画像を保存
plt.show()  # 画面に表示
