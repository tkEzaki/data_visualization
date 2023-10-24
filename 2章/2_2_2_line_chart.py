import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import japanize_matplotlib

# データの生成
np.random.seed(0)
days = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
data = {
    '曜日': days,
    'Aさん': np.random.normal(36.0, 0.2, size=7),
    'Bさん': np.random.normal(36.0, 0.2, size=7),
}
df = pd.DataFrame(data)

# プロットの設定
fig, ax = plt.subplots(figsize=(8, 4))

# 折れ線グラフをプロットする関数


def plot_line(ax, df, person, marker, linestyle):
    ax.plot(df['曜日'], df[person], marker=marker, linestyle=linestyle, label=person)
    # ax.legend()
    ax.tick_params(labelsize=12)


# AさんとBさんの体温推移をプロット
plot_line(ax, df, 'Aさん', 'o', '-')
plot_line(ax, df, 'Bさん', 's', '--')

ax.set_ylabel('体温 [℃]', fontsize=14)
ax.legend(fontsize=14)
# plt.show()
plt.savefig('2_2_2_line_plot.png', dpi=300)
plt.savefig('2_2_2_line_plot.svg', dpi=300)
