import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import japanize_matplotlib

plt.rcParams["font.size"] = 20

# Given data
data = {
    'x': [0.204, 1.07, -0.296, 0.57, 0.637, 0.82, 0.137, -0.046],
    'y': [0.07, 0.57, 0.936, 1.436, 0.32, 1.003, 1.186, 0.503]
}

df = pd.DataFrame(data)

# Define the coordinates of the four points that make up the square
square_points = np.array([
    [-0.296, 0.936],
    [0.57, 1.436],
    [1.07, 0.57],
    [0.204, 0.07],
    [-0.296, 0.936]  # Close the loop
])

# Plot the points
plt.scatter(df['x'], df['y'], label='Points', color='blue')

# Plot the square by connecting the four points
plt.plot(square_points[:, 0], square_points[:, 1], 'r--', label='Square')

# Add labels and title
plt.xlabel('$x$')
plt.ylabel('$y$')
# plt.title('Scatter Plot with Square')
# plt.legend()
# plt.grid(True)
plt.axis('equal')
# Show the plot
plt.tight_layout()
plt.savefig('1_2_2_square_scatter.png', dpi=300)
plt.savefig('1_2_2_square_scatter.svg', dpi=300)
plt.show()
