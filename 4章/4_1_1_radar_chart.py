import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
import japanize_matplotlib

# データの定義
# compelling data
data = pd.DataFrame({
    "person": ['Aさん', 'Bさん'],
    "数学": [5, 5],
    "国語": [5, 1],
    "理科": [1, 5],
    "社会": [1, 1],
    "体育": [1, 5],
    "音楽": [5, 1],
})

# overwhelming data
# data = pd.DataFrame({
#     "person": ['Aさん', 'Bさん'],
#     "数学": [5, 2],
#     "国語": [5, 3],
#     "理科": [5, 4],
#     "社会": [4, 3],
#     "体育": [4, 4],
#     "音楽": [5, 2],
# })


# 科目の順序のリストを定義します。
categories1 = ["数学", "国語", "理科", "社会", "体育", "音楽"]
categories2 = ["音楽", "数学", "理科", "体育", "社会", "国語"]  # 順序を変えたリスト
color_list = ["lightblue", "lightcoral"]  # 塗りつぶし色の指定

# サブプロットを作成
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5),
                       subplot_kw=dict(polar=True))

# 各サブプロットについてループ処理を行う
for i, categories in enumerate([categories1, categories2]):

    # 各カテゴリを等間隔に配置し、最初のカテゴリを閉じた円形のチャートを作成するために、再度追加します
    angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
    angles += angles[:1]

    # 各値の最大値を定義
    max_val = 5

    # レーダーチャートに目盛り線を追加
    plt.subplot(1, 2, i + 1, polar=True)
    plt.xticks(angles[:-1], categories, color='grey', size=15)  # フォントサイズを大きく
    plt.yticks(np.arange(1, max_val), [str(i) for i in range(1, max_val)], color="grey", size=14)  # フォントサイズを大きく
    plt.ylim(0, max_val)

    # 各人物のデータについてループ処理
    for index, row in data.iterrows():
        values = row[categories].values.flatten().tolist()
        values += values[:1]
        plt.plot(angles, values, linewidth=1, linestyle='solid', label=row['person'])
        plt.fill(angles, values, color_list[index], alpha=0.2)  # 塗りつぶし色を変更

# レイアウトの間隔を広くする
plt.tight_layout(pad=5)

# 描画
# plt.savefig('4_1_1_2_radar_chart_compelling.png')
plt.savefig('4_1_1_2_radar_chart_compelling.svg')
# plt.savefig('4_1_1_1_radar_chart_overwhelming.png')
# plt.savefig('4_1_1_1_radar_chart_overwhelming.svg')


plt.show()
