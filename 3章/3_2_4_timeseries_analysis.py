import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import statsmodels.api as sm  # 統計モデルのためのStatsmodels
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定

# データの読み込み（インターネットからDL）
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                 parse_dates=['date'], index_col='date')


model_type = 'additive'  # 'multiplicative'  # 加算で分解するか、乗算で分解するかを指定

# データを分解
res = sm.tsa.seasonal_decompose(df['value'], model=model_type)

# 図の描画
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 8))  # 4行1列のグラフを作成

res.observed.plot(ax=ax1, color='blue', alpha=0.5)  # 観測値を描画
res.trend.plot(ax=ax2, color='red', alpha=0.5)  # トレンドを描画
res.seasonal.plot(ax=ax3, color='green', alpha=0.5)  # 季節性を描画
res.resid.plot(ax=ax4, color='purple', alpha=0.5)  # 残差を描画


# グラフの設定
# x軸のラベルを削除
ax1.set_xlabel('')
ax2.set_xlabel('')
ax3.set_xlabel('')
ax4.set_xlabel('')

plt.subplots_adjust(hspace=0.8)  # サブプロット間の余白を設定
plt.savefig(f'3_2_4_timeseries_analysis_{model_type}.png', dpi=300)  # 画像として保存
plt.show()  # 図の表示
