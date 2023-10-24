import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import japanize_matplotlib


def generate_heatmap():
    mean = [0, 0]
    cov = [[1, 0.8], [0.8, 1]]
    x = np.random.multivariate_normal(mean, cov, (10, 10))
    heatmap1, heatmap2 = x[..., 0], x[..., 1]
    heatmap1 = (heatmap1 - np.min(heatmap1)) / (np.max(heatmap1) - np.min(heatmap1))
    heatmap2 = (heatmap2 - np.min(heatmap2)) / (np.max(heatmap2) - np.min(heatmap2))
    x = heatmap1.flatten()
    y = heatmap2.flatten()
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(heatmap1, cmap='gray', interpolation='nearest')
    axs[0].axis('off')
    axs[1].imshow(heatmap2, cmap='gray', interpolation='nearest')
    axs[1].axis('off')
    plt.savefig('1_1_6_visual_data.png')
    plt.savefig('1_1_6_visual_data.svg')
    plt.show()

    plt.figure(figsize=(4, 4))
    plt.scatter(x, y, alpha=0.5)
    plt.plot(x, intercept + slope * x, 'b')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([0.0, 0.5, 1.0])
    plt.yticks([0.0, 0.5, 1.0])
    plt.tick_params(axis='both', which='major', labelsize=22)
    plt.tight_layout()
    plt.savefig('1_1_6_scatter.png', dpi=300)
    plt.savefig('1_1_6_scatter.svg', dpi=300)
    plt.show()
    print(f'Correlation coefficient: {r_value}, {p_value}')


def generate_individual_location():
    individual1 = np.abs(np.random.normal(loc=0, scale=1, size=100))
    individual2 = np.abs(np.random.normal(loc=0, scale=1, size=100))
    individual2 = 0.6 * individual1 + 0.4 * individual2
    individual1 = individual1 / np.sum(individual1)
    individual2 = individual2 / np.sum(individual2)
    slope, intercept, r_value, p_value, std_err = stats.linregress(individual1, individual2)

    plt.figure(figsize=(6, 3))
    barWidth = 0.3
    r1 = np.arange(len(individual1))
    r2 = [x + barWidth for x in r1]
    plt.bar(r1, individual1, color='b', width=barWidth, edgecolor='b')
    plt.bar(r2, individual2, color='r', width=barWidth, edgecolor='r')
    plt.xlim([0, 100])
    plt.tick_params(axis='both', which='major', labelsize=18)
    plt.savefig('1_1_6_location_index.png', dpi=300)
    plt.savefig('1_1_6_location_index.svg', dpi=300)
    plt.show()

    plt.figure(figsize=(4, 4))
    plt.scatter(individual1, individual2, alpha=0.5, c="g")
    plt.plot(individual1, intercept + slope * individual1, 'g')
    plt.xlim([0, 0.03])
    plt.ylim([0, 0.03])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([0.0, 0.01, 0.02, 0.03])
    plt.yticks([0.0, 0.01, 0.02, 0.03])
    plt.tick_params(axis='both', which='major', labelsize=20)
    plt.tight_layout()
    plt.savefig('1_1_6_location_index_scatter.png', dpi=300)
    plt.savefig('1_1_6_location_index_scatter.svg', dpi=300)
    plt.show()
    print(f'Correlation coefficient: {r_value}, {p_value}')


if __name__ == "__main__":
    generate_heatmap()
    generate_individual_location()
