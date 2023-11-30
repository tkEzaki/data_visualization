import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from matplotlib.gridspec import GridSpec  # グラフのレイアウト指定のため
from matplotlib import cm  # カラーマップのためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

# データの定義
data = {
    '曜日': ['月曜', '火曜', '水曜', '木曜', '金曜', '土曜', '日曜'],
    '売上': [30, 25, 35, 28, 22, 34, 35],
    'カード会員': [20, 13, 20, 14, 14, 20, 25],
    '非会員': [10, 12, 15, 14, 8, 14, 10]
}
df = pd.DataFrame(data)  # データフレームにデータを格納

# カラーマップの設定
cmap = cm.get_cmap('tab10')  # 'tab10'は良く使われるカラーマップの一つ

# 基本的な棒グラフの作成関数


def plot_basic_bar(ax, df):
    ax.bar(df['曜日'], df['売上'], color=cmap(0))  # 売上の棒グラフを描画
    ax.tick_params(labelsize=14)  # 軸ラベルのフォントサイズを設定
    ax.set_ylabel('売上 [万円]', fontsize=14)  # y軸ラベルを設定


# 積み上げ棒グラフの作成関数
def plot_stacked_bar(ax, df):
    ax.bar(df['曜日'], df['カード会員'], label='カード会員',
           color=cmap(1))  # カード会員の棒グラフを描画
    ax.bar(df['曜日'], df['非会員'], bottom=df['カード会員'],
           label='非会員', color=cmap(2))  # 非会員の棒グラフを描画
    ax.set_ylabel('売上 [万円]', fontsize=14)  # y軸ラベルを設定
    ax.tick_params(labelsize=14)  # 軸ラベルのフォントサイズを設定


# 水平棒グラフの作成関数
def plot_horizontal_bar(ax, df):
    bar_width = 0.35  # 棒の幅
    index = pd.Index(sorted([7, 6, 5, 4, 3, 2, 1]))  # x軸の値
    ax.barh(index - bar_width / 2, df['カード会員'], bar_width,
            label='カード会員', color=cmap(1))  # カード会員の棒グラフを描画
    ax.barh(index + bar_width / 2,
            df['非会員'], bar_width, label='非会員', color=cmap(2))  # 非会員の棒グラフを描画
    ax.set_yticks(index)  # y軸の目盛りを設定
    ax.set_yticklabels(df['曜日'])  # y軸の目盛りラベルを設定
    ax.set_xlabel('売上 [万円]', fontsize=14)  # x軸ラベルを設定
    ax.legend(fontsize=14)  # 凡例の表示
    ax.tick_params(labelsize=14)  # 軸ラベルのフォントサイズを設定


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

plt.subplots_adjust(wspace=0.3, hspace=0.3)  # サブプロット間の余白を調整
plt.savefig('2_2_1_bar_charts.png', dpi=300)  # 画像として保存
plt.show()  # 画面に表示
