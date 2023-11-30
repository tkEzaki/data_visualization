import numpy as np  # 数値計算のためのNumPy
import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from math import pi  # 円周率πのため
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

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
                       subplot_kw=dict(polar=True))  # polar=Trueで極座標になる

# 各サブプロットについてループ処理を行う
for i, categories in enumerate([categories1, categories2]):

    # 各カテゴリを等間隔に配置し、最初のカテゴリを閉じた円形のチャートにする
    angles = [n / float(len(categories)) * 2 *
              pi for n in range(len(categories))]  # 角度を計算
    angles += angles[:1]  # 閉じた円形にするために、最初のカテゴリを追加

    # 各値の最大値を定義
    max_val = 5

    plt.subplot(1, 2, i + 1, polar=True)  # サブプロットを追加
    plt.xticks(angles[:-1], categories, color='grey', size=15)  # x軸のラベルを追加
    plt.yticks(np.arange(1, max_val), [str(i) for i in range(
        1, max_val)], color="grey", size=14)  # y軸の目盛りを追加
    plt.ylim(0, max_val)  # y軸の範囲を設定

    # 各人物のデータについて描画を行なう
    for index, row in data.iterrows():
        values = row[categories].values.flatten().tolist()  # 値を取得
        values += values[:1]  # 閉じた円形にするために、最初の値を追加
        plt.plot(angles, values, linewidth=1,
                 linestyle='solid', label=row['person'])
        plt.fill(angles, values, color_list[index], alpha=0.2)

# レイアウトの間隔を広くする
plt.tight_layout(pad=5)

# 描画
plt.savefig('4_1_1_2_radar_chart_compelling.png')
# plt.savefig('4_1_1_1_radar_chart_overwhelming.png')
plt.show()  # 画面に表示
