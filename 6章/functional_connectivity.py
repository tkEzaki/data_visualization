import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
from scipy.stats import linregress


plt.rcParams['font.family'] = 'Yu Gothic'
plt.rcParams['font.size'] = 12


# データを読み込む

path = "data\\brain.txt"
# データをDataFrameに変換
data_df = pd.read_csv(path, delimiter='\t')

# 時刻を1ステップにつき2.5秒に変換
time_steps = np.arange(0, len(data_df) * 2.5, 2.5)

# 時系列の折れ線グラフを描画して保存（時刻を変換）
fig1, ax1 = plt.subplots(figsize=(8, 2))
ax1.plot(time_steps, data_df['ROI1'], label='脳領域1', marker='o', markersize=3, color='darkorange')
ax1.plot(time_steps, data_df['ROI2'], label='脳領域2', marker='x', markersize=3, color='blue')
ax1.set_xlabel('時間 [秒]')
ax1.set_ylabel('活動量')
# ax1.legend()
fig1.tight_layout()
fig1.savefig('time_series_plot.png', dpi=300)

# r値の計算
slope, intercept, r_value, p_value, std_err = linregress(data_df['ROI1'], data_df['ROI2'])

# seabornのregplotを使用して散布図と回帰直線、信頼区間を描画して保存
fig2, ax2 = plt.subplots(figsize=(4, 4))
sns.regplot(x='ROI1', y='ROI2', data=data_df, 
            scatter_kws={'label': 'Data Points', "color": "grey"}, 
            line_kws={'label': 'Regression Line', 'color': 'red'}, 
            ax=ax2)
ax2.plot(data_df['ROI1'], data_df['ROI2'], linestyle='-', linewidth=1, color='grey', label='Time Sequence')
ax2.set_xlabel('脳領域1')
ax2.set_ylabel('脳領域2')
# r値をグラフに追加
ax2.annotate(f'$r$ = {r_value:.2f}', xy=(0.1, 0.9), xycoords='axes fraction', fontsize=16)

# ax2.legend()
fig2.tight_layout()
fig2.savefig('scatter_plot.png', dpi=300)