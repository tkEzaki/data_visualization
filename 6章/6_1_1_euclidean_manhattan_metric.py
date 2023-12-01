import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# ポイントの定義
x1, y1 = 1, 3
x2, y2 = 4, 2

# ユークリッド距離の計算
euclidean_distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# マンハッタン距離の計算
manhattan_distance = abs(x2 - x1) + abs(y2 - y1)

# プロット
fig, ax = plt.subplots(figsize=(4, 4))  # 図の準備
ax.scatter([x1, x2], [y1, y2], c='gold')  # 各点のプロット
ax.plot([x1, x2], [y1, y2], c='blue', linestyle='--')  # ユークリッド距離の線
ax.plot([x1, x2], [y1, y1], c='salmon', linestyle='--')  # マンハッタン距離の線
ax.plot([x2, x2], [y1, y2], c='salmon', linestyle='--')  # マンハッタン距離の線

# マンハッタン距離の線のラベル
ax.text((x1 + x2) / 2 + 0.05, y1 + 0.05,
        f'{abs(x2-x1)}', verticalalignment='bottom', horizontalalignment='right', color='salmon')
ax.text(x2 + 0.4, (y1 + y2) / 2 - 0.15,
        f'{abs(y2-y1)}', verticalalignment='bottom', horizontalalignment='right', color='salmon')

# ユークリッド距離の線のラベル
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2
ax.text(mid_x, mid_y - 0.5, r'$\sqrt{10}=$' + f'{euclidean_distance:.2f}',
        verticalalignment='bottom', horizontalalignment='right', color='blue') 

plt.xlabel('x')  # x軸ラベル
plt.ylabel('y')  # y軸ラベル

# x_rangeとy_rangeを0から5に設定
plt.xlim([0, 5])  # x軸の範囲を設定
plt.ylim([0, 5])  # y軸の範囲を設定

plt.savefig('6_1_1_euclidean_manhattan_metric.png',
            bbox_inches='tight', dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
