import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import pandas as pd

plt.rcParams["font.size"] = 14

# ユーザー数
num_users = 100

# 各ペア間のリプライ数をランダムに生成
np.random.seed(0)
replies_sent = np.zeros(num_users)
replies_received = np.zeros(num_users)

for i in range(num_users):
    # パターンをランダムに選択
    pattern = np.random.choice(['moderate', 'one_sided_few', 'one_sided_many'])
    if pattern == 'moderate':
        # お互いにそれなりの回数を送り合っている
        replies_sent[i] = np.random.randint(low=10, high=30)
        replies_received[i] = replies_sent[i] + np.random.randint(low=-3, high=3)
        replies_sent[num_users - i - 1] = replies_received[i]
        replies_received[num_users - i - 1] = replies_sent[i]
    elif pattern == 'one_sided_few':
        # 片方が全く送らずにもう片方が０～３回送っている
        replies_sent[i] = np.random.randint(low=0, high=4)
        replies_received[i] = 0
        replies_sent[num_users - i - 1] = replies_received[i]
        replies_received[num_users - i - 1] = replies_sent[i]
    else:  # pattern == 'one_sided_many'
        # 片方が全く送らずにもう片方が２０回くらい送っている
        replies_sent[i] = np.random.randint(low=10, high=30)
        replies_received[i] = 0
        replies_sent[num_users - i - 1] = replies_received[i]
        replies_received[num_users - i - 1] = replies_sent[i]

weights_1 = np.random.normal(60, 2, 50)  # 平均60、分散10の正規分布
weights_2 = weights_1 + np.random.normal(-1, 0.5, 50)  # 平均-1、分散0.5の正規分布

# データフレームにまとめる
df = pd.DataFrame({
    'Sent': replies_sent,
    'Received': replies_received,
})

df_weights = pd.DataFrame({
    'Weight1': weights_1,
    'Weight2': weights_2,
})

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# 散布図の描画
axs[1].scatter(df['Sent'], df['Received'], color='lightblue', label='User Pair')
# axs[0].set_xlabel('Replies Sent')
# axs[0].set_ylabel('Replies Received')

# y=xの直線を描画
lims = [
    np.min([axs[1].get_xlim(), axs[1].get_ylim()]),  # min of both axes
    np.max([axs[1].get_xlim(), axs[1].get_ylim()]),  # max of both axes
]
axs[1].plot(lims, lims, color='black', label='y=x')
axs[1].set_xlim(lims)
axs[1].set_ylim(lims)
axs[1].set_aspect('equal', 'box')
axs[1].set_ylabel('受信したリプライ数', fontsize=18)
axs[1].set_xlabel('送信したリプライ数', fontsize=18)

# axs[0].legend()
axs[1].grid(True)

# 散布図の描画 for weights
axs[0].scatter(df_weights['Weight1'], df_weights['Weight2'], color='orange', label='Weight Pair')
# axs[1].set_xlabel('Weight1')
# axs[1].set_ylabel('Weight2')

# y=xの直線を描画
lims = [
    np.min([axs[0].get_xlim(), axs[0].get_ylim()]),  # min of both axes
    np.max([axs[0].get_xlim(), axs[0].get_ylim()]),  # max of both axes
]
axs[0].plot(lims, lims, color='black', label='y=x')
axs[0].set_xlim(lims)
axs[0].set_ylim(lims)
axs[0].set_ylabel('一か月後体重 [kg]', fontsize=18)
axs[0].set_xlabel('実験開始時体重 [kg]', fontsize=18)
axs[0].set_aspect('equal', 'box')

# axs[1].legend()
axs[0].grid(True)

# plt.subplots_adjust(wspace=0.3)
plt.tight_layout()
plt.savefig('3_3_4_vs_x=y.png', dpi=300)
plt.savefig('3_3_4_vs_x=y.svg', dpi=300)
plt.show()
