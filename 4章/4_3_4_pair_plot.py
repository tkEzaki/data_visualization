import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns


# 高次元のデータを生成
X, _ = make_classification(n_samples=300, n_features=10, n_informative=2, n_redundant=5, n_clusters_per_class=1, random_state=42, n_classes=3)

# pandasのDataFrameに変換
df = pd.DataFrame(X, columns=[f'{i+1}' for i in range(X.shape[1])])

# ペアプロットの表示
sns.set(style="white", color_codes=True)
pairplot_fig = sns.pairplot(df, plot_kws={'alpha': 0.6}, diag_kws={'bins': 30, "color":"gold"}, aspect=1)  # aspectパラメータで正方形に設定


for ax in pairplot_fig.axes[-1, :]:
    ax.set_xlabel(ax.get_xlabel(), fontsize=40)  # x軸のラベルのフォントサイズを15に設定

for ax in pairplot_fig.axes[:, 0]:
    ax.set_ylabel(ax.get_ylabel(), fontsize=40)  # y軸のラベルのフォントサイズを15に設定

# 軸の目盛りを非表示にする
for ax in pairplot_fig.axes.flatten():
    ax.set_xticklabels([])
    ax.set_yticklabels([])


# タイトルの追加
# pairplot_fig.fig.suptitle("Pairplot of the Variables", y=1.02)  # yパラメータはタイトルの位置を調整します

# ファイルに保存
pairplot_fig.savefig("4_3_4_pairplot.png", dpi=300)
pairplot_fig.savefig("4_3_4_pairplot.svg")


plt.show()
