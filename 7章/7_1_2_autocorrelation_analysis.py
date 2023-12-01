import numpy as np  # 数値演算のためのNumPy
import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import statsmodels.api as sm  # 統計モデルの構築のためのStatsModels
import math  # 数学関数のためのmath
import seaborn as sns  # グラフ作成のためのSeaborn
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams['font.size'] = 14  # プロットのフォントサイズを14に設定

# 生成するテストデータの設定
np.random.seed(42)  # シード値を固定
n = 100  # データ数
x = np.linspace(0, 100, n)  # 0から100まで
y = np.sin(math.pi / 5 * x) + 0.8 * \
    np.random.normal(size=len(x))  # 正弦波にノイズを加える

# DataFrameにデータを格納
df = pd.DataFrame({'y': y})

# 元の時系列データをプロット
plt.figure(figsize=(6, 3))
plt.plot(df['y'])
plt.xlabel('時刻 $t$')  # x軸ラベルを設定
plt.ylabel('$x(t)$')  # y軸ラベルを設定
plt.tight_layout()  # レイアウトの設定
plt.savefig('7_1_2_1_original_time_series.png', dpi=300)  # 図の保存
plt.show()  # 図の表示


# 自己相関プロットを作成
fig, ax = plt.subplots(figsize=(6, 3))
sm.graphics.tsa.plot_acf(df['y'], lags=40, ax=ax, title=None)  # 自己相関プロットを作成
plt.xlabel('ラグ（ずれ幅）')  # x軸ラベルを設定
plt.ylabel('自己相関係数')  # y軸ラベルを設定
plt.tight_layout()  # レイアウトの設定
plt.savefig('7_1_2_2_autocorr.png', dpi=300)  # 図の保存
plt.show()  # 図の表示


# ラグ10のラグプロット
lag = 10
x = df['y']
x_lag10 = x.shift(-lag).dropna()  # ラグ10を取る
x = x[:-lag]  # ラグ10だけデータを削除

corr = np.corrcoef(x, x_lag10)[0, 1]  # 相関係数を計算
print(f'Correlation Coefficient: {corr:.2f}')

# ラグプロットの作成
lag_df = pd.DataFrame({'$x(t)$': x, f'$x(t+{lag})$': x_lag10})  # データフレームを作成
plt.figure(figsize=(3, 3))
sns.regplot(x='$x(t)$', y=f'$x(t+{lag})$', data=lag_df, ci=95)  # ラグプロットを作成
plt.tight_layout()  # レイアウトの設定
plt.savefig('7_1_2_3_lag_plot.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
