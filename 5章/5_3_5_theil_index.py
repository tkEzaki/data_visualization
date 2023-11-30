import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams['font.size'] = 14
# シードの固定
np.random.seed(0)

# パラメータ設定
n = 10
mean_income = 400  # 平均収入
mean_log = np.log(mean_income)
std_dev_log = 0.5  # 対数正規分布の標準偏差（ログスケールで）

# 対数正規分布から収入をサンプリング
unequal_incomes = np.random.lognormal(mean_log, std_dev_log, n)


# 完全均一な収入を作成
mean_income = np.mean(unequal_incomes)
equal_incomes = np.full(n, mean_income)

# タイル指数（Theil Index）を計算


def calc_theil_index(incomes):
    mean_income = np.mean(incomes)
    return np.sum((incomes / mean_income) * np.log(incomes / mean_income)) / n


unequal_theil = calc_theil_index(unequal_incomes)
equal_theil = calc_theil_index(equal_incomes)

# サブプロットで描画
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# 縦軸のレンジを決定
y_max = max(np.max(unequal_incomes), np.max(equal_incomes)) * 1.1  # 1.1は余裕を持たせるため

# 不均一な収入のプロット
axes[0].bar(range(n), unequal_incomes, color='skyblue')
axes[0].set_ylim(0, y_max)
axes[0].set_title(f'ばらついた収入分布 (タイル指数: {unequal_theil:.4f})')
axes[0].set_xlabel('')
axes[0].set_ylabel('収入 [万円]')
labels = [chr(65 + i) for i in range(n)]
axes[0].set_xticks(range(n))
axes[0].set_xticklabels(labels)

# 均一な収入のプロット
axes[1].bar(range(n), equal_incomes, color='salmon')
axes[1].set_ylim(0, y_max)
axes[1].set_title(f'一様な収入分布 (タイル指数: {equal_theil:.4f})')
axes[1].set_xlabel('')
axes[1].set_ylabel('収入 [万円]')
axes[1].set_xticks(range(n))
axes[1].set_xticklabels(labels)
plt.tight_layout()

plt.savefig('5_3_5_theil_index.png', dpi=300)
plt.savefig('5_3_5_theil_index.svg', dpi=300)

plt.show()
