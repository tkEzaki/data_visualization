import seaborn as sns
import matplotlib.pyplot as plt
import japanize_matplotlib
plt.rcParams['font.size'] = 14

# SeabornからIrisデータセットを読み込む
# （注：この環境ではインターネットアクセスが制限されているため、実行できません）
iris_dataset = sns.load_dataset("iris")
japanese_species_names = ['セトサ', 'バージカラー', 'バージニカ']
iris_dataset["species"] = iris_dataset['species'].map({
    'setosa': 'セトサ',
    'versicolor': 'バージカラー',
    'virginica': 'バージニカ'
})
iris_dataset = iris_dataset.rename(columns={"species": "種"})

# サブプロットを作成
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# 左側のサブプロット
sns.scatterplot(x="petal_length", y="petal_width", hue="種", data=iris_dataset, ax=axes[0])
# axes[0].set_title('Petal Length vs Petal Width (Left)')
axes[0].set_xlabel('$L_p$')
axes[0].set_ylabel('$W_p$')
# eliminate the legend
axes[0].get_legend().remove()

# 右側のサブプロット
sns.scatterplot(x="petal_length", y="petal_width", hue="種", data=iris_dataset, ax=axes[1])
# axes[1].set_title('Petal Length vs Petal Width (Right)')
axes[1].set_xlabel('花弁の長さ [cm], $L_p$')
axes[1].set_ylabel('花弁の幅 [cm], $W_p$')


# グラフを表示
plt.tight_layout()
plt.savefig('8_1_7_label_intelligibility.png', dpi=300)
plt.show()
