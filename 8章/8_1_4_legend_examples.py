import pandas as pd  # データフレーム操作のためのPandas
import numpy as np  # 数値計算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ
plt.rcParams['font.size'] = 15  # プロットのフォントサイズを15に設定

np.random.seed(0)  # 乱数のシードを固定

# 月曜日から日曜日までの7日間
days_of_week = ['月', '火', '水', '木', '金', '土', '日']

# 各時刻
hours_of_day = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# データフレームを作成
df_visitor_count = pd.DataFrame(index=days_of_week, columns=hours_of_day)

# パターンに基づいて来客数を生成する関数（水曜日の特別処理を含む）
def generate_visitor_count_with_wednesday(day):
    visitor_count = []
    for hour in hours_of_day:
        if day == '水':
            # 水曜日は12時と17時以外の時間に、普段の平日より1.5倍の来客
            if hour == 12 or hour == 17:
                visitor_count.append(np.random.randint(50, 80))
            else:
                visitor_count.append(int(np.random.randint(20, 50) * 1.4))
        elif day in ['土', '日']:
            # 休日は11:00 - 17:00 までまんべんなく多い
            if 11 <= hour <= 17:
                visitor_count.append(np.random.randint(70, 100))
            else:
                visitor_count.append(np.random.randint(30, 60))
        else:
            # 平日は12時と17時が多い
            if hour == 12 or hour == 17:
                visitor_count.append(np.random.randint(50, 80))
            else:
                visitor_count.append(np.random.randint(20, 50))
    return visitor_count


# 各日、各時刻の来客数をパターンに基づいて生成
for day in days_of_week:
    df_visitor_count.loc[day] = generate_visitor_count_with_wednesday(day)

# 折れ線グラフを描画
plt.figure(figsize=(10, 5))
for day in days_of_week:
    plt.plot(hours_of_day, df_visitor_count.loc[day], label=day, marker='o')

plt.xlabel('時刻')  # x軸ラベル
plt.ylabel('来客数')  # y軸ラベル
plt.xticks(hours_of_day)  # x軸の目盛を設定
plt.legend(title='曜日', loc='upper right', bbox_to_anchor=(1.135, 1), fontsize=14)  # 凡例を表示
plt.grid(True)  # グリッドを表示

plt.savefig('8_1_4_1_legend_example_with_legend_box.png', dpi=300)  # 図の保存
plt.show() # 図の表示


# 折れ線グラフを描画
plt.figure(figsize=(10, 5))
for day in days_of_week:
    plt.plot(hours_of_day, df_visitor_count.loc[day], label=day, marker='o')

plt.xlabel('時刻')  # x軸ラベル
plt.ylabel('来客数')  # y軸ラベル
plt.xticks(hours_of_day)  # x軸の目盛を設定
plt.grid(True)  # グリッドを表示

plt.savefig('8_1_4_2_legend_example_without_legend_box.png', dpi=300)  # 図の保存
plt.show() # 図の表示
