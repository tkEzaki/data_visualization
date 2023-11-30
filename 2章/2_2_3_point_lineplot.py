import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

# データの生成
np.random.seed(0)  # 乱数のシードを設定（再現性のため）
people = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # 人のリスト
data_evening = {
    '人': people,
    '夕方': np.random.normal(36.0, 0.2, size=7),  # 夕方の体温
}
data_morning = {
    '人': people,
    '早朝': np.random.normal(36.0, 0.2, size=7),  # 早朝の体温
}
df_evening = pd.DataFrame(data_evening)  # データフレームにデータを格納
df_morning = pd.DataFrame(data_morning)  # データフレームにデータを格納

# プロットの設定
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# マーカーのみの折れ線グラフをプロットする関数
def plot_line(ax, df, time_of_day, marker, line=''):
    ax.plot(df['人'], df[time_of_day], marker=marker, linestyle=line, label=time_of_day)  # 折れ線グラフを描画
    ax.set_ylabel('体温 [℃]', fontsize=14)  # y軸ラベルを設定
    ax.tick_params(labelsize=14)  # 軸ラベルのフォントサイズを設定
    ax.legend(fontsize=14)  # 凡例の表示

# マーカーのみの折れ線グラフをプロット
plot_line(axs[0], df_evening, '夕方', 'o')
plot_line(axs[0], df_morning, '早朝', 's')

# マーカーと折れ線のグラフをプロット
plot_line(axs[1], df_evening, '夕方', 'o', '-')
plot_line(axs[1], df_morning, '早朝', 's', '--')

plt.tight_layout()  # レイアウトの設定
plt.savefig('2_2_3_point_lineplot.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示