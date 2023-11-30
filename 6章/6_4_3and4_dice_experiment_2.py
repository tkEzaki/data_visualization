import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# 初期設定
np.random.seed(0)
n_trials = 100000

# ボーナスタイムと通常時の確率
bonus_prob = [1 / 11, 2 / 11, 2 / 11, 2 / 11, 2 / 11, 2 / 11]
normal_prob = [2 / 11, 9 / 55, 9 / 55, 9 / 55, 9 / 55, 9 / 55]

# 結果の格納用
heatmap_data = np.zeros((6, 6))
bonus_time_die1 = []
bonus_time_die2 = []
samples_die1 = []
samples_die2 = []

# ボーナスタイムフラグ
bonus_time = False

# サイコロを振る
for _ in range(n_trials):
    if bonus_time:
        die1 = np.random.choice(range(1, 7), p=bonus_prob)
        die2 = np.random.choice(range(1, 7), p=bonus_prob)
        samples_die1.append(die1)
        samples_die2.append(die2)
        bonus_time_die1.append(die1)
        bonus_time_die2.append(die2)
    else:
        die1 = np.random.choice(range(1, 7), p=normal_prob)
        die2 = np.random.choice(range(1, 7), p=normal_prob)
        samples_die1.append(die1)
        samples_die2.append(die2)

    # 結果をヒートマップ用に集計
    heatmap_data[die1 - 1, die2 - 1] += 1

    # ボーナスタイムフラグの更新
    bonus_time = (die1 == 1)

# ヒートマップデータを確率に変換
heatmap_data = heatmap_data / np.sum(heatmap_data)

# ヒートマップを描画
plt.figure(figsize=(4.5, 4))
sns.heatmap(heatmap_data, annot=True, fmt=".3f", annot_kws={'size': 10}, cmap='coolwarm', xticklabels=range(1, 7), yticklabels=range(1, 7), vmin=0.0139, vmax=0.031)
# plt.title("Dice Roll Heatmap")
plt.xlabel("サイコロBの出目")
plt.ylabel("サイコロAの出目")
plt.tight_layout()
plt.savefig("6_4_3_1_dice_experiment_2_heatmap.png", dpi=300)
plt.savefig("6_4_3_1_dice_experiment_2_heatmap.svg", dpi=300)

plt.show()


# サイコロAが1が出たときのサイコロBの結果を棒グラフで描画
plt.figure(figsize=(4, 4))
samples_die1 = np.array(samples_die1)
samples_die2 = np.array(samples_die2)
# データの集計
counts, _ = np.histogram(samples_die2[samples_die1 == 1], bins=range(1, 8))
# print(samples_die1, samples_die2)
# 棒グラフの描画
plt.bar(range(1, 7), counts / np.sum(counts), color='blue')
plt.xticks(range(1, 7))
# plt.title("Bar Plot of Die 2 when Die 1 rolls a 1 (Sampled from P(X, Y))")
plt.xlabel("サイコロBの出目")
plt.ylabel("相対頻度")
plt.tight_layout()
plt.savefig("6_4_3_2_dice_experiment_2_bar.png", dpi=300)
plt.savefig("6_4_3_2_dice_experiment_2_bar.svg", dpi=300)

plt.show()


# サンプルされた二つのサイコロの時系列を折れ線グラフで示す
# 初めの100個のサンプルだけ描画
plt.figure(figsize=(6, 3))

# サイコロAとサイコロBの時系列を描画
plt.plot(range(1, 51), bonus_time_die1[:50], label='Die 1', marker='o', linestyle='-')
plt.plot(range(1, 51), bonus_time_die2[:50], label='Die 2', marker='o', linestyle='-')

# サイコロAで1が出た場合（ボーナスタイム）に背景色をつける
for i, val in enumerate(bonus_time_die1[:49], start=1):  # 最初の99個のサンプルを確認
    if val == 1:
        plt.axvspan(i + 0.5, i + 1.5, color='yellow', alpha=0.3)

plt.xlabel("試行回数")
plt.ylabel("サイコロの出目")
# plt.title("Time Series of Die 1 and Die 2 (First 100 samples)")
# plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("6_4_4_1_dice_experiment_2_time_series.png", dpi=300)
plt.savefig("6_4_4_1_dice_experiment_2_time_series.svg", dpi=300)

plt.show()


# ボーナスタイム時の棒グラフを描画
plt.figure(figsize=(6, 3))

# サイコロAの棒グラフ
plt.subplot(1, 2, 1)
counts1, _ = np.histogram(bonus_time_die1, bins=range(1, 8))
plt.bar(range(1, 7), counts1 / np.sum(counts1), alpha=0.7, color='blue', edgecolor='black')
plt.xticks(range(1, 7))
# plt.title("Bar Plot of Die 1 during Bonus Time")
plt.xlabel("サイコロAの出目")
plt.ylabel("相対頻度")

# サイコロBの棒グラフ
plt.subplot(1, 2, 2)
counts2, _ = np.histogram(bonus_time_die2, bins=range(1, 8))
plt.bar(range(1, 7), counts2 / np.sum(counts2), alpha=0.7, color='red', edgecolor='black')
plt.xticks(range(1, 7))
# plt.title("Bar Plot of Die 2 during Bonus Time")
plt.xlabel("サイコロBの出目")
plt.ylabel("相対頻度")

plt.tight_layout()
plt.savefig("6_4_4_2_dice_experiment_2_conditioned_bar.png", dpi=300)
plt.savefig("6_4_4_2_dice_experiment_2_conditioned_bar.svg", dpi=300)

plt.show()
