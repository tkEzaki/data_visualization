import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import graycomatrix, graycoprops
from skimage import data

plt.rcParams["font.size"] = 14

PATCH_SIZE = 21

# Open the camera image
image = data.camera()

# Select one patch from grassy areas of the image
grass_patch = image[280:280 + PATCH_SIZE, 454:454 + PATCH_SIZE]

# Select one patch from sky areas of the image
sky_patch = image[38:38 + PATCH_SIZE, 34:34 + PATCH_SIZE]

# Compute GLCM properties for each patch
features = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation']
grass_features = [graycoprops(graycomatrix(grass_patch, [1], [0], symmetric=True, normed=True), feature)[0, 0]
                  for feature in features]
sky_features = [graycoprops(graycomatrix(sky_patch, [1], [0], symmetric=True, normed=True), feature)[0, 0]
                for feature in features]

# Create the figure
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

# Display original image with locations of patches
axs[0, 0].imshow(image, cmap=plt.cm.gray, vmin=0, vmax=255)
axs[0, 0].plot(454 + PATCH_SIZE / 2, 280 + PATCH_SIZE / 2, 'gs')  # Grass
axs[0, 0].plot(34 + PATCH_SIZE / 2, 38 + PATCH_SIZE / 2, 'bs')   # Sky
axs[0, 0].set_xlabel('Original Image')
axs[0, 0].set_xticks([])
axs[0, 0].set_yticks([])
axs[0, 0].axis('image')

# Display the sky patch
axs[0, 1].imshow(sky_patch, cmap=plt.cm.gray, vmin=0, vmax=255)
axs[0, 1].set_xlabel('Sky')
axs[0, 1].set_xticks([])
axs[0, 1].set_yticks([])

# Display the grass patch
axs[0, 2].imshow(grass_patch, cmap=plt.cm.gray, vmin=0, vmax=255)
axs[0, 2].set_xlabel('Grass')
axs[0, 2].set_xticks([])
axs[0, 2].set_yticks([])

# Plot GLCM features
barWidth = 0.3
r1 = np.arange(len(grass_features))
r2 = [x + barWidth for x in r1]

axs[1, 0].bar(r2, grass_features, color='g', width=barWidth, edgecolor='grey', label='Grass')
axs[1, 0].bar(r1, sky_features, color='b', width=barWidth, edgecolor='grey', label='Sky')

axs[1, 0].set_xticks([r + barWidth for r in range(len(grass_features))])
axs[1, 0].set_xticklabels(features, rotation=30, ha='right')
# axs[1, 0].set_xlabel('GLCM Features')
# axs[1, 0].set_ylabel('Value')
# y log scale
axs[1, 0].set_yscale('log')
axs[1, 0].legend()

# Plot the GLCM of sky patch
axs[1, 1].imshow(graycomatrix(sky_patch, [1], [0], symmetric=True, normed=True)[:, :, 0, 0], cmap='jet', origin='lower')
axs[1, 1].set_title('GLCM of Sky')
axs[1, 1].set_xlabel('Pixel value')
axs[1, 1].set_ylabel('Pixel value')

# Plot the GLCM of grass patch
axs[1, 2].imshow(graycomatrix(grass_patch, [1], [0], symmetric=True, normed=True)[:, :, 0, 0], cmap='jet', origin='lower')
axs[1, 2].set_title('GLCM of Grass')
axs[1, 2].set_xlabel('Pixel value')
axs[1, 2].set_ylabel('Pixel value')

plt.tight_layout()
plt.savefig('glcm.png')
plt.show()
