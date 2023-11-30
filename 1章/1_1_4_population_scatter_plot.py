import matplotlib.pyplot as plt  # matplotlib.pyplotをpltとしてインポート
import pandas as pd  # pandasをpdとしてインポート
import seaborn as sns  # seabornをsnsとしてインポート
import japanize_matplotlib  # matplotlibで日本語を使用するためのライブラリ

plt.rcParams["font.size"] = 14  # グラフのフォントサイズを設定

# データを辞書形式で提供
data = {
    'year': list(range(1990, 2023)),  # 年（1990年から2022年まで）
    'population': [1.23611, 1.24101, 1.24567, 1.24938, 1.25265, 1.2557, 1.25859, 1.26157, 1.26472, 1.26667,
                   1.26926, 1.27316, 1.27486, 1.27694, 1.27787, 1.27768, 1.27901, 1.28033, 1.28084, 1.28032,
                   1.28057, 1.27834, 1.27593, 1.27414, 1.27237, 1.27095, 1.27042, 1.26919, 1.26749, 1.26555,
                   1.26146, 1.25502, 1.24947]  # 人口（億人単位）
}

df = pd.DataFrame(data)  # pandasデータフレームにデータを変換

# 散布図の作成
# 現在の年と次の年の人口を保持する新しいDataFrameを作成
df_shifted = df.copy()
df_shifted['next_year_population'] = df_shifted['population'].shift(-1)  # 次の年の人口列を追加
df_shifted = df_shifted[:-1]  # 最後の行を削除（次の年の値がないため）

plt.figure(figsize=(5, 5))  # グラフのサイズを指定
sns.scatterplot(x='population', y='next_year_population', data=df_shifted)  # 散布図の描画
plt.xlim(1.23, 1.29)  # x軸の範囲設定
plt.ylim(1.23, 1.29)  # y軸の範囲設定
plt.xlabel('ある年の日本の総人口 [億人]')  # x軸のラベル
plt.ylabel('次の年の日本の総人口 [億人]')  # y軸のラベル
plt.grid(True)  # グリッドを表示
plt.tight_layout()  # レイアウトの調整
plt.savefig('1_1_4_population_scatter_plot.png', dpi=300)  # グラフをファイルに保存
plt.show()  # グラフの表示
