import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import matplotlib.colors as mcolors  # カラーマップを利用するためのライブラリ
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

# パーセンテージのデータ
data = [40, 32, 25, 3]

# ラベル
labels = ['支持する', '支持しない', 'どちらとも\nいえない', '無回答']

# 各ラベルに対応する色
colors = ['blue', 'red', 'lightgray', 'gray']

# データとラベルと色を大きい順にソート
data, labels, colors = zip(*sorted(zip(data, labels, colors), reverse=True))

# 色の彩度を下げる
colors = [mcolors.to_rgba(color, alpha=0.6) for color in colors]

# ドーナツチャートの描画
plt.figure(figsize=(6, 6))  # グラフのサイズを指定
plt.pie(data, labels=labels, colors=colors, startangle=90, counterclock=False, wedgeprops=dict(width=0.3), textprops={'fontsize': 20})  # ドーナツチャートを描画
plt.tight_layout()  # レイアウトの調整
plt.savefig("2_1_1_donut.png", dpi=300)  # グラフを画像として保存
plt.show()  # グラフの表示
