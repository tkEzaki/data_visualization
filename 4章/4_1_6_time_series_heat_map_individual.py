import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# 仮のCSVデータを読み込む（この部分は実際のCSVファイルを読み込むように変更してください）
df = pd.read_csv("behavior_data.csv")

# Time列を秒から時間に変換
df['Time'] = df['Time'].div(3600)

# 各行動に対するDataFrameを作成
actions = ['Other', 'Nest', 'Toilet', 'Garbage']
df_actions = pd.DataFrame(0, index=df['Time'], columns=actions)  # 初期化時に0を設定

df.set_index('Time', inplace=True)

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
new_cmap = ListedColormap(['white'] + action_colors)

fig, axs = plt.subplots(1, 2, figsize=(8, 11))  # 1行2列のサブプロット

# 全体のヒートマップを描画
sns.heatmap(df_actions, cmap=new_cmap, cbar=False, ax=axs[0])
axs[0].set_xlabel('')
axs[0].set_ylabel('時間 [h]')
axs[0].set_xticklabels(actions, rotation=30, ha='right')
axs[0].set_yticks(np.arange(0, df_actions.shape[0] * 25 / 24, df_actions.shape[0] / 24))
axs[0].set_yticklabels(np.arange(25))

# 部分的なヒートマップを描画
df_actions_zoomed = df_actions.loc[(df_actions.index >= 13) & (df_actions.index <= 16)]
sns.heatmap(df_actions_zoomed, cmap=new_cmap, cbar=False, ax=axs[1])
axs[1].set_xlabel('')
axs[1].set_ylabel('時間 [h]')
axs[1].set_xticklabels(actions, rotation=30, ha='right')
axs[1].set_yticks(np.arange(0, df_actions_zoomed.shape[0] * 4 / 3, (df_actions_zoomed.shape[0]) / 3))
axs[1].set_yticklabels([13, 14, 15, 16])

# Add lines to the border of the heatmap for both subplots
for ax in axs:
    for _, spine in ax.spines.items():
        spine.set_visible(True)

plt.subplots_adjust(wspace=0.5)
plt.tight_layout()
plt.savefig("4_1_6_time_series_heat_map_individual.png", dpi=300)
plt.savefig("4_1_6_time_series_heat_map_individual.svg", dpi=300)

plt.show()
