from nichord.chord import plot_chord
from nichord.glassbrain import plot_glassbrain
from nichord.combine import combine_imgs, plot_and_combine
from nichord.coord_labeler import get_idx_to_label
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# Each of the examples covered in the README.md file.

# Example 0, basic introduction

if __name__ == '__main__':
    edges = [(0, 1), (0, 2), (1, 5), (3, 5), (4, 6), (2, 7), (6, 7)]
    edge_weights = [-0.3, -0.5, 0.7, 0.5, -0.2, 0.3, 0.8]
    coords = [[-24, -99, -12], [51, -3, -15], [-15, -70, 30], [21, 39, 39],
              [21, -66, 48], [54, 33, 12], [-33, 3, 3], [57, -45, 12]]
    idx_to_label = get_idx_to_label(coords, atlas='yeo')

    fp_chord = r'ex0_chord.png'
    plot_chord(idx_to_label, edges, edge_weights=edge_weights,
               coords=None, network_order=None,
               network_colors=None, linewidths=15,
               alphas = 0.9, label_fontsize=50,
               fp_chord=fp_chord, do_ROI_circles=True,
               do_ROI_circles_specific=True, ROI_circle_radius=0.02,
               arc_setting=False)

    fp_glass = r'ex0_glass.png'
    plot_glassbrain(idx_to_label, edges, edge_weights, fp_glass,
                    coords, linewidths=15, node_size=17)

    fp_combined = r'ex0.png'
    combine_imgs(fp_glass, fp_chord, fp_combined)
    print('Example 0 done')

# Examples 1 and 2 reflect how NiChord may be used given full connectome's
#   worth of ROIs. Here ROIs are taken from the Power et al. (2014) atlas.
#   The examples also show how network label colors can be specified and the
#   networks can be plotted in a specific order around the circle.
