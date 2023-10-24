import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import japanize_matplotlib

plt.rcParams['font.size'] = 14
# データの生成
np.random.seed(0)

# 商品1の日別販売数
product1_small_var = np.random.normal(100, 5, 30)
product1_small_var = product1_small_var - np.mean(product1_small_var) + 100  # 平均値を100に調整

product1_large_var = np.random.normal(100, 20, 4)
product1_large_var = product1_large_var - np.mean(product1_large_var) + 100  # 平均値を100に調整

np.random.seed(2)
# 商品2の日別販売数
product2_small_var = np.random.normal(80, 5, 30)
product2_small_var = product2_small_var - np.mean(product2_small_var) + 80  # 平均値を80に調整

product2_large_var = np.random.normal(80, 20, 4)
product2_large_var = product2_large_var - np.mean(product2_large_var) + 80  # 平均値を80に調整

# データフレームの生成
df1 = pd.DataFrame({'商品': ['商品1'] * len(product1_small_var), '日別販売数': product1_small_var})
df2 = pd.DataFrame({'商品': ['商品2'] * len(product2_small_var), '日別販売数': product2_small_var})
df3 = pd.DataFrame({'商品': ['商品1'] * len(product1_large_var), '日別販売数': product1_large_var})
df4 = pd.DataFrame({'商品': ['商品2'] * len(product2_large_var), '日別販売数': product2_large_var})

df_small_var = pd.concat([df1, df2])
df_large_var = pd.concat([df3, df4])

# 描画
fig, axs = plt.subplots(1, 3, figsize=(10, 5))

# 棒グラフ
axs[0].bar(['商品1', '商品2'], [100, 80], color=['blue', 'orange'])
axs[0].set_ylim([0, 130])
# axs[0].set_title('棒グラフ')
axs[0].set_ylabel('日別販売数（平均）')

# ストリッププロット（分散小）
sns.stripplot(x='商品', y='日別販売数', data=df_small_var, ax=axs[1], palette=['blue', 'orange'])
axs[1].set_ylim([0, 130])
# axs[1].set_title('ストリッププロット（分散小）')
axs[1].set_xlabel('')
# axs[1].set_ylabel('')

# ストリッププロット（分散大）
sns.stripplot(x='商品', y='日別販売数', data=df_large_var, ax=axs[2], palette=['blue', 'orange'])
axs[2].set_ylim([0, 130])
# axs[2].set_title('ストリッププロット（分散大）')
axs[2].set_xlabel('')
# axs[2].set_ylabel('')

# サブプロット間の間隔調整
# plt.subplots_adjust(wspace=0.4)
plt.tight_layout()
# グラフの表示
# plt.show()
plt.savefig('2_3_1_group_comparison.png', dpi=300)
plt.savefig('2_3_1_group_comparison.svg', dpi=300)

