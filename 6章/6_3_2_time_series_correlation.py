import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
from sklearn.linear_model import LinearRegression  # 線形回帰のためのscikit-learn
import seaborn as sns  # グラフ作成のためのSeaborn
from scipy.stats import linregress  # 線形回帰のためのSciPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# データを読み込む（著者が準備したサンプルデータ）
path = "data\\brain.txt"
# データをDataFrameに変換
data_df = pd.read_csv(path, delimiter='\t')

# 時刻を1ステップにつき2.5秒に変換（2.5秒に一回のペースで撮像されたデータ）
time_steps = np.arange(0, len(data_df) * 2.5, 2.5)

# 時系列の折れ線グラフを描画して保存
fig1, ax1 = plt.subplots(figsize=(8, 2))
ax1.plot(time_steps, data_df['ROI1'], label='脳領域1',
         marker='o', markersize=3, color='darkorange')
ax1.plot(time_steps, data_df['ROI2'], label='脳領域2',
         marker='x', markersize=3, color='blue')
ax1.set_xlabel('時間 [秒]')  # x軸ラベルを設定
ax1.set_ylabel('活動量')  # y軸ラベルを設定

fig1.tight_layout()  # レイアウトの設定
fig1.savefig('6_3_2_1_time_series_line_plot.png', dpi=300)  # 図の保存
plt.show()  # 図の表示

# r値の計算
slope, intercept, r_value, p_value, std_err = linregress(
    data_df['ROI1'], data_df['ROI2'])

# seabornのregplotを使用して散布図と回帰直線、信頼区間を描画して保存
fig2, ax2 = plt.subplots(figsize=(4, 4))
sns.regplot(x='ROI1', y='ROI2', data=data_df,
            scatter_kws={'label': 'Data Points', "color": "grey"},
            line_kws={'label': 'Regression Line', 'color': 'red'},
            ax=ax2)
# 線でつなぐ
ax2.plot(data_df['ROI1'], data_df['ROI2'], linestyle='-',
         linewidth=1, color='grey', label='Time Sequence')
ax2.set_xlabel('脳領域1')  # x軸ラベルを設定
ax2.set_ylabel('脳領域2')  # y軸ラベルを設定
# r値をグラフに追加
ax2.annotate(f'$r$ = {r_value:.2f}', xy=(0.1, 0.9),
             xycoords='axes fraction', fontsize=16)

fig2.tight_layout()  # レイアウトの設定
fig2.savefig('6_3_2_2_time_series_scatter_plot.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
