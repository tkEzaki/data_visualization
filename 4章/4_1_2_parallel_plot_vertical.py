from sklearn.datasets import load_wine
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore
import numpy as np
import japanize_matplotlib

plt.rcParams["font.size"] = 14

# Wineデータセットのロード
wine = load_wine()

# データフレームの作成
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df = df.apply(zscore)  # z-score normalization

df['target'] = wine.target

# ターゲット（クラスラベル）を文字列に変換
df['target'] = df['target'].map({0: '品種1', 1: '品種2', 2: '品種3'})

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
    'プロリン',
    'target'
]

# クラスごとに色を設定
colors = {'品種1': 'gray', '品種2': 'gold', '品種3': 'blue'}

# プロットの設定
plt.figure(figsize=(7, 10))

# クラスごとに線を描画
for idx, row in df.iterrows():
    plt.plot(row[:-1].values, range(len(df.columns) - 1), c=colors[row['target']], alpha=0.5)

# y軸の設定
plt.yticks(range(len(df.columns) - 1), df.columns[:-1])

plt.xlabel('相対スコア')
# グリッドを表示
plt.grid(True, which='both', axis='both')

plt.tight_layout()
plt.savefig('4_1_2_parallel_plot_vertical.png', dpi=300)
plt.savefig('4_1_2_parallel_plot_vertical.svg', dpi=300)

plt.show()
