import numpy as np  # 数値計算のためのNumPy
import pandas as pd  # データフレーム操作のためのPandas
import seaborn as sns  # グラフ作成のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import matplotlib.cm as cm  # カラーマップのためのMatplotlib
import matplotlib.colors as colors  # カラーマップのためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定

np.random.seed(0)  # 同じ乱数が生成されるようにシードを設定

# ランダムな体重データを生成
weights_1 = np.random.normal(60, 2, 50)  # 平均60、分散10の正規分布
weights_2 = weights_1 + np.random.normal(-1, 0.5, 50)  # 平均-1、分散0.5の正規分布

# データフレームを作成
df1 = pd.DataFrame({'Weight': weights_1, 'Group': [
                   '実験開始時'] * 50, 'Person': np.arange(50)})
df2 = pd.DataFrame({'Weight': weights_2, 'Group': [
                   '一か月後'] * 50, 'Person': np.arange(50)})
df = pd.concat([df1, df2])  # データフレームを結合


# 図の描画
fig, axes = plt.subplots(1, 3, figsize=(10, 5))  # 1行3列のグラフを作成


# 点のみプロット
axes[0].scatter([0.25] * 50, weights_1, color='gray', alpha=0.5)  # 実験開始時の体重を描画
axes[0].scatter([0.75] * 50, weights_2, color='gray', alpha=0.5)  # 一か月後の体重を描画
axes[0].set_xticks([0.25, 0.75])  # x軸の目盛りを設定
axes[0].set_xticklabels(['実験開始時', '一か月後'], fontsize=14)  # x軸の目盛りのラベルを設定
axes[0].set_xlim([0, 1])  # x軸の範囲を設定
axes[0].set_ylabel('体重 [kg]')  # y軸のラベルを設定


# スロープグラフ
differences = weights_2 - weights_1  # 体重の差を計算
cmap = cm.get_cmap('coolwarm')  # カラーマップを取得
norm = colors.Normalize(-2, 2)  # 正規化を作成
for i in range(50):
    axes[2].plot([0.25, 0.75], [weights_1[i], weights_2[i]], marker='o',
                 color=cmap(norm(differences[i])), alpha=0.5)  # スロープグラフを描画

axes[2].set_xticks([0.25, 0.75])  # x軸の目盛りを設定
axes[2].set_xticklabels(['実験開始時', '一か月後'], fontsize=14)  # x軸の目盛りのラベルを設定
axes[2].set_xlim([0, 1])  # x軸の範囲を設定


# スロープグラフ（ランダム）
np.random.shuffle(weights_2)  # 一か月後の体重をランダムに並び替え
differences = weights_2 - weights_1  # 体重の差を計算
for i in range(50):
    axes[1].plot([0.25, 0.75], [weights_1[i], weights_2[i]], marker='o',
                 color=cmap(norm(differences[i])), alpha=0.5)  # スロープグラフを描画

axes[1].set_xticks([0.25, 0.75])  # x軸の目盛りを設定
axes[1].set_xticklabels(['実験開始時', '一か月後'], fontsize=14)  # x軸の目盛りのラベルを設定
axes[1].set_xlim([0, 1])  # x軸の範囲を設定


# カラーバーを描画
fig.subplots_adjust(right=0.85)  # プロットエリアを狭めてカラーバーにスペースを作る
cbar_ax = fig.add_axes([0.9, 0.15, 0.02, 0.7])  # カラーバーの位置とサイズを指定
cbar = plt.colorbar(cm.ScalarMappable(
    norm=norm, cmap=cmap), cax=cbar_ax
)  # カラーバーを描画
cbar.set_label('差 [kg]')  # カラーバーのラベルを設定


plt.savefig('3_2_3_slope.png', dpi=300)  # 画像を保存
plt.show()  # 画面に表示
