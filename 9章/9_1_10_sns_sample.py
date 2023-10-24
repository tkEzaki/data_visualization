import seaborn as sns
import matplotlib.pyplot as plt

# サンプルデータのロード (Irisデータセット)
data = sns.load_dataset('iris')

# ペアプロットの描画
sns.pairplot(data, hue='species', height=2.0, aspect=1.0)

plt.savefig('9_1_10_sns_sample.png', bbox_inches='tight')
# # 図の表示
plt.show()
