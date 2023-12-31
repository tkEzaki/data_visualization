import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import seaborn as sns  # グラフ作成のためのSeaborn
from scipy.stats import linregress  # 線形回帰のためのSciPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを設定

# シード値の設定
np.random.seed(42)

# 書籍の数
n_books = 100

# Aさんのレビュー
a_scores = np.random.normal(loc=60, scale=15, size=n_books).astype(int)
a_scores = np.clip(a_scores, 0, 100)  # 0から100の範囲にクリップ（0以下は0に、100以上は100にする）

# Bさんのレビュー（Aさんと高い相関）
b_scores = a_scores + np.random.normal(loc=0, scale=10, size=n_books).astype(int)
b_scores = np.clip(b_scores, 0, 100)  # 0から100の範囲にクリップ

# Cさんのレビュー（Aさんと緩い逆相関）
c_scores = 100 - a_scores + np.random.normal(loc=0, scale=20, size=n_books).astype(int)
c_scores = np.clip(c_scores, 0, 100)  # 0から100の範囲にクリップ

print('Aさんのレビュー\tBさんのレビュー\tCさんのレビュー')
for a, b, c in zip(a_scores, b_scores, c_scores):
    print(f'{a}\t\t\t{b}\t\t\t{c}')

# 相関係数の計算
corr_ab = np.corrcoef(a_scores, b_scores)[0, 1]
corr_ac = np.corrcoef(a_scores, c_scores)[0, 1]


# 線形回帰の描画
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
sns.regplot(x=a_scores, y=b_scores, ax=axes[0], color='blue')  # AさんとBさんのレビューの散布図と線形回帰直線を描画
axes[0].set_title(f'AさんとBさんの類似度 $r$ = {corr_ab:.2f}')  # タイトルを設定
axes[0].set_xlabel('Aさんによる評価')  # x軸ラベルを設定
axes[0].set_ylabel('Bさんによる評価')  # y軸ラベルを設定

sns.regplot(x=a_scores, y=c_scores, ax=axes[1], color='red')  # AさんとCさんのレビューの散布図と線形回帰直線を描画
axes[1].set_title(f'AさんとCさんの類似度 $r$ = {corr_ac:.2f}')  # タイトルを設定
axes[1].set_xlabel('Aさんによる評価')  # x軸ラベルを設定
axes[1].set_ylabel('Cさんによる評価')  # y軸ラベルを設定


# 相対スコアを元にコサイン類似度を計算してみる（可視化には無関係）
a_scores_rel = a_scores - np.mean(a_scores)
b_scores_rel = b_scores - np.mean(b_scores)
c_scores_rel = c_scores - np.mean(c_scores)

cos_sim_ab = np.dot(a_scores_rel, b_scores_rel) / (np.linalg.norm(a_scores_rel) * np.linalg.norm(b_scores_rel))
cos_sim_ac = np.dot(a_scores_rel, c_scores_rel) / (np.linalg.norm(a_scores_rel) * np.linalg.norm(c_scores_rel))
print(f'コサイン類似度（AさんとBさん）: {cos_sim_ab:.2f}')
print(f'コサイン類似度（AさんとCさん）: {cos_sim_ac:.2f}')


plt.tight_layout()  # レイアウトの設定
plt.savefig('6_3_1_correlation_similarity.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
