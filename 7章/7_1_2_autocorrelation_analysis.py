import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math
import seaborn as sns
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# 生成するテストデータの設定
np.random.seed(42)
n = 100
x = np.linspace(0, 100, n)
y = np.sin(math.pi / 5 * x) + 0.8 * np.random.normal(size=len(x))

# DataFrameにデータを格納
df = pd.DataFrame({'y': y})

# オリジナルの時系列データをプロット
plt.figure(figsize=(6, 3))
plt.plot(df['y'])
plt.xlabel('時刻 $t$')
plt.ylabel('$x(t)$')
plt.tight_layout()
plt.savefig('7_1_2_1_original_time_series.png', dpi=300)
plt.savefig('7_1_2_1_original_time_series.svg')
plt.show()

# 自己相関プロットを作成
fig, ax = plt.subplots(figsize=(6, 3))
sm.graphics.tsa.plot_acf(df['y'], lags=40, ax=ax, title=None)
# plt.title('Autocorrelation Plot')
plt.xlabel('ラグ（ずれ幅）')
plt.ylabel('自己相関係数')
plt.tight_layout()
plt.savefig('7_1_2_2_autocorr.png', dpi=300)
plt.savefig('7_1_2_2_autocorr.svg', dpi=300)
plt.show()

# ラグ10のラグプロット
lag = 10
x = df['y']
x_lag10 = x.shift(-lag).dropna()  # ラグ10を取る
print(x)
print(x_lag10)
x = x[:-lag]

corr = np.corrcoef(x, x_lag10)[0, 1]
print(f'Correlation Coefficient: {corr:.2f}')
# Create a DataFrame for seaborn
lag_df = pd.DataFrame({'$x(t)$': x, f'$x(t+{lag})$': x_lag10})

plt.figure(figsize=(3, 3))
sns.regplot(x='$x(t)$', y=f'$x(t+{lag})$', data=lag_df, ci=95)
# plt.title(f'Lag {lag} Scatter Plot with Regression Line and 95% CI')
# plt.legend()
plt.tight_layout()
plt.savefig('7_1_2_3_lag_plot.png', dpi=300)
plt.savefig('7_1_2_3_lag_plot.svg', dpi=300)

plt.show()
