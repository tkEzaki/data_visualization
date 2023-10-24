import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
plt.rcParams['font.size'] = 14
np.random.seed(0)

# 中央傾向：平均値が0と10の二つの分布
data1_a = np.random.normal(0, 1, 1000)
data1_b = np.random.normal(5, 1, 1000)

# 分散：分散が大きい分布と小さい分布
data2_a = np.random.normal(5, 1, 1000)
data2_b = np.random.normal(5, 3, 1000)

# 形状：正規分布、左寄せの分布
data3_a = np.random.normal(5, 1, 1000)
data3_b = np.random.gamma(2, 2, 1000)  # 左寄せの分布を作るためにガンマ分布を使用

# ピーク：ピーク一つとピーク二つの分布
data4_a = np.random.normal(5, 1, 1000)
data4_b = np.concatenate([np.random.normal(3, 1, 500), np.random.normal(7, 1, 500)])

# 外れ値：ごく少量の大きい外れ値が含まれている分布と含まれていない分布
data5_a = np.concatenate([np.random.normal(5, 1, 995), np.random.normal(50, 5, 5)])  # 大きな外れ値をごく少量含む
data5_b = np.random.normal(5, 1, 1000)  # 外れ値を含まない

# 外れ値：外れ値が多少ある分布とほぼない分布
data6_a = np.random.normal(5, 1, 1000)  # 外れ値なし
data6_b = np.concatenate([np.random.normal(5, 1, 975), np.random.normal(15, 1, 25)])  # 外れ値あり


data_a = [data1_a, data2_a, data3_a, data4_a, data5_a, data6_a]
data_b = [data1_b, data2_b, data3_b, data4_b, data5_b, data6_b]

fig, axs = plt.subplots(2, 3, figsize=(10, 6))

titles = ['ピークの位置', '広がりの度合い', '分布の形状', 'ピークの数と位置', '外れ値', '外れ値？']

for i, ax in enumerate(axs.flat):
    min_bin = min(min(data_a[i]), min(data_b[i]))
    max_bin = max(max(data_a[i]), max(data_b[i]))
    bins = np.linspace(min_bin, max_bin, 30)
    if i == 4:
        bins = np.linspace(min_bin, max_bin, 100)

    ax.hist(data_a[i], bins=bins, alpha=0.5, color='blue', edgecolor='black', label='A')
    ax.hist(data_b[i], bins=bins, alpha=0.5, color='gold', edgecolor='black', label='B')
    ax.set_title(titles[i])
    # ax.legend()

axs[1, 1].set_xlabel('観測値')
axs[0, 0].set_ylabel('頻度')
axs[1, 0].set_ylabel('頻度')

plt.tight_layout()
# plt.subplots_adjust(wspace=0.3, hspace=0.4)

plt.savefig('3_1_1_dist_comparison.png', dpi=300)
plt.savefig('3_1_1_dist_comparison.svg')
