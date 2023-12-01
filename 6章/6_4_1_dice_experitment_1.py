import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import seaborn as sns  # グラフ作成のためのSeaborn
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams['font.size'] = 13  # プロットのフォントサイズを13に設定

# 確率分布を準備
joint_prob = np.array([
    [1 / 36 - 1 / 72, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 /
        36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5],
    [1 / 36 + 1 / 72 / 5, 1 / 36 - 1 / 72, 1 / 36 + 1 / 72 / 5, 1 /
        36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5],
    [1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 - 1 / 72, 1 /
        36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5],
    [1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5,
        1 / 36 - 1 / 72, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5],
    [1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5,
        1 / 36 + 1 / 72 / 5, 1 / 36 - 1 / 72, 1 / 36 + 1 / 72 / 5],
    [1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5,
        1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 - 1 / 72]
])
joint_prob = joint_prob / np.sum(joint_prob)

# サンプリング（1000回）
np.random.seed(0)  # 再現性のため
# サンプルをjoint_probに従って1000回サンプリング
samples = np.random.choice(range(36), p=joint_prob.flatten(), size=1000000)

# サンプリングされた値を(X, Y)ペアに変換
samples_die1 = samples // 6 + 1
samples_die2 = samples % 6 + 1

# 結果を集計する（ヒートマップ用）
heatmap_data_sampled = np.zeros((6, 6))
for roll1, roll2 in zip(samples_die1, samples_die2):
    heatmap_data_sampled[roll1 - 1, roll2 - 1] += 1 / 1000000

# ヒートマップを描画
plt.figure(figsize=(4.5, 4))
sns.heatmap(heatmap_data_sampled, annot=True, fmt=".3f", annot_kws={
            "size": 10}, cmap='coolwarm', xticklabels=range(1, 7), yticklabels=range(1, 7))

plt.xlabel("サイコロBの出目")  # x軸ラベルを設定
plt.ylabel("サイコロAの出目")  # y軸ラベルを設定
plt.tight_layout()  # レイアウトの設定
plt.savefig("6_4_1_1_dice_experiment_1_heatmap.png", dpi=300)  # 図の保存
plt.show()  # 図の表示

# サイコロAが1が出たときのサイコロBの結果を棒グラフで描画
plt.figure(figsize=(4, 4))
# データの集計
counts, _ = np.histogram(samples_die2[samples_die1 == 1], bins=range(1, 8))
# 棒グラフの描画
plt.bar(range(1, 7), counts / np.sum(counts), color='blue')  # 相対頻度を計算してから描画
plt.xticks(range(1, 7))  # x軸の目盛りを設定
plt.xlabel("サイコロBの出目")  # x軸ラベルを設定
plt.ylabel("相対頻度")  # y軸ラベルを設定
plt.tight_layout()  # レイアウトの設定
plt.savefig("6_4_1_2_dice_experiment_1_bar.png", dpi=300)  # 図の保存
plt.show()  # 図の表示
