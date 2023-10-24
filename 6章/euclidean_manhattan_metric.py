import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Yu Gothic'

# ポイントの定義
x1, y1 = 1, 3
x2, y2 = 4, 2

# ユークリッド距離の計算
euclidean_distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# マンハッタン距離の計算
manhattan_distance = abs(x2 - x1) + abs(y2 - y1)

# プロット
fig, ax = plt.subplots(figsize=(4, 4))
ax.scatter([x1, x2], [y1, y2], c='gold') #, label='Points')
ax.plot([x1, x2], [y1, y2], c='blue', linestyle='--')  #, label=f'ユークリッド距離')
ax.plot([x1, x2], [y1, y1], c='salmon', linestyle='--')  #, label='マンハッタン距離')
ax.plot([x2, x2], [y1, y2], c='salmon', linestyle='--')

# マンハッタン距離の線のラベル
ax.text((x1+x2)/2+0.05, y1+0.05, f'{abs(x2-x1)}', verticalalignment='bottom', horizontalalignment='right', color='salmon')
ax.text(x2+0.2, (y1+y2)/2-0.15, f'{abs(y2-y1)}', verticalalignment='bottom', horizontalalignment='right', color='salmon')

# ユークリッド距離の線のラベル
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2
ax.text(mid_x, mid_y - 0.5,  r'$\sqrt{10}=$' + f'{euclidean_distance:.2f}', verticalalignment='bottom', horizontalalignment='right', color='blue')

# グリッドとラベルの設定
# ax.grid(True)
# ax.legend()

plt.xlabel('x')
plt.ylabel('y')

# x_rangeとy_rangeを0から5に設定
plt.xlim([0, 5])
plt.ylim([0, 5])

plt.savefig('euclidean_manhattan_metric.png', bbox_inches='tight', dpi=300)
plt.show()
