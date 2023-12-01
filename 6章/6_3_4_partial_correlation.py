
import seaborn as sns  # グラフ作成のためのSeaborn
import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams['font.size'] = 16  # プロットのフォントサイズを16に設定

# Seabornのtipsデータセットを使用
df = sns.load_dataset('tips')

# 相関係数の計算
corr_total_tip = np.corrcoef(df['total_bill'], df['tip'])[0, 1]
corr_total_size = np.corrcoef(df['total_bill'], df['size'])[0, 1]
corr_tip_size = np.corrcoef(df['tip'], df['size'])[0, 1]


# total_billで統制したtipとsizeの偏相関係数の計算
partial_corr_tip_size = (corr_tip_size - corr_total_tip * corr_total_size) / \
    np.sqrt((1 - corr_total_tip**2) * (1 - corr_total_size**2))


# 散布図と回帰直線を描画する
fig, axes = plt.subplots(1, 3, figsize=(12, 5))

# 日本語の列名に変更
df = df.rename(
    columns={'total_bill': r'会計額 [$]', 'tip': r'チップの額 [$]', 'size': 'グループの人数'})

# total_billとtipの散布図
sns.regplot(x=df[r'会計額 [$]'], y=df[r'チップの額 [$]'], ax=axes[1],
            color='b', scatter_kws={'alpha': 0.4})
axes[1].set_title(f'会計額とチップの額\n $r = ${corr_total_tip:.2f}')

# total_billとsizeの散布図
sns.regplot(x=df['グループの人数'], y=df[r'会計額 [$]'], ax=axes[2],
            color='r', scatter_kws={'alpha': 0.4})
axes[2].set_title(f'グループの人数と会計額\n $r = ${corr_total_size:.2f}')

# tipとsizeの散布図
sns.regplot(x=df['グループの人数'], y=df[r'チップの額 [$]'], ax=axes[0],
            color='g', scatter_kws={'alpha': 0.4})
axes[0].set_title(f'グループの人数とチップの額\n $r = ${corr_tip_size:.2f}')

plt.tight_layout()  # レイアウトの設定
plt.savefig('6_3_4_partial_correlation.png', dpi=300)  # 図の保存
plt.show()  # 図の表示

print(corr_total_tip, corr_total_size, corr_tip_size, partial_corr_tip_size)
