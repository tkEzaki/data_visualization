import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import japanize_matplotlib
plt.rcParams['font.size'] = 16

# 各サンプルの設定
np.random.seed(0)
n = 20  # サンプルサイズ

# 平均と分散
means = [10, 15, 12, 20]
stddevs = [5, 5, 5, 5]

# サンプリング
sample_A = np.random.normal(means[0], stddevs[0], n - 1)
sample_B = np.random.normal(means[1], stddevs[1], n)
sample_C = np.random.normal(means[2], stddevs[2], n)
sample_D = np.random.normal(means[3], stddevs[3], n)

# サンプルAに外れ値を追加
sample_A = np.append(sample_A, 100)

# データの整形
samples = np.concatenate([sample_A, sample_B, sample_C, sample_D])
labels = ['A'] * len(sample_A) + ['B'] * len(sample_B) + ['C'] * len(sample_C) + ['D'] * len(sample_D)

# 色の設定（tab10の1,2,3,4）
colors = [plt.cm.tab10(0), plt.cm.tab10(1), plt.cm.tab10(2), plt.cm.tab10(3)]

# スウォームプロット
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.swarmplot(x=labels, y=samples, palette=colors)
# plt.title("Swarmplot of Samples")

# 棒グラフ（平均値）
sample_means = [np.mean(sample) for sample in [sample_A, sample_B, sample_C, sample_D]]

plt.subplot(1, 2, 2)
plt.bar(["A", "B", "C", "D"], sample_means, color=colors)
# plt.title("Mean of Samples")
# plt.xlabel("")
# plt.ylabel("Mean")

plt.tight_layout()
plt.savefig('8_2_4_index_including_outliers.png', dpi=300)
plt.savefig('8_2_4_index_including_outliers.svg')

plt.show()
