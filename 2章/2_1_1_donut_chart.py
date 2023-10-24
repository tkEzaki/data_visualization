import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import japanize_matplotlib
# 日本語フォントを設定
# plt.rcParams['font.family'] = 'Yu Gothic'

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
# plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops=dict(width=0.3))  # ドーナツチャートを描画
plt.pie(data, labels=labels, colors=colors, startangle=90, counterclock=False, wedgeprops=dict(width=0.3), textprops={'fontsize': 20})  # ドーナツチャートを描画

# plt.title('Donut Chart')  # グラフのタイトルを指定
# plt.show()  # グラフの表示
plt.tight_layout()
plt.savefig("2_1_1_donut.png", dpi=300)  # グラフを画像として保存
plt.savefig("2_1_1_donut.svg")  # グラフを画像として保存
