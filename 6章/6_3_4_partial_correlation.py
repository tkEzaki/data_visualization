
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams['font.size'] = 16

# Seabornのtipsデータセットを使用
df = sns.load_dataset('tips')

# 相関係数の計算
corr_total_tip = np.corrcoef(df['total_bill'], df['tip'])[0, 1]
corr_total_size = np.corrcoef(df['total_bill'], df['size'])[0, 1]
corr_tip_size = np.corrcoef(df['tip'], df['size'])[0, 1]


# total_billで統制したtipとsizeの偏相関係数の計算
partial_corr_tip_size = (corr_tip_size - corr_total_tip * corr_total_size) / \
    np.sqrt((1 - corr_total_tip**2) * (1 - corr_total_size**2))


# 散布図と回帰直線
fig, axes = plt.subplots(1, 3, figsize=(12, 5))

df = df.rename(columns={'total_bill': r'会計額 [$]', 'tip': r'チップの額 [$]', 'size': 'グループの人数'})
# total_billとtip
sns.regplot(x=df[r'会計額 [$]'], y=df[r'チップの額 [$]'], ax=axes[1], color='b', scatter_kws={'alpha': 0.4})
axes[1].set_title(f'会計額とチップの額\n $r = ${corr_total_tip:.2f}')

# total_billとsize
sns.regplot(x=df['グループの人数'], y=df[r'会計額 [$]'], ax=axes[2], color='r', scatter_kws={'alpha': 0.4})
axes[2].set_title(f'グループの人数と会計額\n $r = ${corr_total_size:.2f}')

# tipとsize
sns.regplot(x=df['グループの人数'], y=df[r'チップの額 [$]'], ax=axes[0], color='g', scatter_kws={'alpha': 0.4})
axes[0].set_title(f'グループの人数とチップの額\n $r = ${corr_tip_size:.2f}')

plt.tight_layout()
plt.savefig('6_3_4_partial_correlation.png', dpi=300)
plt.savefig('6_3_4_partial_correlation.svg', dpi=300)

plt.show()

print(corr_total_tip, corr_total_size, corr_tip_size, partial_corr_tip_size)
