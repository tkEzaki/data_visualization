import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap

plt.rcParams['font.family'] = 'Yu Gothic'

df = pd.read_csv("behavior_data.csv")


# 個体"J"のデータのみを選択
df = df[["Time", "J"]]

# Time列を秒から時間に変換
df['Time'] = df['Time'].div(3600)

# 各行動に対するDataFrameを作成
actions = ['Other', 'Nest', 'Toilet', 'Garbage']
df_actions = pd.DataFrame(0, index=df['Time'], columns=actions)  # 初期化時に0を設定

df.set_index('Time', inplace=True)
print(df)
# 各行動が発生しているときはそれぞれ異なる数値を設定
for i, action in enumerate(actions):
    df_actions[action] = 0
    df_actions.loc[df[df['J'] == action].index, action] = i + 1

column_dict = {
    'Other': '一般の部屋',
    "Nest": '寝室',
    "Toilet": "トイレ",
    "Garbage": 'ゴミ捨て場'
}

df_actions = df_actions.rename(columns=column_dict)
actions = column_dict.values()
print(actions)

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
action_colors = [color_dict[action] for action in actions]

# ヒートマップの背景色を白に設定するためにカラーマップを作成
new_cmap = ListedColormap(['white'] + action_colors)

fig, axs = plt.subplots(2, 1, figsize=(9, 6))

# 全体のヒートマップを描画
sns.heatmap(df_actions.T, cmap=new_cmap, cbar=False, ax=axs[0])
axs[0].set_xlabel('時間 [h]')
axs[0].set_ylabel('')
axs[0].set_yticklabels(actions, rotation=0)
axs[0].set_xticks(np.arange(0, df_actions.shape[0] * 25 / 24, df_actions.shape[0] / 24))  # 追加: x軸の目盛りの位置
axs[0].set_xticklabels(np.arange(25), rotation=0)  # 追加: x軸の目盛りのラベル

# Add lines to the border of the heatmap
for _, spine in axs[0].spines.items():
    spine.set_visible(True)

# 部分的なヒートマップを描画
df_actions_zoomed = df_actions.loc[(df_actions.index >= 13) & (df_actions.index <= 16)]
sns.heatmap(df_actions_zoomed.T, cmap=new_cmap, cbar=False, ax=axs[1])
axs[1].set_xlabel('時間 [h]')
axs[1].set_ylabel('')
axs[1].set_yticklabels(actions, rotation=0)
axs[1].set_xticks(np.arange(0, df_actions_zoomed.shape[0] * 4 / 3, (df_actions_zoomed.shape[0]) / 3))  # 追加: x軸の目盛りの位置
axs[1].set_xticklabels([13, 14, 15, 16], rotation=0)  # 追加: x軸の目盛りのラベル

# Add lines to the border of the heatmap
for _, spine in axs[1].spines.items():
    spine.set_visible(True)

# plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
plt.savefig("time_series_heat_map_individual.png", dpi=300)
plt.show()
