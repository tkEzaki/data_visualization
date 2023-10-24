import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import FuncFormatter
import japanize_matplotlib

# plt.rcParams["font.family"] = "Yu Gothic"
plt.rcParams["font.size"] = 20

# Given data
countries = ['日本', 'ブラジル', '米国', '中国']
populations = [124620000, 215802222, 335540000, 1425849288]

# Create a DataFrame
df = pd.DataFrame({
    'Country': countries,
    'Population': populations
})
df['Population'] = df['Population'] / 100000000  # Convert to 100 million

# Filter and sort data for the first plot
df_filtered = df[df['Country'].isin(['米国', '日本'])].sort_values(by='Population', ascending=False)

# Sort data for the second plots
df_sorted = df.sort_values(by='Population', ascending=False)


# First Bar Plot using seaborn (Only 米国 and 日本)
fig1, ax1 = plt.subplots(figsize=(6, 2.5))
sns.barplot(x='Population', y='Country', data=df_filtered, ax=ax1, orient='h', color='orange')
# ax1.set_title("Bar Plot 1 (USA and Japan)")
ax1.set_xlabel("人口 [億人]")
ax1.set_ylabel("")

# Use exponents of 10 for x-axis labels
# formatter = FuncFormatter(exp_notation)
# ax1.xaxis.set_major_formatter(formatter)
plt.tight_layout()
plt.savefig('1_2_1_bar1.png', dpi=300)
plt.savefig('1_2_1_bar1.svg', dpi=300)
plt.show()

# Second Bar Plot using seaborn (All four countries)
fig2, ax2 = plt.subplots(figsize=(6, 3))
sns.barplot(x='Population', y='Country', data=df_sorted, ax=ax2, orient='h', color='orange')
# ax2.set_title("Bar Plot 2 (All Countries)")
ax2.set_xlabel("人口 [億人]")
ax2.set_ylabel("")

# Use exponents of 10 for x-axis labels
# ax2.xaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.savefig('1_2_1_bar2.png', dpi=300)
plt.savefig('1_2_1_bar2.svg', dpi=300)
plt.show()
