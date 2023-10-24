import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib

plt.rcParams["font.size"] = 14

# Load the data
df = pd.read_csv('bubble_chart_data.csv')
region_df = pd.read_csv('bubble_chart_region_data.csv')

# Filter the required data
gdp_df = df[df['Series Name'] == 'GDP, PPP (current international $)']
life_exp_df = df[df['Series Name'] == 'Life expectancy at birth, total (years)']
population_df = df[df['Series Name'] == 'Population, total']

# Check for ".." and exclude missing values, also convert the type to float
gdp_df = gdp_df[gdp_df['2021 [YR2021]'] != '..']
gdp_df['2021 [YR2021]'] = gdp_df['2021 [YR2021]'].astype(float)

life_exp_df = life_exp_df[life_exp_df['2021 [YR2021]'] != '..']
life_exp_df['2021 [YR2021]'] = life_exp_df['2021 [YR2021]'].astype(float)

population_df = population_df[population_df['2021 [YR2021]'] != '..']
population_df['2021 [YR2021]'] = population_df['2021 [YR2021]'].astype(float)

# Merge the dataframes based on 'Country Name'
data = gdp_df[['Country Name', 'Country Code', '2021 [YR2021]']].merge(
    life_exp_df[['Country Name', '2021 [YR2021]']], on='Country Name', how='inner', suffixes=('_GDP', '_Life_Expectancy')
).merge(
    population_df[['Country Name', '2021 [YR2021]']], on='Country Name', how='inner'
)
data.rename(columns={'2021 [YR2021]': '2021 [YR2021]_Population', 'Country Name': 'Country_Name'}, inplace=True)

# Create a new DataFrame where 'alpha-3' and 'name' are both indices
region_df.set_index(['alpha-3', 'name'], inplace=True)

# First, try merging on 'Country Code'
merged_data = data.merge(region_df[['region']], left_on='Country Code', right_on='alpha-3', how='left')

# For rows where 'region' is still NaN, try merging on 'Country Name'
merged_data.loc[merged_data['region'].isnull()] = data.merge(region_df[['region']], left_on='Country_Name', right_on='name', how='left')

# Set 'Country Name' as the index
merged_data.set_index('Country_Name', inplace=True)
merged_data.dropna(inplace=True)

merged_data["GDP per capita"] = merged_data["2021 [YR2021]_GDP"] / merged_data["2021 [YR2021]_Population"]

# Get unique regions and map to tab10 colormap
unique_regions = merged_data['region'].unique()
region_colors = {region: color for region, color in zip(unique_regions, plt.cm.tab10.colors)}

# Create the bubble chart
plt.figure(figsize=(10, 10))
for region, color in region_colors.items():
    temp_df = merged_data[merged_data['region'] == region]
    if not temp_df.empty:  # Only plot if there is data for this region
        plt.scatter(temp_df['GDP per capita'], temp_df['2021 [YR2021]_Life_Expectancy'],
                    s=temp_df['2021 [YR2021]_Population'] / 1000000, color=color, alpha=0.5)

# Add a legend for colors
legend_handles = []
for region, color in region_colors.items():
    plt.scatter([], [], c=color, alpha=0.5, s=100, label=region)
    legend_handles.append(plt.scatter([], [], c=color, alpha=0.5, s=100))  # Save handles for legend

# Add a legend for sizes
populations = [1e6, 1e7, 1e8, 1e9]  # Assuming population in millions
size_legend_handles = []
for pop in populations:
    plt.scatter([], [], c='k', alpha=0.3, s=pop / 1000000,
                label='{:.0e}'.format(pop))  # Format population as integer
    size_legend_handles.append(plt.scatter([], [], c='k', alpha=0.3, s=pop / 1000000))  # Save handles for size legend

# Combine the legends
# regions_legend = plt.legend(handles=legend_handles, labels=['Asia', 'Europe', 'Africa', 'Oceania', 'Americas'], title="Regions", loc='upper left')
regions_legend = plt.legend(handles=legend_handles, labels=['Asia', 'Europe', 'Africa', 'Oceania', 'Americas'], title="地域", loc='upper left')

# plt.legend(handles=size_legend_handles, labels=[str(int(pop)) for pop in populations], title='Population', loc='lower right')
plt.legend(handles=size_legend_handles, labels=[str(int(pop)) for pop in populations], title='人口', loc='lower right')


plt.gca().add_artist(regions_legend)

plt.xscale('log')
plt.xlabel('一人あたりGDP [$]', fontsize=18)
plt.ylabel('平均寿命 [年]', fontsize=18)
plt.grid(True)

# Add country names to the points
for line in range(0, merged_data.shape[0]):
    country = merged_data.index[line]
    x = merged_data['GDP per capita'][line]
    y = merged_data['2021 [YR2021]_Life_Expectancy'][line]
    if not np.isnan(x) and not np.isnan(y):  # Check that the point is not NaN
        region = merged_data['region'][line]
        if region in region_colors:  # Check that the country is in a plotted region
            plt.text(x + 0.2, y, country,
                     horizontalalignment='left',
                     size='small',
                     color=region_colors[region])  # Use the region color

plt.tight_layout()
plt.savefig("3_3_6_bubble_chart.png", dpi=300)
plt.savefig("3_3_6_bubble_chart.svg", dpi=300)

plt.show()
