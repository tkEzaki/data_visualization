import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
import japanize_matplotlib
plt.rcParams['font.size'] = 14

# データの生成
np.random.seed(0)
data1_sample1 = np.random.normal(6, 2, 20)
data1_sample2 = np.random.normal(6, 2, 20)
data2_sample1 = np.random.normal(6, 2, 400)
data2_sample2 = np.random.normal(5.75, 2, 400)

# T検定
t_stat1, p_val1 = ttest_ind(data1_sample1, data1_sample2)
t_stat2, p_val2 = ttest_ind(data2_sample1, data2_sample2)

print(np.mean(data1_sample1), np.mean(data1_sample2))
print(np.mean(data2_sample1), np.mean(data2_sample2))
# プロットの設定
fig, axes = plt.subplots(1, 2, figsize=(8, 5))

# サブプロット1
sns.swarmplot(x=['Group 1'] * len(data1_sample1) + ['Group 2'] * len(data1_sample2),
              y=np.concatenate([data1_sample1, data1_sample2]),
              palette=['blue', 'green'],
              ax=axes[0])
sns.barplot(x=['Group 1', 'Group 2'],
            y=[np.mean(data1_sample1), np.mean(data1_sample2)],
            palette=['blue', 'green'],
            alpha=0.5,
            ax=axes[0])
axes[0].set_title('$t_{20}$ =' + f'{t_stat1:.2f}, p-value = {p_val1:.4f}')
axes[0].set_ylim(0, 12)

# サブプロット2
sns.swarmplot(x=['Group 1'] * len(data2_sample1) + ['Group 2'] * len(data2_sample2),
              y=np.concatenate([data2_sample1, data2_sample2]),
              palette=['blue', 'green'],
              ax=axes[1])
sns.barplot(x=['Group 1', 'Group 2'],
            y=[np.mean(data2_sample1), np.mean(data2_sample2)],
            palette=['blue', 'green'],
            alpha=0.5,
            ax=axes[1])
axes[1].set_title('$t_{400}$ =' + f'{t_stat2:.2f}, p-value = {p_val2:.4f}')
axes[1].set_ylim(0, 12)

plt.tight_layout()
plt.savefig('8_3_2_significance_and_effect.png', dpi=300)
plt.savefig('8_3_2_significance_and_effect.svg')

plt.show()
