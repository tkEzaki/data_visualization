from sklearn.datasets import load_wine
import pandas as pd
from pandas.plotting import parallel_coordinates
import matplotlib.pyplot as plt
from scipy.stats import zscore

# 日本語化用フォント設定
plt.rcParams['font.family'] = 'Yu Gothic'

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

# パラレルプロットの作成
plt.figure(figsize=(10, 5))
parallel_coordinates(df, class_column='target', color=['gray', 'gold', 'blue'], alpha=0.5)

# x軸のラベルを45度回転、ラベルの右端が目盛りに合うように調整
plt.xticks(rotation=30, ha='right')

# 横方向の線を消す
plt.gca().yaxis.grid(False)
plt.tight_layout()
plt.savefig('parallel_plot_example.png', dpi=300)
plt.show()
