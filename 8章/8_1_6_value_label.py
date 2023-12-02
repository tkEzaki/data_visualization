import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # 日本語化のためのライブラリ
import pandas as pd  # データフレーム操作のためのPandas
import numpy as np  # 数値計算のためのNumPy
import seaborn as sns  # グラフ描画のためのSeaborn
plt.rcParams['font.size'] = 13  # プロットのフォントサイズを13に設定

np.random.seed(5)  # 乱数のシードを固定

# 10変数、各時系列の長さはL=20でランダムデータを生成（正の値のみ）
# 乱数は0から1の範囲で生成されるため、それに50を足して負にならないようにする
L = 20
data = np.random.rand(L, 6) * 50
df = pd.DataFrame(data, columns=[chr(65 + i)
                  for i in range(6)])  # 変数名をA, B, C, ...とする

# 相関係数を計算
correlation_matrix = df.corr()

# サブプロットを作成（1行、2列）
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

# ヒートマップのサブプロット
sns.heatmap(correlation_matrix, ax=axes[1], cmap='coolwarm', vmin=-1, vmax=1)

# 棒グラフのサブプロット（1変数目（'A'）を使用）
axes[0].bar(range(L), df['A'])  # 棒グラフを描画
axes[0].set_xlim(-0.50, 10.5)  # x軸の範囲を設定

plt.tight_layout()  # レイアウトの設定
plt.savefig('8_1_6_1_heatmap_and_bar_without_values.png', dpi=300)  # 図の保存
plt.show()  # 図の表示


# 修正を加えた図を作成
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

# ヒートマップ（相関係数の値を表示）
sns.heatmap(correlation_matrix, annot=True,
            ax=axes[1], cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)

# 棒グラフ（各棒の値を表示）
bars = axes[0].bar(range(L), df['A'])
for bar in bars[0:11]:
    yval = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width() / 2, yval,
                 round(yval, 2), ha='center', va='bottom')
axes[0].set_xlim(-0.50, 10.5)  # x軸の範囲を設定

plt.tight_layout()  # レイアウトの設定
plt.savefig('8_1_6_2_heatmap_and_bar_with_values.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
