import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize

# 設定
cmap = plt.get_cmap('jet')  # カラーマップを設定
norm = Normalize(vmin=-3, vmax=3)  # カラーマップの範囲を設定
n_components = 3  # 仮の値
cmap_state = ListedColormap(cmap(norm(np.arange(n_components))))  # 隠れ状態のカラーマップを設定

# カラーマップの表示
fig, ax = plt.subplots(1, 1, figsize=(5, 2),
                       dpi=80, sharex=True,
                       sharey=True)

# カラーバーの表示
cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=cmap_state), ax=ax)
cbar.set_ticks(np.linspace(0, 1, n_components))
cbar.set_ticklabels(range(n_components))
plt.show()
