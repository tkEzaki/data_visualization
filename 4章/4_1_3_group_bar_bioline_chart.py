import seaborn as sns  # グラフ作成のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import pandas as pd  # データフレーム操作のためのPandas
from sklearn.datasets import load_wine  # ワインデータセット
from scipy.stats import zscore  # Zスコア正規化のための関数
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams["font.size"] = 15  # プロットのフォントサイズを15に設定

# Wineデータセットのロード
wine = load_wine()

# データフレームの作成
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df = df.apply(zscore)  # Zスコア正規化
df['target'] = wine.target  # ターゲット（クラスラベル）をデータフレームに追加

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


# データセットの成型
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

ylim_info_0 = (-1.55394967369141, 1.4988994568029632)  # y軸の範囲
ylim_info_1 = (-5.164243574086434, 5.876217066266364)  # y軸の範囲

# 交互に背景色を変える
for i in range(len(wine.feature_names)):
    if i % 2 == 0:  # 偶数
        axs[0].fill_between([i - 0.5, i + 0.5], *ylim_info_0,
                            color='yellow', alpha=0.1)
        axs[1].fill_between([i - 0.5, i + 0.5], *ylim_info_1,
                            color='yellow', alpha=0.1)


# 集団棒グラフ
sns.barplot(x='', y='value', hue='target', data=data,
            ax=axs[0], palette=['gray', 'gold', 'blue'])
axs[0].get_legend().remove()  # 凡例非表示
axs[0].set_ylabel('相対スコア')  # y軸ラベル非表示


# バイオリンプロット
sns.violinplot(x='', y='value', hue='target', data=data,
               ax=axs[1], palette=['gray', 'gold', 'blue'])
axs[1].get_legend().remove()  # 凡例非表示
axs[1].set_ylabel('相対スコア')  # y軸ラベル非表示
axs[1].legend(loc='lower right', ncol=3)  # 凡例表示


axs[0].set_ylim(*ylim_info_0)  # y軸の範囲を設定
axs[1].set_ylim(*ylim_info_1)  # y軸の範囲を設定

# ラベルの回転
for ax in axs:
    plt.sca(ax)  # 現在のサブプロットを設定
    plt.xticks(rotation=15, ha='right')  # x軸ラベルの回転と位置調整

# サブプロット間のスペース調整
# plt.subplots_adjust(hspace=0.4)  # 縦方向のスペースを調整
plt.tight_layout(pad=2.0)  # レイアウトの調整
plt.savefig('4_1_3_group_bar_violin_chart.png', dpi=300)  # 画像を保存
plt.show()  # 画像を表示
