import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib


plt.rcParams['font.size'] = 14

# ファイルを読み込む
file_path = 'WHO-COVID-19-global-data.csv'  # data downloaded from https://covid19.who.int/data

df = pd.read_csv(file_path)

# 日本、アメリカ、中国のデータを抜き出す
selected_countries = ['Japan', 'United States of America', 'China']
filtered_df = df[df['Country'].isin(selected_countries)]

# 日付をDatetime形式に変換
filtered_df['Date_reported'] = pd.to_datetime(filtered_df['Date_reported'])

# 7日の移動平均を計算
filtered_df['14_day_avg'] = filtered_df.groupby('Country')['New_cases'].transform(lambda x: x.rolling(14).mean())

# 通常の縦軸
plt.figure(figsize=(10, 5))
for country in selected_countries:
    country_data = filtered_df[filtered_df['Country'] == country]
    plt.plot(country_data['Date_reported'], country_data['New_cases'], label=country)

# plt.ylabel('新規感染者数')
plt.legend()
plt.grid(True)
plt.ticklabel_format(style='plain', axis='y')
plt.gca().get_yaxis().set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))  # 縦軸の目盛にカンマを入れる

plt.tight_layout()
plt.savefig('8_1_3_normal_axis_plot.png', dpi=300)
plt.savefig('8_1_3_normal_axis_plot.svg', dpi=300)
plt.close()

# 対数縦軸
plt.figure(figsize=(10, 5))
for country in selected_countries:
    country_data = filtered_df[filtered_df['Country'] == country]
    plt.plot(country_data['Date_reported'], country_data['New_cases'], label=country)

# plt.ylabel('新規感染者数 (対数)')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.gca().get_yaxis().set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))  # 縦軸の目盛にカンマを入れる

plt.tight_layout()
plt.savefig('8_1_3_log_axis_plot.png', dpi=300)
plt.savefig('8_1_3_log_axis_plot.svg', dpi=300)

plt.close()
