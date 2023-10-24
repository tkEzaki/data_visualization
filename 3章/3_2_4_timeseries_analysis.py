import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# Load a dataset available in seaborn library
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'], index_col='date')

# Decompose the time series
model_type = 'additive' # 'multiplicative'  # 'additive'
res = sm.tsa.seasonal_decompose(df['value'], model=model_type)


# Plot the original data, the trend, the seasonality, and the residuals
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 8))
res.observed.plot(ax=ax1, color='blue', alpha=0.5)
res.trend.plot(ax=ax2, color='red', alpha=0.5)
res.seasonal.plot(ax=ax3, color='green', alpha=0.5)
res.resid.plot(ax=ax4, color='purple', alpha=0.5)

# Set the title of each subplot
# ax1.set_title('Observed')
# ax2.set_title('Trend')
# ax3.set_title('Seasonal')
# ax4.set_title('Residual')

# plt.tight_layout()
# Increase the space between plots
plt.subplots_adjust(hspace=0.8)

# Remove x-axis label for each subplot
ax1.set_xlabel('')
ax2.set_xlabel('')
ax3.set_xlabel('')
ax4.set_xlabel('')

plt.savefig(f'3_2_4_timeseries_analysis_{model_type}.png', dpi=300)
plt.savefig(f'3_2_4_timeseries_analysis_{model_type}.svg', dpi=300)
plt.show()
