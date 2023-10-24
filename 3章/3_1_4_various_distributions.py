import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.stats import norm, binom, poisson, expon, uniform, gamma, lognorm, weibull_min, pareto

plt.rcParams['font.size'] = 16

# Colors for the plots
colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'cyan']

fig, axs = plt.subplots(3, 3, figsize=(14, 10))

# Uniform Distribution
x_values = np.linspace(-1, 1, 1000)
axs[0, 0].plot(x_values, uniform.pdf(x_values, -1, 2), color=colors[4], label="$f(x) = \\frac{1}{b - a}$")
axs[0, 0].set_ylim(0, 1)
axs[0, 0].legend()
axs[0, 0].set_title("一様分布", fontsize=20)

# Normal Distribution
x_values = np.linspace(-4, 4, 1000)
axs[0, 1].plot(x_values, norm.pdf(x_values, 0, 1), color=colors[0], label="$f(x) = \\frac{1}{\\sqrt{2\\pi\\sigma^2}} e^{ -\\frac{(x-\\mu)^2}{2\\sigma^2} }$")
axs[0, 1].set_ylim(0, 0.65)
axs[0, 1].legend()
axs[0, 1].set_title("正規分布", fontsize=20)

# Binomial Distribution
n, p = 10, 0.5
x_values = range(n + 1)
axs[0, 2].plot(x_values, binom.pmf(x_values, n, p), 'o', color=colors[1], label="$P(k; n, p)=$" + "\n" + "  $C(n, k) p^k (1-p)^{n-k}$")
axs[0, 2].set_ylim(0, 0.4)
axs[0, 2].legend()
axs[0, 2].set_title("二項分布", fontsize=20)

# Poisson Distribution
mu = 3
x_values = range(10)
axs[1, 0].plot(x_values, poisson.pmf(x_values, mu), 'o', color=colors[2], label="$P(k; \\mu) = \\frac{e^{-\\mu} \\mu^k}{k!}$")
axs[1, 0].set_ylim(0, 0.3)
axs[1, 0].legend()
axs[1, 0].set_title("ポアソン分布", fontsize=20)

# Exponential Distribution
x_values = np.linspace(0, 10, 1000)
axs[1, 1].plot(x_values, expon.pdf(x_values), color=colors[3], label="$f(x; \\lambda) = \\lambda e^{-\\lambda x}$")
axs[1, 1].set_ylim(0, 1.0)
axs[1, 1].legend(loc='lower right')
axs[1, 1].set_title("指数分布", fontsize=20)

# Adding inset for Exponential Distribution
axins_exp = axs[1, 1].inset_axes([0.5, 0.5, 0.47, 0.47])
x_values_large = np.linspace(0.01, 10, 1000)
axins_exp.plot(x_values_large, expon.pdf(x_values_large), color=colors[3])
axins_exp.set_yscale('log')
# Set specific y-ticks
axins_exp.set_yticks([0.0001, 0.01, 1])

# Set y-tick labels
axins_exp.set_yticklabels(['$10^{-4}$', '$10^{-2}$', '$10^{0}$'])

# Gamma Distribution
x_values = np.linspace(0, 10, 1000)
axs[1, 2].plot(x_values, gamma.pdf(x_values, a=5), color=colors[5], label="$f(x; \\alpha) = \\frac{1}{\\Gamma(\\alpha)} \\beta^{\\alpha} x^{\\alpha - 1} e^{-\\beta x}$")
axs[1, 2].set_ylim(0, 0.3)
axs[1, 2].legend()
axs[1, 2].set_title("ガンマ分布", fontsize=20)

# Weibull Distribution
x_values = np.linspace(0.01, 2, 1000)
axs[2, 0].plot(x_values, weibull_min.pdf(x_values, c=1.5), color=colors[7], label="$f(x; k) = k (\\frac{x}{\\lambda})^{k - 1} e^{-(x/\\lambda)^{k}}$")
axs[2, 0].set_ylim(0, 1.1)
axs[2, 0].legend(loc='upper right', framealpha=0.5)
axs[2, 0].set_title("ワイブル分布", fontsize=20)

# Log-Normal Distribution
x_values = np.linspace(0.01, 10, 1000)
axs[2, 1].plot(x_values, lognorm.pdf(x_values, s=1), color=colors[6], label="$f(x; \\mu, \\sigma) = \\frac{1}{x \\sigma \\sqrt{2\\pi}} e^{-\\frac{(\\ln x - \\mu)^2}{2\\sigma^2}}$")
axs[2, 1].set_ylim(0, 0.8)
axs[2, 1].legend(loc='lower right', framealpha=0.5)
axs[2, 1].set_title("対数正規分布", fontsize=20)

# Adding inset for Log-Normal Distribution
axins_lognorm = axs[2, 1].inset_axes([0.5, 0.5, 0.47, 0.47])
x_values_large = np.linspace(-5, 3, 100)
x_values_large = np.exp(x_values_large)
# x_values_large = np.linspace(0.01, 100, 1000)
axins_lognorm.plot(x_values_large, lognorm.pdf(x_values_large, s=1), color=colors[6])
axins_lognorm.set_xscale('log')

# Pareto Distribution
x_values = np.linspace(1, 4, 1000)
axs[2, 2].plot(x_values, pareto.pdf(x_values, b=5), color=colors[8])
axs[2, 2].set_ylim(0, 6)
axs[2, 2].legend(["$f(x; \\alpha) = \\alpha x_m^{\\alpha} x^{-\\alpha - 1}$"], loc='lower right')
axs[2, 2].set_title("パレート分布", fontsize=20)

# Adding inset for Pareto Distribution
axins = axs[2, 2].inset_axes([0.5, 0.5, 0.47, 0.47])
x_values_large = np.linspace(1, 100, 1000)
axins.plot(x_values_large, pareto.pdf(x_values_large, b=5), color=colors[8])
axins.set_xscale('log')
axins.set_yscale('log')
axins.set_yticks([0.0000000001, 0.0001])
axins.get_yaxis().set_tick_params(which='both', direction='out', pad=5)

# Set y-tick labels
axins.set_yticklabels(['$10^{-10}$', '$10^{-4}$'])

# Hide minor ticks
axins.xaxis.set_tick_params(which='minor', length=0)


# plt.subplots_adjust(wspace=0.3, hspace=0.5)
plt.tight_layout()
plt.savefig('3_1_4_various_distributions.png', dpi=300)
plt.savefig('3_1_4_various_distributions.svg', dpi=300)

plt.show()
