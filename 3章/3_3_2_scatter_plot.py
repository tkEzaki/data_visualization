import seaborn as sns  # グラフ作成のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする
from scipy import stats  # 統計解析のためSciPyを読み込み

plt.rcParams["font.size"] = 16  # フォントサイズの設定
penguins = sns.load_dataset("penguins")  # データセットの読み込み

lm = sns.lmplot(x='bill_length_mm', y='body_mass_g', hue='species',
                data=penguins, scatter_kws={'alpha': 0.3}, legend=False)  # 回帰直線を描画

# 種ごとに回帰直線を描画
for species in penguins.species.unique():
    if species is not None:  # Exclude NaN
        species_data = penguins[penguins.species == species].dropna()  # NaNを除外
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            species_data['bill_length_mm'], species_data['body_mass_g']
        )  # 線形回帰分析

        # 相関係数とp値の出力
        print(f"For {species}:\n r value is: {r_value}\n p_value is: {p_value}")

plt.xlabel('くちばしの長さ [mm]')  # x軸ラベル
plt.ylabel('体重 [g]')  # y軸ラベル
plt.savefig('3_3_2_scatter_plot.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示
