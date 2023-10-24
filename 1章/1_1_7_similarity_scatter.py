import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy import stats


def generate_similarity_scatter():
    n = 190
    low, high = -0.45, 0.95
    rho = 0.7
    mean = [0, 0]
    cov = [[1, rho], [rho, 1]]
    rng = np.random.default_rng(seed=42)
    x, y = rng.multivariate_normal(mean, cov, n - 1).T
    x = low + (high - low) * (x - x.min()) / (x.max() - x.min())
    y = low + (high - low) * (y - y.min()) / (y.max() - y.min())
    x = np.append(x, 0.80)
    y = np.append(y, 0.72)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    plt.scatter(x, y, c="orange", alpha=0.5)
    plt.plot(x, intercept + slope * x, 'orange')
    plt.scatter([0.80], [0.72], c="r")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([-0.5, 0.0, 0.5, 1])
    plt.yticks([-0.5, 0.0, 0.5, 1])
    plt.xlim([-0.5, 1.0])
    plt.ylim([-0.5, 1.0])
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.savefig('1_1_7_similarity_scatter.png', dpi=300)
    plt.savefig('1_1_7_similarity_scatter.svg', dpi=300)
    plt.show()


generate_similarity_scatter()
