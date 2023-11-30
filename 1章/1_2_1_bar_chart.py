import seaborn as sns  # seabornをインポートする（統計的グラフ描画ライブラリ）
import matplotlib.pyplot as plt  # matplotlib.pyplotをpltとしてインポート
import pandas as pd  # pandasをpdとしてインポート
import numpy as np  # numpyをnpとしてインポート
from matplotlib.ticker import FuncFormatter  # MatplotlibのFuncFormatterをインポート
import japanize_matplotlib  # matplotlibで日本語を使用するためのライブラリをインポート

plt.rcParams["font.size"] = 20  # フォントサイズの設定

# データ
countries = ['日本', 'ブラジル', '米国', '中国']  # 国のリスト
populations = [124620000, 215802222, 335540000, 1425849288]  # 人口のリスト

# DataFrameの作成
df = pd.DataFrame({
    'Country': countries,  # 国名
    'Population': populations  # 人口
})
df['Population'] = df['Population'] / 100000000  # 人口を億単位に変換

# 米国と日本だけをフィルタリングして降順に並べ替え
df_filtered = df[df['Country'].isin(['米国', '日本'])].sort_values(by='Population', ascending=False)

# 全ての国を人口で降順に並べ替え
df_sorted = df.sort_values(by='Population', ascending=False)

# 米国と日本のみを含む棒グラフの描画（seabornを使用）
fig1, ax1 = plt.subplots(figsize=(6, 2.5))
sns.barplot(x='Population', y='Country', data=df_filtered, ax=ax1, orient='h', color='orange')
ax1.set_xlabel("人口 [億人]")  # x軸ラベル
ax1.set_ylabel("")  # y軸ラベル（空）


plt.tight_layout()
plt.savefig('1_2_1_bar1.png', dpi=300)  # PNG形式で保存
plt.show()

# 四つの国を含む棒グラフの描画（seabornを使用）
fig2, ax2 = plt.subplots(figsize=(6, 3))
sns.barplot(x='Population', y='Country', data=df_sorted, ax=ax2, orient='h', color='orange')
ax2.set_xlabel("人口 [億人]")  # x軸ラベル
ax2.set_ylabel("")  # y軸ラベル（空）

plt.tight_layout()
plt.savefig('1_2_1_bar2.png', dpi=300)  # PNG形式で保存
plt.show()
