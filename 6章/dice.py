# 必要なライブラリをインポート
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = 'Yu Gothic'
# plt.rcParams['font.size'] = 12

# 合計が1になるように確率分布を調整
joint_prob = np.array([
    [1 / 36 - 1 / 72, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5],
    [1 / 36 + 1 / 72 / 5, 1 / 36 - 1 / 72, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5],
    [1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 - 1 / 72, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5],
    [1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 - 1 / 72, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5],
    [1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 - 1 / 72, 1 / 36 + 1 / 72 / 5],
    [1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 + 1 / 72 / 5, 1 / 36 - 1 / 72]
])
joint_prob = joint_prob / np.sum(joint_prob)

# 合計が1になるか確認
print("Sum of joint probabilities:", np.sum(joint_prob))

# サンプリング（1000回）
np.random.seed(0)
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
sns.heatmap(heatmap_data_sampled, annot=True, fmt=".3f", cmap='coolwarm', xticklabels=range(1, 7), yticklabels=range(1, 7))
# plt.title("二つのサイコロを1,000,000回振った結果のまとめ")
plt.xlabel("サイコロBの出目")
plt.ylabel("サイコロAの出目")
plt.tight_layout()
plt.savefig("dice_heatmap.png", dpi=300)
plt.show()

# サイコロAが1が出たときのサイコロBの結果を棒グラフで描画
plt.figure(figsize=(4, 4))
# データの集計
counts, _ = np.histogram(samples_die2[samples_die1 == 1], bins=range(1, 8))
# 棒グラフの描画
plt.bar(range(1, 7), counts / np.sum(counts), color='blue')
plt.xticks(range(1, 7))
# plt.title("Bar Plot of Die 2 when Die 1 rolls a 1 (Sampled from P(X, Y))")
plt.xlabel("サイコロBの出目")
plt.ylabel("相対頻度")
plt.tight_layout()
plt.savefig("dice_bar.png", dpi=300)
plt.show()
