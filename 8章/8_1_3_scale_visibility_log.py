import pandas as pd  # データフレーム操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ


plt.rcParams['font.size'] = 16  # プロットのフォントサイズを16に設定

# ファイルを読み込む
# data downloaded from https://covid19.who.int/data
# file_path = 'WHO-COVID-19-global-data.csv'
file_path = 'data\\covid_data_dummy.csv'  # これはダミーデータ
df = pd.read_csv(file_path)

# 日本、アメリカ、中国のデータを抜き出す
selected_countries = ['Japan', 'United States of America', 'China']
filtered_df = df[df['Country'].isin(selected_countries)]

# 日付をDatetime形式に変換
filtered_df['Date_reported'] = pd.to_datetime(filtered_df['Date_reported'])

# 7日の移動平均を計算
filtered_df['14_day_avg'] = filtered_df.groupby(
    'Country')['New_cases'].transform(lambda x: x.rolling(14).mean())

# 通常の縦軸
plt.figure(figsize=(10, 5))
for country in selected_countries:
    country_data = filtered_df[filtered_df['Country'] == country]
    plt.plot(country_data['Date_reported'],
             country_data['New_cases'], label=country)

plt.legend()  # 凡例を表示
plt.grid(True)  # グリッドを表示
plt.ticklabel_format(style='plain', axis='y')  # 縦軸の目盛を指数表記にしない
plt.gca().get_yaxis().set_major_formatter(
    plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))  # 縦軸の目盛にカンマを入れる
plt.xticks(rotation=30, ha='right')  # x軸の目盛を30度回転
plt.ylabel('新規感染者数')  # y軸ラベル


plt.tight_layout()  # レイアウトの設定
plt.savefig('8_1_3_1_normal_axis_plot.png', dpi=300)  # 図の保存
plt.show()  # 図の表示


# 対数縦軸
plt.figure(figsize=(10, 5))
for country in selected_countries:
    country_data = filtered_df[filtered_df['Country'] == country]
    plt.plot(country_data['Date_reported'],
             country_data['New_cases'], label=country)

plt.yscale('log')  # 縦軸を対数にする
plt.legend()  # 凡例を表示
plt.grid(True)  # グリッドを表示
plt.gca().get_yaxis().set_major_formatter(
    plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))  # 縦軸の目盛にカンマを入れる
plt.xticks(rotation=30, ha='right')  # x軸の目盛を30度回転
plt.ylabel('新規感染者数')  # y軸ラベル

plt.tight_layout()  # レイアウトの設定
plt.savefig('8_1_3_2_log_axis_plot.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
