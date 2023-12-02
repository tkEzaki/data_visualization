import pandas as pd  # データ操作のためのPandas
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定


# pandasで読み込む
df = pd.read_csv("data\\gdp_data.csv", thousands=',')  # 千の位のカンマを除去して数値として読み込む
print(df.head())  # 先頭5行を表示

# 年ごとのGDPデータとセクターごとのデータ
years = df['年度']  # 年度
gdp = df['国内総生産(支出側)'] / 1000  # 国内総生産（支出側）を兆円単位に変換
sectors = df[['民間最終消費支出', '民間住宅', '民間企業設備',
              '政府最終消費支出', '公的固定資本形成']] / 1000  # 各セクターを兆円単位に変換


fig, ax = plt.subplots(1, 3, figsize=(10, 5))  # サブプロットの作成

# 折れ線グラフ
ax[0].plot(years, gdp, color='skyblue')  # 折れ線グラフを描画
ax[0].set_title('折れ線グラフ', fontsize=16)  # タイトル
ax[0].set_ylabel('国内総生産（支出側） [兆円]')  # y軸ラベル

# エリアチャート
ax[1].fill_between(years, gdp, color='skyblue')  # エリアチャートを描画
ax[1].set_title('エリアチャート', fontsize=16)  # タイトル
ax[1].set_xlabel('年度')  # x軸ラベル
ax[1].set_ylim(0, 600)  # y軸の範囲を設定

# 積み上げエリアチャート
ax[2].stackplot(years, sectors.transpose(),
                labels=sectors.columns)  # 積み上げエリアチャートを描画
ax[2].set_title('積み上げエリアチャート', fontsize=16)  # タイトル
ax[2].set_ylim(0, 600)  # y軸の範囲を設定
ax[2].legend(loc='lower center')  # 凡例を表示


plt.tight_layout()  # レイアウトの設定
plt.savefig('3_2_1_line_plots.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示
