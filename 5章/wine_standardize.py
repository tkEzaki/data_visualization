import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_wine
from scipy.stats import zscore

# 日本語化用フォント設定
plt.rcParams['font.family'] = 'Yu Gothic'

# Wineデータセットのロード
wine = load_wine()

# オリジナルのデータフレームの作成
original_df = pd.DataFrame(wine.data, columns=wine.feature_names)
original_df['target'] = wine.target
original_df['target'] = original_df['target'].map({0: '品種1', 1: '品種2', 2: '品種3'})

# z-score normalization
df = original_df.copy()
df[df.columns[:-1]] = df[df.columns[:-1]].apply(zscore)

# 日本語列名の設定
columns_jp = [
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
original_df.columns = df.columns = columns_jp

# データセット
original_data = original_df.melt(id_vars='target', var_name='', value_name='元の値')
zscored_data = df.melt(id_vars='target', var_name='', value_name='Zスコア')

# サブプロットの設定
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# オリジナルのスウォームプロット
sns.swarmplot(x='', y='元の値', hue='target', data=original_data, ax=axs[0], palette=['gray', 'gold', 'blue'])
axs[0].get_legend().remove()  # 凡例非表示

# zスコア化したスウォームプロット
sns.swarmplot(x='', y='Zスコア', hue='target', data=zscored_data, ax=axs[1], palette=['gray', 'gold', 'blue'])
axs[1].get_legend().remove()  # 凡例非表示

# ラベルの回転
for ax in axs:
    plt.sca(ax)
    plt.xticks(rotation=15, ha='right')

# サブプロット間のスペース調整
plt.subplots_adjust(hspace=0.4)

plt.tight_layout(pad=2.0)  # Increase padding
plt.savefig('swarm_plot_chart.png', dpi=300)
plt.show()
