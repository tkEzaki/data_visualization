import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import seaborn as sns  # グラフ作成のためのSeaborn
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams["font.size"] = 14

# 乱数のシードを設定（再現性のため）
np.random.seed(0)

# 相関のないデータを生成
x1 = np.random.rand(50)
y1 = np.random.rand(50)

# 相関の大きいデータを生成
x2 = np.random.rand(50)
y2 = 0.8 * (x2 - 0.5) + 0.5 + 0.1 * np.random.randn(50)

# グラフ描画の設定
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# サブプロット1: 相関のないデータ（色：青）
sns.regplot(x=x1, y=y1, ax=axes[0], color='blue')
# axes[0].set_title('No Correlation')
axes[0].set_xlabel('変数X', fontsize=18)  # x軸ラベル
axes[0].set_ylabel('変数Y', fontsize=18)  # y軸ラベル

# サブプロット2: 相関の大きいデータ（色：緑）
sns.regplot(x=x2, y=y2, ax=axes[1], color='green')
axes[1].set_xlabel('変数X', fontsize=18)  # x軸ラベル
axes[1].set_ylabel('変数Y', fontsize=18)  # y軸ラベル

plt.tight_layout()  # レイアウトの調整
plt.savefig('1_3_2_correlation_scatter.png', dpi=300)  # PNG形式で保存

plt.show()
