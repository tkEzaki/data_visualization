import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Yu Gothic'

# サンプルサイズを設定
sample_size = 1000

# 1. 半分くらいずれた同一の正規分布（さらに中心をずらす）
mean1_new, std1_new = 0, 1
mean2_new, std2_new = 1, 1  # 中心をさらに変更
dist1_1_new = np.random.normal(mean1_new, std1_new, sample_size)
dist1_2_new = np.random.normal(mean2_new, std2_new, sample_size)

# 2. 一部被っているが狭い正規分布と広い正規分布（中心をずらす）
mean3_new, std3_new = -1, 0.5  # 中心を変更
mean4_new, std4_new = 1, 1.5  # 中心を変更
dist2_1_new = np.random.normal(mean3_new, std3_new, sample_size)
dist2_2_new = np.random.normal(mean4_new, std4_new, sample_size)

# 3. 二峰性の分布（GMM）と正規分布
mean5, std5 = -2, 1
mean6, std6 = 2, 1
mean7, std7 = 0, 1.5
dist3_1 = np.concatenate([np.random.normal(mean5, std5, sample_size // 2),
                          np.random.normal(mean6, std6, sample_size // 2)])
dist3_2 = np.random.normal(mean7, std7, sample_size)

# プロット設定（一つ目のサブプロットの中心と全体の色を変更）
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 全体で使用する色
common_colors = ['darkblue', 'darkorange']

# 1. 半分くらいずれた同一の正規分布（中心をさらに変更）
axes[0].hist(dist1_1_new, alpha=0.5, label=f'N({mean1_new},{std1_new}^2)', bins=20, color=common_colors[0])
axes[0].hist(dist1_2_new, alpha=0.5, label=f'N({mean2_new},{std2_new}^2)', bins=20, color=common_colors[1])
axes[0].set_title('分布ペア１')
axes[0].legend()

# 2. 一部被っているが狭い正規分布と広い正規分布（色を変更）
axes[1].hist(dist2_1_new, alpha=0.5, label=f'N({mean3_new},{std3_new}^2)', bins=20, color=common_colors[0])
axes[1].hist(dist2_2_new, alpha=0.5, label=f'N({mean4_new},{std4_new}^2)', bins=20, color=common_colors[1])
axes[1].set_title('分布ペア２')
axes[1].legend()

# 3. 二峰性の分布（GMM）と正規分布（色を変更）
axes[2].hist(dist3_1, alpha=0.5, label=f'GMM', bins=20, color=common_colors[0])
axes[2].hist(dist3_2, alpha=0.5, label=f'N({mean7},{std7}^2)', bins=20, color=common_colors[1])
axes[2].set_title('分布ペア３')
axes[2].legend()

# グラフ表示
plt.show()

