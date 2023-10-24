import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'Yu Gothic'
np.random.seed(42)


def kl_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))


# Parameters for the normal distributions (mean and standard deviation)
mu1, sigma1 = 0, 0.5
mu2, sigma2 = 2, 1

# Generate sample data
num_samples = 10000
samples1 = np.random.normal(mu1, sigma1, num_samples)
samples2 = np.random.normal(mu2, sigma2, num_samples)

# Filter the samples to only include those within the limited range [-1, 3]
filtered_samples1 = samples1[(samples1 >= -1) & (samples1 <= 3)]
filtered_samples2 = samples2[(samples2 >= -1) & (samples2 <= 3)]

# Generate histograms with a limited range to ensure non-zero bins
limited_bins = np.linspace(-1, 3, 50)
hist1, _ = np.histogram(filtered_samples1, bins=limited_bins, density=True)
hist2, _ = np.histogram(filtered_samples2, bins=limited_bins, density=True)

# Normalize the histograms
hist1 /= np.sum(hist1 * (limited_bins[1] - limited_bins[0]))
hist2 /= np.sum(hist2 * (limited_bins[1] - limited_bins[0]))

# Re-calculate KL divergence
kl_1_to_2 = kl_divergence(hist1, hist2)
kl_2_to_1 = kl_divergence(hist2, hist1)

# Re-calculate JS divergence
js_divergence = 0.5 * (kl_divergence(hist1, 0.5 * (hist1 + hist2)) +
                       kl_divergence(hist2, 0.5 * (hist1 + hist2)))

# Re-plot histograms and show divergences
plt.figure(figsize=(8, 5))
plt.hist(filtered_samples1, bins=limited_bins, alpha=0.5, label=f'Filtered Sample Distribution 1', density=False, weights=np.ones(len(filtered_samples1)) / len(filtered_samples1))
plt.hist(filtered_samples2, bins=limited_bins, alpha=0.5, label=f'Filtered Sample Distribution 2', density=False, weights=np.ones(len(filtered_samples2)) / len(filtered_samples2))
plt.title(f'KL情報量: {kl_1_to_2:.4f} (1→2), ∞ (2→1), JS情報量: {js_divergence:.4f}')
# plt.xlabel('Value')
plt.ylabel('相対頻度')
# plt.legend()
plt.savefig('kl_js_divergence.png', dpi=300)
plt.show()
