import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import japanize_matplotlib


# plt.rcParams["font.size"] = 20

# Given data in a dictionary
data = {
    'year': list(range(1990, 2023)),
    'population': [1.23611, 1.24101, 1.24567, 1.24938, 1.25265, 1.2557, 1.25859, 1.26157, 1.26472, 1.26667,
                   1.26926, 1.27316, 1.27486, 1.27694, 1.27787, 1.27768, 1.27901, 1.28033, 1.28084, 1.28032,
                   1.28057, 1.27834, 1.27593, 1.27414, 1.27237, 1.27095, 1.27042, 1.26919, 1.26749, 1.26555,
                   1.26146, 1.25502, 1.24947]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(5, 3))

sns.lineplot(x='year', y='population', data=df, marker='o', linestyle='-')

# plt.title("Population Over Years")
plt.xlabel("西暦")
plt.ylabel("日本の総人口 [億人]")
plt.grid(True)
plt.tight_layout()
plt.savefig("1_1_3_population_line_plot.png", dpi=300)
plt.savefig("1_1_3_population_line_plot.svg", dpi=300)
plt.show()
