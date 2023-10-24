import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib import cm
import japanize_matplotlib
# pltで日本語フォントを設定
# import matplotlib as mpl
# mpl.rcParams['font.family'] = 'Yu Gothic'

# データの定義
data = {
    '曜日': ['月曜', '火曜', '水曜', '木曜', '金曜', '土曜', '日曜'],
    '売上': [30, 25, 35, 28, 22, 34, 35],
    'カード会員': [20, 13, 20, 14, 14, 20, 25],
    '非会員': [10, 12, 15, 14, 8, 14, 10]
}
df = pd.DataFrame(data)

# カラーマップの設定
cmap = cm.get_cmap('tab10')  # 'tab10'は良く使われるカラーマップの一つ

# 基本的な棒グラフの作成関数


def plot_basic_bar(ax, df):
    ax.bar(df['曜日'], df['売上'], color=cmap(0))
    # ax.set_title('基本的な棒グラフ', fontsize=14)
    ax.tick_params(labelsize=14)
    # set ylabel
    ax.set_ylabel('売上 [万円]', fontsize=14)


def plot_stacked_bar(ax, df):
    ax.bar(df['曜日'], df['カード会員'], label='カード会員', color=cmap(1))
    ax.bar(df['曜日'], df['非会員'], bottom=df['カード会員'], label='非会員', color=cmap(2))
    # ax.set_title('積み上げ棒グラフ', fontsize=14)
    # ax.legend()
    ax.set_ylabel('売上 [万円]', fontsize=14)
    ax.tick_params(labelsize=14)

# 水平棒グラフの作成関数


def plot_horizontal_bar(ax, df):
    bar_width = 0.35
    index = pd.Index(sorted([7, 6, 5, 4, 3, 2, 1]))  # x軸の値
    ax.barh(index - bar_width / 2, df['カード会員'], bar_width, label='カード会員', color=cmap(1))
    ax.barh(index + bar_width / 2, df['非会員'], bar_width, label='非会員', color=cmap(2))
    # ax.set_title('水平棒グラフ', fontsize=14)
    ax.set_yticks(index)
    ax.set_yticklabels(df['曜日'])
    ax.set_xlabel('売上 [万円]', fontsize=14)
    ax.legend(fontsize=14)
    ax.tick_params(labelsize=14)


# GridSpecの設定
gs = GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1])

# サブプロットの作成
fig = plt.figure(figsize=(10, 8))
ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])
ax2 = plt.subplot(gs[2:])

# 各サブプロットへのプロット関数の呼び出し
plot_basic_bar(ax0, df)
plot_stacked_bar(ax1, df)
plot_horizontal_bar(ax2, df)

# サブプロット間の間隔調整
plt.subplots_adjust(wspace=0.3, hspace=0.3)


# グラフの表示
# plt.show()
plt.savefig('2_2_1_bar_charts.png', dpi=300)
plt.savefig('2_2_1_bar_charts.svg')
