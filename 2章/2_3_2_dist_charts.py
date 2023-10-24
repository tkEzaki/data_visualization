import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

plt.rcParams['font.size'] = 15
# データ生成
np.random.seed(0)
num_samples = 100
category1 = np.random.normal(100, 10, num_samples)
category2 = np.random.normal(80, 20, num_samples)
data = pd.DataFrame({
    'Value': np.concatenate((category1, category2)),
    'Category': ['商品3'] * num_samples + ['商品4'] * num_samples
})

# サブプロットの作成
fig, axes = plt.subplots(2, 3, figsize=(10, 10))

# ストリッププロット
sns.stripplot(ax=axes[0, 0], x='Category', y='Value', data=data, palette=[sns.color_palette()[0], sns.color_palette()[1]])
axes[0, 0].set_title('ストリッププロット')
axes[0, 0].set_ylim(0, 140)
axes[0, 0].set_xlabel('')
axes[0, 0].set_ylabel('')

# スウォームプロット
sns.swarmplot(ax=axes[0, 1], x='Category', y='Value', data=data, palette=[sns.color_palette()[0], sns.color_palette()[1]])
axes[0, 1].set_title('スウォームプロット')
axes[0, 1].set_ylim(0, 140)
axes[0, 1].set_xlabel('')
axes[0, 1].set_ylabel('')

# ヒストグラム
bins = np.linspace(0, 140, 20)
axes[0, 2].hist(category1, bins=bins, alpha=0.5, orientation='horizontal', label='商品3')
axes[0, 2].hist(category2, bins=bins, alpha=0.5, orientation='horizontal', label='商品4')
axes[0, 2].set_title('ヒストグラム')
axes[0, 2].set_ylim(0, 140)
axes[0, 2].legend()


# バイオリンプロット
sns.violinplot(ax=axes[1, 0], x='Category', y='Value', data=data)
axes[1, 0].set_title('バイオリンプロット')
axes[1, 0].set_ylim(0, 140)
axes[1, 0].set_xlabel('')
axes[1, 0].set_ylabel('')

# エラーバー付き棒グラフ
sns.barplot(ax=axes[1, 1], x='Category', y='Value', data=data, ci='sd')  # ci='sd'で標準偏差をエラーバーとして表示
axes[1, 1].set_title('エラーバー付き棒グラフ')
axes[1, 1].set_ylim(0, 140)
axes[1, 1].set_xlabel('')
axes[1, 1].set_ylabel('')

# 箱ひげ図
sns.boxplot(ax=axes[1, 2], x='Category', y='Value', data=data)
axes[1, 2].set_title('箱髭図')
axes[1, 2].set_ylim(0, 140)
axes[1, 2].set_xlabel('')
axes[1, 2].set_ylabel('')

# plt.subplots_adjust(wspace=0.4, hspace=0.4)  # サブプロット間の空間を調節
plt.tight_layout()
plt.savefig('2_3_2_dist_charts.png', dpi=300)
plt.savefig('2_3_2_dist_charts.svg', dpi=300)
