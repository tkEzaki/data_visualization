import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib

# データの生成
np.random.seed(0)
people = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
data_evening = {
    '人': people,
    '夕方': np.random.normal(36.0, 0.2, size=7),
}
data_morning = {
    '人': people,
    '早朝': np.random.normal(36.0, 0.2, size=7),
}
df_evening = pd.DataFrame(data_evening)
df_morning = pd.DataFrame(data_morning)

# プロットの設定
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# マーカーのみの折れ線グラフをプロットする関数


def plot_line(ax, df, time_of_day, marker, line=''):
    ax.plot(df['人'], df[time_of_day], marker=marker, linestyle=line, label=time_of_day)
    # ax.set_title('体温推移', fontsize=14)
    # ax.legend()
    ax.set_ylabel('体温 [℃]', fontsize=14)
    ax.tick_params(labelsize=14)
    ax.legend(fontsize=14)


# マーカーのみの折れ線グラフをプロット
plot_line(axs[0], df_evening, '夕方', 'o')
plot_line(axs[0], df_morning, '早朝', 's')

# マーカーと折れ線のグラフをプロット
plot_line(axs[1], df_evening, '夕方', 'o', '-')
plot_line(axs[1], df_morning, '早朝', 's', '--')

# plt.subplots_adjust(wspace=0.3)  # サブプロット間の間隔を調整
# axs[0].legend(fontsize=14)
plt.tight_layout()
# plt.show()
plt.savefig('2_2_3_point_lineplot.png', dpi=300)
plt.savefig('2_2_3_point_lineplot.svg', dpi=300)
