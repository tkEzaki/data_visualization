import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# データ生成
np.random.seed(0)
num_samples = 100
category1 = np.random.normal(100, 10, num_samples)
category2 = np.random.normal(80, 20, num_samples)
data = pd.DataFrame({
    'Value': np.concatenate((category1, category2)),
    'Category': ['商品3'] * num_samples + ['商品4'] * num_samples
})

# 商品4だけを選択
data = data[data['Category'] == '商品4']

fig, ax = plt.subplots(figsize=(6, 6))
# 箱ひげ図
sns.boxplot(x='Category', y='Value', data=data, color=sns.color_palette()[1], width=0.3)

# スウォームプロット
sns.swarmplot(x='Category', y='Value', data=data, color=sns.color_palette()[1], edgecolor="black", linewidth=1)

plt.ylim(0, 140)
plt.xlabel('')
plt.ylabel('')

# 枠線の削除
sns.despine()

plt.savefig('2_3_3_boxplot.png', dpi=300)
plt.savefig('2_3_3_boxplot.svg', dpi=300)

# plt.show()
