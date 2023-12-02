import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# データの生成
x = np.linspace(0.25, 3.75, 400)
y1 = np.cos(4 * (x - 0.25))
y2 = np.cos(3 * (x - 0.25)) + 0.5

# 図の生成
fig, ax = plt.subplots(figsize=(8, 8))

# ラインプロットの描画
ax.plot(x, y1, label='Signal 1', color='blue')
ax.plot(x, y2, label="Signal 2", color='red')

# 散布図の描画
scatter_x = np.linspace(0.25, 3.75, 50)
scatter_y1 = np.cos(4 * (scatter_x - 0.25)) + np.random.normal(0, 0.2, size=scatter_x.shape)
scatter_y2 = np.cos(3 * (scatter_x - 0.25)) + 0.5 + np.random.normal(0, 0.2, size=scatter_x.shape)
ax.scatter(scatter_x, scatter_y1, color='blue')
ax.scatter(scatter_x, scatter_y2, color='red')


# グリッドの表示
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# 軸のラベル
ax.set_xlabel("X軸ラベル")
ax.set_ylabel("Y軸ラベル")
ax.set_title("図のタイトル")

ax.set_xticks([0, 1, 2, 3, 4])

# 凡例の表示
ax.legend()

# 図の表示
plt.savefig('A_1_6_name_of_components.png', bbox_inches='tight', dpi=300)
plt.show()