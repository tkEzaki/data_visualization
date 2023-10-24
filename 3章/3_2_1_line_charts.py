import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams['font.size'] = 14


# pandasで読み込む
df = pd.read_csv("gdp_data.csv", thousands=',')  # 千の位のカンマを除去して数値として読み込む

print(df)
# 年ごとのGDPデータとセクターごとのデータ
years = df['年度']
gdp = df['国内総生産(支出側)'] / 1000
sectors = df[['民間最終消費支出', '民間住宅', '民間企業設備', '政府最終消費支出', '公的固定資本形成']] / 1000

fig, ax = plt.subplots(1, 3, figsize=(10, 5))

# 折れ線グラフ
ax[0].plot(years, gdp, color='skyblue')
ax[0].set_title('折れ線グラフ', fontsize=16)
# ax[0].set_xlabel('Year')
ax[0].set_ylabel('国内総生産（支出側） [兆円]')

# エリアチャート
ax[1].fill_between(years, gdp, color='skyblue')
ax[1].set_title('エリアチャート', fontsize=16)
ax[1].set_xlabel('年度')
# ax[1].set_ylabel('GDP')
ax[1].set_ylim(0, 600)

# 積み上げエリアチャート
ax[2].stackplot(years, sectors.transpose(), labels=sectors.columns)
ax[2].set_title('積み上げエリアチャート', fontsize=16)
# ax[2].set_xlabel('Year')
# ax[2].set_ylabel('GDP')
ax[2].set_ylim(0, 600)
ax[2].legend(loc='lower center')

plt.tight_layout()
plt.savefig('3_2_1_line_plots.png', dpi=300)
plt.savefig('3_2_1_line_plots.svg', dpi=300)

plt.show()
