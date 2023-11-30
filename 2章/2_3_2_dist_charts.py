import numpy as np  # 数値演算のためのNumPy
import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import seaborn as sns  # グラフ作成のためのSeaborn
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams['font.size'] = 15  # フォントサイズを15に設定

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

# サブプロットの作成
fig, axes = plt.subplots(2, 3, figsize=(10, 10))

# ストリッププロット
sns.stripplot(ax=axes[0, 0], x='Category', y='Value', data=data, palette=[
              sns.color_palette()[0], sns.color_palette()[1]])  # ストリッププロットを描画
axes[0, 0].set_title('ストリッププロット')  # タイトル
axes[0, 0].set_ylim(0, 140)  # y軸の範囲を設定
axes[0, 0].set_xlabel('')  # x軸ラベル
axes[0, 0].set_ylabel('')  # y軸ラベル

# スウォームプロット
sns.swarmplot(ax=axes[0, 1], x='Category', y='Value', data=data, palette=[
              sns.color_palette()[0], sns.color_palette()[1]])  # スウォームプロットを描画
axes[0, 1].set_title('スウォームプロット')  # タイトル
axes[0, 1].set_ylim(0, 140)  # y軸の範囲を設定
axes[0, 1].set_xlabel('')  # x軸ラベル
axes[0, 1].set_ylabel('')  # y軸ラベル

# ヒストグラム
bins = np.linspace(0, 140, 20)  # ビンの設定
axes[0, 2].hist(category1, bins=bins, alpha=0.5,
                orientation='horizontal', label='商品3')  # ヒストグラムを描画
axes[0, 2].hist(category2, bins=bins, alpha=0.5,
                orientation='horizontal', label='商品4')  # ヒストグラムを描画
axes[0, 2].set_title('ヒストグラム')  # タイトル
axes[0, 2].set_ylim(0, 140)  # y軸の範囲を設定
axes[0, 2].legend()  # 凡例の表示


# バイオリンプロット
sns.violinplot(ax=axes[1, 0], x='Category', y='Value', data=data)  # バイオリンプロットを描画
axes[1, 0].set_title('バイオリンプロット')  # タイトル
axes[1, 0].set_ylim(0, 140)  # y軸の範囲を設定
axes[1, 0].set_xlabel('')  # x軸ラベル
axes[1, 0].set_ylabel('')  # y軸ラベル

# エラーバー付き棒グラフ
sns.barplot(ax=axes[1, 1], x='Category', y='Value',
            data=data, ci='sd')  # ci='sd'で標準偏差をエラーバーとして表示
axes[1, 1].set_title('エラーバー付き棒グラフ')  # タイトル
axes[1, 1].set_ylim(0, 140)  # y軸の範囲を設定
axes[1, 1].set_xlabel('')  # x軸ラベル  
axes[1, 1].set_ylabel('')  # y軸ラベル

# 箱ひげ図
sns.boxplot(ax=axes[1, 2], x='Category', y='Value', data=data)  # 箱ひげ図を描画
axes[1, 2].set_title('箱髭図')  # タイトル
axes[1, 2].set_ylim(0, 140)  # y軸の範囲を設定
axes[1, 2].set_xlabel('')  # x軸ラベル
axes[1, 2].set_ylabel('')  # y軸ラベル


plt.tight_layout()  # レイアウトの設定
plt.savefig('2_3_2_dist_charts.png', dpi=300)  # 画像として保存
