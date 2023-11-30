import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_wine
from scipy.stats import zscore
import japanize_matplotlib

plt.rcParams["font.size"] = 15

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

# フォント設定
plt.rcParams['font.family'] = 'Yu Gothic'

# データセット
data = df.melt(id_vars='target', value_vars=['アルコール度数',
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
                                             'プロリン'], var_name='', value_name='value')

# サブプロットの設定
fig, axs = plt.subplots(2, 1, figsize=(10, 14))

ylim_info_0 = (-1.55394967369141, 1.4988994568029632)
ylim_info_1 = (-5.164243574086434, 5.876217066266364)

# 交互に色を変える
for i in range(len(wine.feature_names)):
    if i % 2 == 0:
        axs[0].fill_between([i - 0.5, i + 0.5], *ylim_info_0, color='yellow', alpha=0.1)
        axs[1].fill_between([i - 0.5, i + 0.5], *ylim_info_1, color='yellow', alpha=0.1)


# 集団棒グラフ
sns.barplot(x='', y='value', hue='target', data=data, ax=axs[0], palette=['gray', 'gold', 'blue'])
axs[0].get_legend().remove()  # 凡例非表示
axs[0].set_ylabel('相対スコア')  # y軸ラベル非表示


# バイオリンプロット
sns.violinplot(x='', y='value', hue='target', data=data, ax=axs[1], palette=['gray', 'gold', 'blue'])
axs[1].get_legend().remove()  # 凡例非表示
axs[1].set_ylabel('相対スコア')  # y軸ラベル非表示
axs[1].legend(loc='lower right', ncol=3)

axs[0].set_ylim(*ylim_info_0)
axs[1].set_ylim(*ylim_info_1)

# ラベルの回転
for ax in axs:
    plt.sca(ax)
    plt.xticks(rotation=15, ha='right')

# サブプロット間のスペース調整
plt.subplots_adjust(hspace=0.4)

plt.tight_layout(pad=2.0)  # Increase padding
plt.savefig('4_1_3_group_bar_violin_chart.png', dpi=300)
plt.savefig('4_1_3_group_bar_violin_chart.svg', dpi=300)

plt.show()
