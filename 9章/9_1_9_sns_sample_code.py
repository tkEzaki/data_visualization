import seaborn as sns
import matplotlib.pyplot as plt

# サンプルデータのロード (Irisデータセット)
data = sns.load_dataset('iris')

# ペアプロットの描画
sns.pairplot(data, hue='species')

# 図の表示
plt.show()