import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# シードの固定
np.random.seed(0)

# パラメータ設定
n = 10
mean_income = 400  # 平均収入
mean_log = np.log(mean_income)  # 対数正規分布の平均（ログスケール）
std_dev_log = 0.5  # 対数正規分布の標準偏差（ログスケール）

# 対数正規分布から収入をサンプリング
unequal_incomes = np.random.lognormal(mean_log, std_dev_log, n)


# 完全均一な収入を作成
mean_income = np.mean(unequal_incomes)
equal_incomes = np.full(n, mean_income)

# タイル指数（Theil Index）を計算する関数


def calc_theil_index(incomes):
    mean_income = np.mean(incomes)
    return np.sum((incomes / mean_income) * np.log(incomes / mean_income)) / n


# タイル指数を計算
unequal_theil = calc_theil_index(unequal_incomes)  # 不均一な収入のケース
equal_theil = calc_theil_index(equal_incomes)  # 均一な収入のケース

# サブプロットで描画
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# 縦軸のレンジを決定
y_max = max(np.max(unequal_incomes), np.max(
    equal_incomes)) * 1.1  # 1.1は余裕を持たせるため

# 不均一な収入のプロット
axes[0].bar(range(n), unequal_incomes, color='skyblue')  # 棒グラフを描画
axes[0].set_ylim(0, y_max)  # 縦軸の範囲を設定
axes[0].set_title(f'ばらついた収入分布 (タイル指数: {unequal_theil:.4f})')  # タイトル
axes[0].set_xlabel('')  # x軸ラベル
axes[0].set_ylabel('収入 [万円]')  # y軸ラベル
labels = [chr(65 + i) for i in range(n)]  # A, B, C, ... とラベルを作成
axes[0].set_xticks(range(n))  # x軸の目盛りを設定
axes[0].set_xticklabels(labels)  # x軸の目盛りのラベルを設定

# 均一な収入のプロット
axes[1].bar(range(n), equal_incomes, color='salmon')  # 棒グラフを描画
axes[1].set_ylim(0, y_max)  # 縦軸の範囲を設定
axes[1].set_title(f'一様な収入分布 (タイル指数: {equal_theil:.4f})')  # タイトル
axes[1].set_xlabel('')  # x軸ラベル
axes[1].set_ylabel('収入 [万円]')  # y軸ラベル
axes[1].set_xticks(range(n))  # x軸の目盛りを設定
axes[1].set_xticklabels(labels)  # x軸の目盛りのラベルを設定

plt.tight_layout()  # レイアウトの調整
plt.savefig('5_3_5_theil_index.png', dpi=300)  # 画像を保存
plt.show()  # 画面に表示
