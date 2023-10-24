import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'

# Generate random data for the line plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 + y2

# Create subplots again with updated fonts
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Left plot with Times New Roman font
font1 = {'family': 'Times New Roman',
         'size': 8}
axes[0].plot(x, y1, label='y = sin(x)', linewidth=0.8, linestyle='-')
axes[0].plot(x, y2, label='y = cos(x)', linewidth=0.8, linestyle='--')
axes[0].plot(x, y3, label='y = sin(x) + cos(x)', linewidth=0.8, linestyle='-.')
# axes[0].set_title('Thin Lines, Small Text, Fine Ticks', fontdict={'family': 'Times New Roman', 'size': 10})
axes[0].set_xlabel('x-axis label, x', fontdict=font1)
axes[0].set_ylabel('y-axis label, y', fontdict=font1)
axes[0].tick_params(axis='both', labelsize=6, width=0.5, length=2)
for label in axes[0].get_xticklabels() + axes[0].get_yticklabels():
    label.set_fontname('Times New Roman')
axes[0].set_xticks(np.linspace(0, 10, 21))
axes[0].set_yticks(np.linspace(-3, 3, 31))
axes[0].legend(prop=font1)
# axes[0].grid(True)

# Make the axis lines thin
for axis in ['top', 'bottom', 'left', 'right']:
    axes[0].spines[axis].set_linewidth(0.5)


# Right plot with Arial font
font2 = {'family': 'Arial', 'size': 18}
axes[1].plot(x, y1, label='y = sin(x)', linewidth=2, linestyle='-')
axes[1].plot(x, y2, label='y = cos(x)', linewidth=2, linestyle='--')
axes[1].plot(x, y3, label='y = sin(x) + cos(x)', linewidth=2, linestyle='-.')
# axes[1].set_title('Thick Lines, Large Text, Coarse Ticks', fontdict={'family': 'Arial', 'size': 16})
axes[1].set_xlabel('x-axis label, x', fontdict=font2)
axes[1].set_ylabel('y-axis label, y', fontdict=font2)
axes[1].tick_params(axis='both', labelsize=16, width=2, length=4)
for label in axes[1].get_xticklabels() + axes[1].get_yticklabels():
    label.set_fontname('Arial')

axes[1].set_xticks(np.linspace(0, 10, 6))
axes[1].set_yticks(np.linspace(-3, 3, 7))
axes[1].legend(prop={'family': 'Arial', 'size': 14})
# axes[1].grid(True)

# Make the axis lines thick
for axis in ['top', 'bottom', 'left', 'right']:
    axes[1].spines[axis].set_linewidth(2)

plt.tight_layout()
plt.savefig('8_1_1_visibility_example.png', dpi=300)
plt.savefig('8_1_1_visibility_example.svg', dpi=300)

plt.show()
