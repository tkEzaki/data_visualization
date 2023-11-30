import matplotlib.pyplot as plt  # matplotlibのpyplotをpltとしてインポート
import pandas as pd  # pandasをpdとしてインポート
import seaborn as sns  # seabornをsnsとしてインポート
import japanize_matplotlib  # matplotlibで日本語を表示可能にする

# データを辞書形式で提供
data = {
    'year': list(range(1990, 2023)),  # 年（1990年から2022年まで）
    'population': [1.23611, 1.24101, 1.24567, 1.24938, 1.25265, 1.2557, 1.25859, 1.26157, 1.26472, 1.26667,
                   1.26926, 1.27316, 1.27486, 1.27694, 1.27787, 1.27768, 1.27901, 1.28033, 1.28084, 1.28032,
                   1.28057, 1.27834, 1.27593, 1.27414, 1.27237, 1.27095, 1.27042, 1.26919, 1.26749, 1.26555,
                   1.26146, 1.25502, 1.24947]  # 人口（億人単位）
}

df = pd.DataFrame(data)  # pandasデータフレームにデータを変換

plt.figure(figsize=(5, 3))  # グラフのサイズを指定
sns.lineplot(x='year', y='population', data=df, marker='o', linestyle='-')  # 折れ線グラフの描画

plt.xlabel("西暦")  # x軸のラベル
plt.ylabel("日本の総人口 [億人]")  # y軸のラベル
plt.grid(True)  # グリッドを表示
plt.tight_layout()  # レイアウトの調整
plt.savefig("1_1_3_population_line_plot.png", dpi=300)  # グラフをファイルに保存
plt.show()  # グラフの表示
