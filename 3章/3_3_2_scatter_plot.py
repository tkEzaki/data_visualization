import seaborn as sns
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy import stats

plt.rcParams["font.size"] = 16
# Load the penguins dataset
penguins = sns.load_dataset("penguins")

# Make a scatter plot with regression line of bill_length_mm and body_mass_g, set marker opacity to 0.5
lm = sns.lmplot(x='bill_length_mm', y='body_mass_g', hue='species', data=penguins, scatter_kws={'alpha': 0.3}, legend=False)

# Loop over each species to calculate and print r and p value
for species in penguins.species.unique():
    if species is not None:  # Exclude NaN
        species_data = penguins[penguins.species == species].dropna()
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            species_data['bill_length_mm'], species_data['body_mass_g'])
        print(f"For {species}:\n r value is: {r_value}\n p_value is: {p_value}")

plt.xlabel('くちばしの長さ [mm]')
plt.ylabel('体重 [g]')
plt.savefig('3_3_2_scatter_plot.png', dpi=300)
plt.savefig('3_3_2_scatter_plot.svg', dpi=300)

plt.show()
