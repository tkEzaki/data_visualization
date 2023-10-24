import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams['font.size'] = 14

np.random.seed(0)
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
            if hour == 12 or hour == 17:
                visitor_count.append(random.randint(50, 80))
            else:
                visitor_count.append(int(random.randint(20, 50) * 1.4))
        elif day in ['土', '日']:
            if 11 <= hour <= 17:
                visitor_count.append(random.randint(70, 100))
            else:
                visitor_count.append(random.randint(30, 60))
        else:
            if hour == 12 or hour == 17:
                visitor_count.append(random.randint(50, 80))
            else:
                visitor_count.append(random.randint(20, 50))
    return visitor_count


# 各日、各時刻の来客数をパターンに基づいて生成
for day in days_of_week:
    df_visitor_count.loc[day] = generate_visitor_count_with_wednesday(day)

# 折れ線グラフを描画
plt.figure(figsize=(10, 5))
for day in days_of_week:
    linestyle = '-'
    color = 'gray'
    if day == '水':
        color = 'red'
    elif day in ['土', '日']:
        linestyle = '--'
    plt.plot(hours_of_day, df_visitor_count.loc[day], label=day, marker='o', linestyle=linestyle, color=color)

plt.xlabel('時刻')
plt.ylabel('来客数')
plt.xticks(hours_of_day)
plt.grid(True)

# 凡例をプロットエリアの外に配置
# plt.legend(title='曜日', loc='upper right', bbox_to_anchor=(1.135, 1))

plt.savefig('8_1_4_legend_example_without_legend.png', dpi=300)
plt.show()
