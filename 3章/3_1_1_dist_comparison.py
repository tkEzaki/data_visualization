import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ
plt.rcParams['font.size'] = 14  # フォントサイズを14に設定
np.random.seed(0)  # 乱数のシードを設定（再現性のため）

# 中央傾向：平均値が0と10の二つの分布
data1_a = np.random.normal(0, 1, 1000)  # 平均0、標準偏差1の正規分布に従う乱数を1000個生成
data1_b = np.random.normal(5, 1, 1000)  # 平均5、標準偏差1の正規分布に従う乱数を1000個生成

# 分散：分散が大きい分布と小さい分布
data2_a = np.random.normal(5, 1, 1000)  # 平均5、標準偏差1の正規分布に従う乱数を1000個生成
data2_b = np.random.normal(5, 3, 1000)  # 平均5、標準偏差3の正規分布に従う乱数を1000個生成

# 形状：正規分布、左寄せの分布
data3_a = np.random.normal(5, 1, 1000)  # 平均5、標準偏差1の正規分布に従う乱数を1000個生成
data3_b = np.random.gamma(2, 2, 1000)  # 形状パラメータ2、尺度パラメータ2のガンマ分布に従う乱数を1000個生成

# ピーク：ピーク一つとピーク二つの分布
data4_a = np.random.normal(5, 1, 1000)  # 平均5、標準偏差1の正規分布に従う乱数を1000個生成
data4_b = np.concatenate(
    [np.random.normal(3, 1, 500), np.random.normal(7, 1, 500)]
)  # 平均3、標準偏差1の正規分布と平均7、標準偏差1の正規分布に従う乱数を500個ずつ生成

# 外れ値：ごく少量の大きい外れ値が含まれている分布と含まれていない分布
data5_a = np.concatenate(
    [np.random.normal(5, 1, 995), np.random.normal(50, 5, 5)]
)  # 平均5、標準偏差1の正規分布に従う乱数を995個と平均50、標準偏差5の正規分布に従う乱数を5個生成
data5_b = np.random.normal(5, 1, 1000)  # 平均5、標準偏差1の正規分布に従う乱数を1000個生成

# 外れ値：外れ値が多少ある分布とほぼない分布
data6_a = np.random.normal(5, 1, 1000)  # 平均5、標準偏差1の正規分布に従う乱数を1000個生成
data6_b = np.concatenate(
    [np.random.normal(5, 1, 975), np.random.normal(15, 1, 25)]
)  # 平均5、標準偏差1の正規分布に従う乱数を975個と平均15、標準偏差1の正規分布に従う乱数を25個生成


# データのプロット
data_a = [data1_a, data2_a, data3_a, data4_a, data5_a, data6_a]
data_b = [data1_b, data2_b, data3_b, data4_b, data5_b, data6_b]

fig, axs = plt.subplots(2, 3, figsize=(10, 6))  # 2行3列のグラフを作成

titles = ['ピークの位置', '広がりの度合い', '分布の形状', 'ピークの数と位置', '外れ値', '外れ値？']  # グラフのタイトル

for i, ax in enumerate(axs.flat):
    min_bin = min(min(data_a[i]), min(data_b[i]))  # ヒストグラムの最小値
    max_bin = max(max(data_a[i]), max(data_b[i]))  # ヒストグラムの最大値
    bins = np.linspace(min_bin, max_bin, 30)  # ビンの設定
    if i == 4:
        bins = np.linspace(min_bin, max_bin, 100)  # ビンの設定

    ax.hist(data_a[i], bins=bins, alpha=0.5,
            color='blue', edgecolor='black', label='A')  # ヒストグラムの描画
    ax.hist(data_b[i], bins=bins, alpha=0.5,
            color='gold', edgecolor='black', label='B')  # ヒストグラムの描画
    ax.set_title(titles[i])  # グラフのタイトル

axs[1, 1].set_xlabel('観測値')  # x軸ラベル
axs[0, 0].set_ylabel('頻度')  # y軸ラベル
axs[1, 0].set_ylabel('頻度')  # y軸ラベル

plt.tight_layout()  # グラフの間隔を調整
plt.savefig('3_1_1_dist_comparison.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
