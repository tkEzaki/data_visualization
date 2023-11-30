import seaborn as sns
import matplotlib.pyplot as plt
import japanize_matplotlib
from matplotlib import cm

plt.rcParams['font.size'] = 13

# SeabornからIrisデータセットを読み込む
iris_dataset = sns.load_dataset("iris")
japanese_species_names = ['セトサ', 'バージカラー', 'バージニカ']
iris_dataset["species"] = iris_dataset['species'].map({
    'setosa': 'セトサ',
    'versicolor': 'バージカラー',
    'virginica': 'バージニカ'
})
iris_dataset = iris_dataset.rename(columns={"species": "種"})

# tab10カラーマップから最初の3色を取得
colors = cm.tab10(range(3))

# サブプロットを作成（横3 x 縦2のレイアウト）
fig, axes = plt.subplots(2, 3, figsize=(9, 6))

# セトサの散布図
sns.scatterplot(x="petal_length", y="petal_width", color=colors[0], data=iris_dataset[iris_dataset['種'] == 'セトサ'], ax=axes[0, 0])
axes[0, 0].set_title('セトサ', fontsize=13)
axes[0, 0].set_xlabel('花弁の長さ [cm]')
axes[0, 0].set_ylabel('花弁の幅 [cm]')

sns.scatterplot(x="petal_length", y="sepal_length", color=colors[0], data=iris_dataset[iris_dataset['種'] == 'セトサ'], ax=axes[1, 0])
# axes[1, 0].set_title('セトサ (花弁長 vs がく片長さ)', fontsize=13)
axes[1, 0].set_xlabel('花弁の長さ [cm]')
axes[1, 0].set_ylabel('がく片の長さ [cm]')

# バージカラーの散布図
sns.scatterplot(x="petal_length", y="petal_width", color=colors[1], data=iris_dataset[iris_dataset['種'] == 'バージカラー'], ax=axes[0, 1])
sns.scatterplot(x="petal_length", y="sepal_length", color=colors[1], data=iris_dataset[iris_dataset['種'] == 'バージカラー'], ax=axes[1, 1])
axes[0, 1].set_title('バージカラー', fontsize=13)
axes[0, 1].set_xlabel('花弁の長さ [cm]')
axes[0, 1].set_ylabel('')
# axes[1, 1].set_title('バージカラー (花弁長 vs がく片長さ)', fontsize=13)
axes[1, 1].set_xlabel('花弁の長さ [cm]')
axes[1, 1].set_ylabel('')

# バージニカの散布図
sns.scatterplot(x="petal_length", y="petal_width", color=colors[2], data=iris_dataset[iris_dataset['種'] == 'バージニカ'], ax=axes[0, 2])
sns.scatterplot(x="petal_length", y="sepal_length", color=colors[2], data=iris_dataset[iris_dataset['種'] == 'バージニカ'], ax=axes[1, 2])
axes[0, 2].set_title('バージニカ', fontsize=13)
axes[0, 2].set_xlabel('花弁の長さ [cm]')
axes[0, 2].set_ylabel('')
# axes[1, 2].set_title('バージニカ (花弁長 vs がく片長さ)', fontsize=13)
axes[1, 2].set_xlabel('花弁の長さ [cm]')
axes[1, 2].set_ylabel('')

# グラフを表示
plt.tight_layout()
plt.savefig('8_1_8_2_panel_layout_good.png', dpi=300)
plt.savefig('8_1_8_2_panel_layout_good.svg', dpi=300)

plt.show()
