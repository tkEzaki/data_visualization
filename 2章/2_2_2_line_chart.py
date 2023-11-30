import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
from matplotlib import cm  # カラーマップのためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

# データの生成
np.random.seed(0)  # 乱数のシードを設定（再現性のため）
days = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
data = {
    '曜日': days,
    'Aさん': np.random.normal(36.0, 0.2, size=7),
    'Bさん': np.random.normal(36.0, 0.2, size=7),
}
df = pd.DataFrame(data)  # データフレームにデータを格納

# プロットの設定
fig, ax = plt.subplots(figsize=(8, 4))

# 折れ線グラフをプロットする関数
def plot_line(ax, df, person, marker, linestyle):
    ax.plot(df['曜日'], df[person], marker=marker, linestyle=linestyle, label=person)  # 折れ線グラフを描画
    ax.tick_params(labelsize=12)  # 軸ラベルのフォントサイズを設定


# AさんとBさんの体温推移をプロット
plot_line(ax, df, 'Aさん', 'o', '-')
plot_line(ax, df, 'Bさん', 's', '--')

ax.set_ylabel('体温 [℃]', fontsize=14)  # y軸ラベルを設定
ax.legend(fontsize=14)  # 凡例の表示
plt.savefig('2_2_2_line_plot.png', dpi=300)  # 画像として保存
