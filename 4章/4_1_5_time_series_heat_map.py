import pandas as pd  # データフレーム操作のためのPandas
import seaborn as sns  # グラフ作成のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
from matplotlib import cm  # カラーマップのためのMatplotlib
from matplotlib.colors import ListedColormap  # カラーマップのためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams['font.size'] = 16  # プロットのフォントサイズを16に設定

# CSVデータを読み込む
df = pd.read_csv("data\\behavior_data.csv")

# Time列を秒から時間に変換
df['Time'] = df['Time'].div(3600).round(2)  # 3600で割って、小数点第二位まで表示

# ヒートマップの作成
# 各個体の行動をカテゴリ変数として扱うために数値に変換
categories = df.iloc[:, 1:].stack().unique()  # カテゴリのリストを取得
df.replace(categories, range(len(categories)), inplace=True)  # カテゴリを数値に変換

# Tab10 colormapの最初の4色を取得
tab10_colors = plt.get_cmap('tab10', 10).colors

# 個々のカテゴリに対応する色の辞書
color_dict = {
    'Nest': tab10_colors[1],
    'Toilet': tab10_colors[2],
    'Garbage': tab10_colors[3],
    'Other': tab10_colors[0]
}

# categoriesリスト内の各要素に対応する色を取得
category_colors = [color_dict[cat] for cat in categories]  # カテゴリに対応する色のリストを作成
n_categories = len(categories)  # カテゴリ数を取得

# カラーマップを作成
new_cmap = ListedColormap(category_colors)

# ヒートマップのプロット
fig, ax = plt.subplots(figsize=(8, 11))  # サブプロットの作成
sns.heatmap(df.set_index('Time'), cmap=new_cmap, ax=ax,
            cbar_kws={"boundaries": np.linspace(-0.5, n_categories - 0.5, n_categories + 1),
                      "ticks": [], "shrink": 0.5})  # ヒートマップを描画

# 1時間=3600秒なので3600をタイムステップ（10秒）で割る
yticks_locations = np.arange(0, len(df['Time']), 360)  # 1時間ごとの位置
yticks_labels = df['Time'].iloc[::360].astype(int)  # 1時間ごとのラベル

plt.yticks(yticks_locations, labels=yticks_labels, rotation=0)  # y軸の目盛りを設定

# ヒートマップの各列間に線を引く
for x in range(df.shape[1] - 1):  # -1 は 'Time' 列を除くため
    plt.vlines(x, ymin=0, ymax=df.shape[0], color='black', linewidth=0.5)

# 枠線の追加
for _, spine in ax.spines.items():
    spine.set_visible(True)

plt.ylabel('時間 [h]')  # y軸のラベル
plt.xlabel('個体')  # x軸のラベル
plt.tight_layout()  # レイアウトの調整
plt.savefig("4_1_5_time_series_heat_map_flipped.png", dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
