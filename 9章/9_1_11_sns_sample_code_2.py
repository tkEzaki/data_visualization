import seaborn as sns
import matplotlib.pyplot as plt

# 散布図
sns.scatterplot(x="x_data", y="y_data", data=data)
# 回帰直線付き散布図
sns.regplot(x="x_data", y="y_data", data=data)
# 折れ線グラフ
sns.lineplot(x="x_data", y="y_data", data=data)
# 棒グラフ
sns.barplot(x="x_data", y="y_data", data=data)
# 箱ひげ図
sns.boxplot(x="x_data", y="y_data", data=data)
# バイオリンプロット
sns.violinplot(x="x_data", y="y_data", data=data)
# スウォームプロット
sns.swarmplot(x="x_data", y="y_data", data=data)
# ヒストグラム
sns.histplot(data=data, x="x_data")
# カーネル密度推定プロットKDE
sns.kdeplot(data=data, x="x_data")
# ヒートマップ
sns.heatmap(data)
# クラスターマップ
sns.clustermap(data)
# ペアプロット
sns.pairplot(data)

