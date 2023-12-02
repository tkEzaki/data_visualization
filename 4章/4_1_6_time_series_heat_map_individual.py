import pandas as pd  # データフレーム操作のためのPandas
import seaborn as sns  # グラフ作成のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
from matplotlib import cm  # カラーマップのためのMatplotlib
from matplotlib.colors import ListedColormap  # カラーマップのためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams['font.size'] = 14  # プロットのフォントサイズを14に設定

# CSVデータを読み込む
df = pd.read_csv("data\\behavior_data.csv")

# Time列を秒から時間に変換
df['Time'] = df['Time'].div(3600)

# 各行動に対するDataFrameを作成
actions = ['Other', 'Nest', 'Toilet', 'Garbage']  # 行動のリスト
df_actions = pd.DataFrame(0, index=df['Time'], columns=actions)  # 初期化時に0を設定

df.set_index('Time', inplace=True)  # Time列をインデックスに設定

# 各行動が発生しているときはそれぞれ異なる数値を設定
for i, action in enumerate(actions):
    df_actions[action] = 0
    df_actions.loc[df[df['J'] == action].index, action] = i + 1

# 列名を日本語に変更
column_dict = {
    'Other': '一般の部屋',
    "Nest": '寝室',
    "Toilet": "トイレ",
    "Garbage": 'ゴミ捨て場'
}
df_actions = df_actions.rename(columns=column_dict)  # 列名を日本語に変更
actions = column_dict.values()  # 列名のリストを取得

# Tab10 colormapの最初の4色を取得
tab10_colors = plt.get_cmap('tab10', 10).colors

# 個々のカテゴリに対応する色の辞書
color_dict = {
    '一般の部屋': tab10_colors[0],
    '寝室': tab10_colors[1],
    'トイレ': tab10_colors[2],
    'ゴミ捨て場': tab10_colors[3]
}

# 各行動に対応する色を取得
action_colors = [color_dict[action] for action in actions]  # 各行動に対応する色を取得
new_cmap = ListedColormap(['white'] + action_colors)  # カラーマップを作成

# ヒートマップのプロット
fig, axs = plt.subplots(1, 2, figsize=(8, 11))  # 1行2列のサブプロット

# 全体のヒートマップを描画
sns.heatmap(df_actions, cmap=new_cmap, cbar=False, ax=axs[0])  # ヒートマップを描画
axs[0].set_xlabel('')  # x軸のラベルを削除
axs[0].set_ylabel('時間 [h]')  # y軸のラベルを設定
axs[0].set_xticklabels(actions, rotation=30, ha='right')  # x軸の目盛りラベルを設定
axs[0].set_yticks(np.arange(0, df_actions.shape[0] * 25 /
                  24, df_actions.shape[0] / 24))  # y軸の目盛りを設定
axs[0].set_yticklabels(np.arange(25))  # y軸の目盛りラベルを設定

# 拡大図のヒートマップを描画
df_actions_zoomed = df_actions.loc[(df_actions.index >= 13) & (
    df_actions.index <= 16)]  # 13時から16時までを抽出
sns.heatmap(df_actions_zoomed, cmap=new_cmap,
            cbar=False, ax=axs[1])  # ヒートマップを描画
axs[1].set_xlabel('')  # x軸のラベルを削除
axs[1].set_ylabel('時間 [h]')  # y軸のラベルを設定
axs[1].set_xticklabels(actions, rotation=30, ha='right')  # x軸の目盛りラベルを設定
axs[1].set_yticks(np.arange(0, df_actions_zoomed.shape[0] *
                  4 / 3, (df_actions_zoomed.shape[0]) / 3))  # y軸の目盛りを設定
axs[1].set_yticklabels([13, 14, 15, 16])  # y軸の目盛りラベルを設定

# 枠線の追加
for ax in axs:
    for _, spine in ax.spines.items():
        spine.set_visible(True)

plt.tight_layout()  # レイアウトの調整
plt.savefig("4_1_6_time_series_heat_map_individual.png", dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
