import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap
import japanize_matplotlib

plt.rcParams['font.size'] = 16

# 仮のCSVデータを読み込む（この部分は実際のCSVファイルを読み込むように変更してください）
df = pd.read_csv("behavior_data.csv")

# Time列を秒から時間に変換します。
df['Time'] = df['Time'].div(3600).round(2)  # 3600で割って、小数点第二位まで表示

# ヒートマップの作成
# ここでは、各個体の行動をカテゴリ変数として扱うために数値に変換します。
categories = df.iloc[:, 1:].stack().unique()
df.replace(categories, range(len(categories)), inplace=True)

# データの転置は行わない
# df.set_index('Time', inplace=True)
# df = df.T

# Tab10 colormapの最初の4色を取得
tab10_colors = plt.get_cmap('tab10', 10).colors

# 個々のカテゴリに対応する色の辞書
color_dict = {'Nest': tab10_colors[1],
              'Toilet': tab10_colors[2],
              'Garbage': tab10_colors[3],
              'Other': tab10_colors[0]
              }

# categoriesリスト内の各要素に対応する色を取得
category_colors = [color_dict[cat] for cat in categories]
n_categories = len(categories)

# カラーマップを作成
new_cmap = ListedColormap(category_colors)

# ヒートマップのプロット
fig, ax = plt.subplots(figsize=(8, 11))
sns.heatmap(df.set_index('Time'), cmap=new_cmap, ax=ax, 
            cbar_kws={"boundaries": np.linspace(-0.5, n_categories - 0.5, n_categories + 1), "ticks": [], "shrink": 0.5})

# yticksを1時間ごとに設定します。
yticks_locations = np.arange(0, len(df['Time']), 360)  # 1時間=3600秒なので3600をタイムステップ（10秒）で割る
yticks_labels = df['Time'].iloc[::360].astype(int)  # 1時間ごとのラベル
plt.yticks(yticks_locations, labels=yticks_labels, rotation=0)

# ヒートマップの各列間に線を引く
for x in range(df.shape[1] - 1):  # -1 は 'Time' 列を除くため
    plt.vlines(x, ymin=0, ymax=df.shape[0], color='black', linewidth=0.5)

# 枠線の追加
for _, spine in ax.spines.items():
    spine.set_visible(True)

plt.ylabel('時間 [h]')
plt.xlabel('個体')
plt.tight_layout()
plt.savefig("4_1_5_time_series_heat_map_flipped.png", dpi=300)
plt.savefig("4_1_5_time_series_heat_map_flipped.svg", dpi=300)

plt.show()
