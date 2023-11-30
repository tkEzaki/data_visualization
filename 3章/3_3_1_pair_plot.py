import seaborn as sns  # グラフ作成のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams["font.size"] = 16  # フォントサイズの設定

penguins = sns.load_dataset("penguins")  # データセットの読み込み

# カラム名を日本語にする
penguins = penguins.rename(columns={"species": "種類", "island": "島", "bill_length_mm": "くちばしの長さ [mm]",
                                    "bill_depth_mm": "くちばしの厚さ [mm]", "flipper_length_mm": "ひれの長さ [mm]", "body_mass_g": "体重 [g]"})

# ペアプロットの描画
grid = sns.pairplot(penguins, hue="種類")  # ペアプロットを描画
grid._legend.remove()  # 凡例を削除

plt.tight_layout()  # レイアウトの設定
plt.savefig('3_3_1_pairplot.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示
