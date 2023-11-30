import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# シード値の設定
np.random.seed(42)


# 書籍の数
n_books = 100

# Aさんのレビュー
a_scores = np.random.normal(loc=60, scale=15, size=n_books).astype(int)
a_scores = np.clip(a_scores, 0, 100)  # 0から100の範囲にクリップ

# Bさんのレビュー（Aさんと高い相関）
b_scores = a_scores + np.random.normal(loc=0, scale=10, size=n_books).astype(int)
b_scores = np.clip(b_scores, 0, 100)  # 0から100の範囲にクリップ

# Cさんのレビュー（Aさんと緩い逆相関）
c_scores = 100 - a_scores + np.random.normal(loc=0, scale=20, size=n_books).astype(int)
c_scores = np.clip(c_scores, 0, 100)  # 0から100の範囲にクリップ

# show scores as a table
print('Aさんのレビュー\tBさんのレビュー\tCさんのレビュー')
for a, b, c in zip(a_scores, b_scores, c_scores):
    print(f'{a}\t\t\t{b}\t\t\t{c}')

# 相関係数の計算
corr_ab = np.corrcoef(a_scores, b_scores)[0, 1]
corr_ac = np.corrcoef(a_scores, c_scores)[0, 1]

# プロット
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
sns.regplot(x=a_scores, y=b_scores, ax=axes[0], color='blue')
axes[0].set_title(f'AさんとBさんの類似度 $r$ = {corr_ab:.2f}')
axes[0].set_xlabel('Aさんによる評価')
axes[0].set_ylabel('Bさんによる評価')

sns.regplot(x=a_scores, y=c_scores, ax=axes[1], color='red')
axes[1].set_title(f'AさんとCさんの類似度 $r$ = {corr_ac:.2f}')
axes[1].set_xlabel('Aさんによる評価')
axes[1].set_ylabel('Cさんによる評価')

# print cosine similarity between A and B
a_scores_rel = a_scores - np.mean(a_scores)
b_scores_rel = b_scores - np.mean(b_scores)
c_scores_rel = c_scores - np.mean(c_scores)

cos_sim_ab = np.dot(a_scores_rel, b_scores_rel) / (np.linalg.norm(a_scores_rel) * np.linalg.norm(b_scores_rel))
cos_sim_ac = np.dot(a_scores_rel, c_scores_rel) / (np.linalg.norm(a_scores_rel) * np.linalg.norm(c_scores_rel))
print(f'コサイン類似度（AさんとBさん）: {cos_sim_ab:.2f}')
print(f'コサイン類似度（AさんとCさん）: {cos_sim_ac:.2f}')


plt.tight_layout()
plt.savefig('6_3_1_correlation_similarity.png', dpi=300)
plt.savefig('6_3_1_correlation_similarity.svg', dpi=300)

plt.show()
