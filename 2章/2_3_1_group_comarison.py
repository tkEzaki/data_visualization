import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
import pandas as pd  # データフレーム操作のためのPandas
import seaborn as sns  # グラフ作成のためのSeaborn
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定

# データの生成
np.random.seed(0)  # 乱数のシードを設定（再現性のため）

# 商品1の日別販売数
product1_small_var = np.random.normal(
    100, 5, 30)  # 平均100、標準偏差5の正規分布に従う乱数を30個生成
product1_small_var = product1_small_var - \
    np.mean(product1_small_var) + 100  # 平均値を100に調整

product1_large_var = np.random.normal(
    100, 20, 4)  # 平均100、標準偏差20の正規分布に従う乱数を4個生成
product1_large_var = product1_large_var - \
    np.mean(product1_large_var) + 100  # 平均値を100に調整

np.random.seed(2)  # 乱数のシードを設定（再現性のため）
# 商品2の日別販売数
product2_small_var = np.random.normal(80, 5, 30)  # 平均80、標準偏差5の正規分布に従う乱数を30個生成
product2_small_var = product2_small_var - \
    np.mean(product2_small_var) + 80  # 平均値を80に調整

product2_large_var = np.random.normal(80, 20, 4)  # 平均80、標準偏差20の正規分布に従う乱数を4個生成
product2_large_var = product2_large_var - \
    np.mean(product2_large_var) + 80  # 平均値を80に調整

# データフレームの生成
df1 = pd.DataFrame(
    {'商品': ['商品1'] * len(product1_small_var), '日別販売数': product1_small_var})
df2 = pd.DataFrame(
    {'商品': ['商品2'] * len(product2_small_var), '日別販売数': product2_small_var})
df3 = pd.DataFrame(
    {'商品': ['商品1'] * len(product1_large_var), '日別販売数': product1_large_var})
df4 = pd.DataFrame(
    {'商品': ['商品2'] * len(product2_large_var), '日別販売数': product2_large_var})

df_small_var = pd.concat([df1, df2])  # データフレームを結合
df_large_var = pd.concat([df3, df4])  # データフレームを結合

# 描画
fig, axs = plt.subplots(1, 3, figsize=(10, 5))

# 棒グラフ
axs[0].bar(['商品1', '商品2'], [100, 80], color=['blue', 'orange'])  # 棒グラフを描画
axs[0].set_ylim([0, 130])  # y軸の範囲を設定
axs[0].set_ylabel('日別販売数（平均）')  # y軸ラベル

# ストリッププロット（分散小）
sns.stripplot(x='商品', y='日別販売数', data=df_small_var,
              ax=axs[1], palette=['blue', 'orange'])  # ストリッププロットを描画
axs[1].set_ylim([0, 130])  # y軸の範囲を設定
axs[1].set_xlabel('')  # x軸ラベル

# ストリッププロット（分散大）
sns.stripplot(x='商品', y='日別販売数', data=df_large_var,
              ax=axs[2], palette=['blue', 'orange'])  # ストリッププロットを描画
axs[2].set_ylim([0, 130])  # y軸の範囲を設定
axs[2].set_xlabel('')  # x軸ラベル

plt.tight_layout()  # レイアウトの調整
plt.savefig('2_3_1_group_comparison.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示
