import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from sklearn.mixture import GaussianMixture
from scipy.stats import norm

np.random.seed(0)

plt.rcParams['font.size'] = 14

# ピーク一つとピーク二つの分布
data4_b = np.concatenate([np.random.normal(3, 1, 500), np.random.normal(7, 1, 500)])

plt.figure(figsize=(5, 4))

# データをヒストグラムでプロット
plt.hist(data4_b, bins=30, density=True, alpha=0.5, color='yellow', edgecolor='black')

# データを2成分のガウシアン混合モデルでフィッティング
gmm = GaussianMixture(n_components=2)
gmm.fit(data4_b.reshape(-1, 1))

# 混合ガウシアンモデルの結果をプロット
x = np.linspace(data4_b.min(), data4_b.max(), 1000).reshape(-1, 1)
logprob = gmm.score_samples(x)
pdf = np.exp(logprob)
plt.plot(x, pdf, '-k', color='grey', alpha=0.5, lw=5)

# 各ガウシアンをプロット
colors = ['red', 'blue']
for i in range(gmm.n_components):
    pdf_individual = gmm.weights_[i] * norm(gmm.means_[i, 0], np.sqrt(gmm.covariances_[i, 0])).pdf(x)
    plt.plot(x, pdf_individual, '--', color=colors[i])

plt.xlabel('観測値 $X$')
# plt.title('Gaussian Mixture Model')
plt.tight_layout()
plt.savefig('3_1_3_2_gmm_fitting.png', dpi=300)
plt.savefig('3_1_3_2_gmm_fitting.svg', dpi=300)

plt.show()
