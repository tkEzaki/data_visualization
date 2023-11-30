import numpy as np  # 数値計算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定

# データ生成
np.random.seed(0)  # 同じ乱数が生成されるようにシードを設定
n_days = 30  # 30日間
n_individuals = 30  # 個体数
half_n = int(n_individuals / 2)  # 個体数の半分

# 各個体の活動量期待値を生成
expected_values_group1 = np.random.normal(
    loc=50, scale=5, size=half_n)  # 期待値50、標準偏差5の正規分布に従う乱数を生成
expected_values_group2 = np.random.normal(
    loc=70, scale=5, size=half_n)  # 期待値70、標準偏差5の正規分布に従う乱数を生成
expected_values = np.concatenate(
    [expected_values_group1, expected_values_group2])  # 二つの配列を結合

# 各個体の30日間の活動量を生成
activity_data = [np.random.normal(loc=ev, scale=10, size=n_days)
                 for ev in expected_values]  # 期待値ev、標準偏差10の正規分布に従う乱数を生成

# グラフ描画
fig, axs = plt.subplots(2, 2, figsize=(8, 6))  # 2行2列のグラフを作成

# 全個体をそれぞれ違う色で描画
colors = plt.cm.jet(np.linspace(0, 1, n_individuals))  # 色のリストを生成

for i in range(n_individuals):
    axs[0, 0].plot(range(n_days), activity_data[i],
                   color=colors[i], alpha=0.8)  # 各個体の活動量を描画

# 一番活動量の期待値が大きい個体をゴールド、それ以外は灰色で描画
max_ev_individual = np.argmax(expected_values)  # 最大期待値の個体のインデックス
for i in range(n_individuals):
    if i == max_ev_individual:  # 最大期待値の個体はゴールドにするのでpassする
        pass
    color = 'gray'  # 最大期待値の個体以外は灰色
    axs[0, 1].plot(range(n_days), activity_data[i],
                   color=color, alpha=0.5)  # 各個体の活動量を描画

color = 'gold'  # 最大期待値の個体はゴールド
axs[0, 1].plot(range(n_days), activity_data[max_ev_individual],
               color=color, lw=2)  # 最大期待値の個体の活動量を描画


# 15個体のグループごとに、ゴールド、青で描画
for i in range(half_n):
    axs[1, 0].plot(range(n_days), activity_data[i],
                   color='gold', alpha=0.5)  # ゴールドで描画

for i in range(half_n, n_individuals):
    axs[1, 0].plot(range(n_days), activity_data[i],
                   color='blue', alpha=0.5)  # 青で描画


# 各グループの各日の平均値と標準偏差を計算し、平均値を折れ線グラフで、標準偏差をその周りの影付きの領域で描画
for i, color in zip([0, half_n], ['gold', 'blue']):
    group_activity_data = activity_data[i:i + half_n]  # グループのデータを取得
    group_mean = np.mean(group_activity_data, axis=0)  # グループの平均値を計算
    group_std = np.std(group_activity_data, axis=0)  # グループの標準偏差を計算
    axs[1, 1].plot(range(n_days), group_mean, color=color)  # 平均値を描画
    axs[1, 1].fill_between(range(n_days), group_mean - group_std,
                           group_mean + group_std, color=color, alpha=0.3)  # 標準偏差を描画

# グラフの調整
for ax in axs.ravel():
    ax.set_ylim(15, 105)  # y軸の範囲を設定

axs[0, 0].set_ylabel("活動量スコア")  # y軸のラベルを設定
axs[1, 0].set_ylabel("活動量スコア")  # y軸のラベルを設定
axs[1, 0].set_xlabel("経過日数")  # x軸のラベルを設定
axs[1, 1].set_xlabel("経過日数")  # x軸のラベルを設定

plt.tight_layout()  # レイアウトの設定
plt.subplots_adjust(hspace=0.3, wspace=0.2)  # サブプロット間の余白を設定
plt.savefig('3_2_2_many_line_plots.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示
