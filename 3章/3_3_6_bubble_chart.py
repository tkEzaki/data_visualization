import pandas as pd  # データフレーム操作のためのPandas
import seaborn as sns  # グラフ作成のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする

plt.rcParams["font.size"] = 14  # プロットのフォントサイズを14に設定

# データセットの読み込み
df = pd.read_csv('bubble_chart_data.csv')  # データセットを読み込む
region_df = pd.read_csv('bubble_chart_region_data.csv')  # 地域データを読み込む

# GDP, Life expectancy, Populationのデータを取得
gdp_df = df[df['Series Name'] == 'GDP, PPP (current international $)']  # GDP
life_exp_df = df[df['Series Name'] ==
                 'Life expectancy at birth, total (years)']  # Life expectancy
population_df = df[df['Series Name'] == 'Population, total']  # Population

# データの前処理
gdp_df = gdp_df[gdp_df['2021 [YR2021]'] != '..']
gdp_df['2021 [YR2021]'] = gdp_df['2021 [YR2021]'].astype(float)

life_exp_df = life_exp_df[life_exp_df['2021 [YR2021]'] != '..']
life_exp_df['2021 [YR2021]'] = life_exp_df['2021 [YR2021]'].astype(float)

population_df = population_df[population_df['2021 [YR2021]'] != '..']
population_df['2021 [YR2021]'] = population_df['2021 [YR2021]'].astype(float)


# GDP, Life expectancy, Populationのデータをマージ
data = gdp_df[['Country Name', 'Country Code', '2021 [YR2021]']].merge(
    life_exp_df[['Country Name', '2021 [YR2021]']], on='Country Name', how='inner', suffixes=('_GDP', '_Life_Expectancy')
).merge(
    population_df[['Country Name', '2021 [YR2021]']], on='Country Name', how='inner'
)
data.rename(columns={'2021 [YR2021]': '2021 [YR2021]_Population',
            'Country Name': 'Country_Name'}, inplace=True)

# NaNを含む行があってもデータをマージできるように処理を行なっていく
region_df.set_index(['alpha-3', 'name'], inplace=True)

# まずは'Country Code'をキーにしてマージ
merged_data = data.merge(
    region_df[['region']], left_on='Country Code', right_on='alpha-3', how='left')

# 'region'がNaNの行については、'Country Name'をキーにしてマージを試みる
merged_data.loc[merged_data['region'].isnull()] = data.merge(
    region_df[['region']], left_on='Country_Name', right_on='name', how='left')

# Country_Nameをインデックスに設定
merged_data.set_index('Country_Name', inplace=True)
merged_data.dropna(inplace=True)

# GDP per capitaを計算
merged_data["GDP per capita"] = merged_data["2021 [YR2021]_GDP"] / \
    merged_data["2021 [YR2021]_Population"]

# 地域ごとに色を割り当てる
unique_regions = merged_data['region'].unique()
region_colors = {region: color for region,
                 color in zip(unique_regions, plt.cm.tab10.colors)}

# バブルチャートを描画
plt.figure(figsize=(10, 10))  # グラフのサイズを指定
for region, color in region_colors.items():
    temp_df = merged_data[merged_data['region'] == region]  # データを地域ごとに分割
    if not temp_df.empty:  # データがある場合のみ描画
        plt.scatter(temp_df['GDP per capita'], temp_df['2021 [YR2021]_Life_Expectancy'],
                    s=temp_df['2021 [YR2021]_Population'] / 1000000, color=color, alpha=0.5)  # バブルチャートを描画

# 地域の色を示す凡例を追加
legend_handles = []
for region, color in region_colors.items():
    plt.scatter([], [], c=color, alpha=0.5, s=100, label=region)
    # Save handles for legend
    legend_handles.append(plt.scatter([], [], c=color, alpha=0.5, s=100))

# 大きさの凡例を追加
populations = [1e6, 1e7, 1e8, 1e9]  # Assuming population in millions
size_legend_handles = []
for pop in populations:
    plt.scatter([], [], c='k', alpha=0.3, s=pop / 1000000,
                label='{:.0e}'.format(pop))  # Format population as integer
    size_legend_handles.append(plt.scatter(
        [], [], c='k', alpha=0.3, s=pop / 1000000))  # Save handles for size legend

# 凡例を表示
regions_legend = plt.legend(handles=legend_handles, labels=[
                            'Asia', 'Europe', 'Africa', 'Oceania', 'Americas'], title="地域", loc='upper left')
plt.legend(handles=size_legend_handles, labels=[
           str(int(pop)) for pop in populations], title='人口', loc='lower right')
plt.gca().add_artist(regions_legend)  # 2つ目の凡例を重ねて表示
plt.xscale('log')  # x軸を対数軸に設定
plt.xlabel('一人あたりGDP [$]', fontsize=18)  # x軸ラベル
plt.ylabel('平均寿命 [年]', fontsize=18)  # y軸ラベル
plt.grid(True)  # グリッド線を表示


# 国名ラベルを追加
for line in range(0, merged_data.shape[0]):
    country = merged_data.index[line]  # 国名
    x = merged_data['GDP per capita'][line]  # 一人あたりGDP
    y = merged_data['2021 [YR2021]_Life_Expectancy'][line]  # 平均寿命
    if not np.isnan(x) and not np.isnan(y):  # NaNでない場合のみラベルを表示
        region = merged_data['region'][line]  # 地域を取得
        if region in region_colors:  # 地域が定義されている場合のみラベルを表示
            plt.text(x + 0.2, y, country,
                     horizontalalignment='left',
                     size='small',
                     color=region_colors[region])  # ラベルを表示

plt.tight_layout()  # レイアウトの設定
plt.savefig("3_3_6_bubble_chart.png", dpi=300)  # 画像として保存
plt.show()  # グラフを表示
