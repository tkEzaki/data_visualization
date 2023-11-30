import numpy as np  # 数値演算のためのNumPy
import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import seaborn as sns  # グラフ作成のためのSeaborn
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定

# データ生成
np.random.seed(0)  # 乱数のシードを設定（再現性のため）
num_samples = 100  # サンプルサイズ
# 平均100、標準偏差10の正規分布に従う乱数をnum_samples個生成
category1 = np.random.normal(100, 10, num_samples)
# 平均80、標準偏差20の正規分布に従う乱数をnum_samples個生成
category2 = np.random.normal(80, 20, num_samples)
# データフレームの生成
data = pd.DataFrame({
    'Value': np.concatenate((category1, category2)),
    'Category': ['商品3'] * num_samples + ['商品4'] * num_samples
})

data = data[data['Category'] == '商品4']  # 商品4だけを選択

fig, ax = plt.subplots(figsize=(6, 6))  # サブプロットの作成

# 箱ひげ図
sns.boxplot(x='Category', y='Value', data=data,
            color=sns.color_palette()[1], width=0.3)  # 箱ひげ図を描画

# スウォームプロット
sns.swarmplot(x='Category', y='Value', data=data, color=sns.color_palette()[
              1], edgecolor="black", linewidth=1)  # スウォームプロットを描画

plt.ylim(0, 140)  # y軸の範囲を設定
plt.xlabel('')  # x軸ラベル
plt.ylabel('')  # y軸ラベル

sns.despine()  # 上下左右の枠線を削除

plt.savefig('2_3_3_boxplot.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示
