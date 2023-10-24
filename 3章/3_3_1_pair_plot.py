import seaborn as sns
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams["font.size"] = 16

# Load the penguins dataset
penguins = sns.load_dataset("penguins")

# japanize labels
penguins = penguins.rename(columns={"species": "種類", "island": "島", "bill_length_mm": "くちばしの長さ [mm]",
                                    "bill_depth_mm": "くちばしの厚さ [mm]", "flipper_length_mm": "ひれの長さ [mm]", "body_mass_g": "体重 [g]"})

# Make a pairplot of the penguins dataset
grid = sns.pairplot(penguins, hue="種類")
grid._legend.remove()

# grid.set(xlabel="", ylabel="")
plt.tight_layout()
# Show the plot
plt.savefig('3_3_1_pairplot.png', dpi=300)
plt.savefig('3_3_1_pairplot.svg', dpi=300)

plt.show()
