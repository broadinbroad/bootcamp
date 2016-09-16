# Lesson 38: Image processing

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 200,
        'legend.fontsize': 16, 'xtick.labelsize': 32,
        'ytick.labelsize': 32}
sns.set(rc=rc)

# For image analysis
import skimage.io
import skimage.exposure
import skimage.measure
import skimage.segmentation

# Load a phase image to look at and segment
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')
#
# with sns.axes_style('dark'):
#     plt.imshow(phase_im, cmap=plt.cm.Greys_r)
#
# plt.show()

# Use background subtraction to remove uneven illumination, use a large blur
im_blur = skimage.filters.gaussian(phase_im, 50) # radius greater than features of image
#
# with sns.axes_style('dark'):
#     plt.imshow(im_blur, cmap=plt.cm.Greys_r)
#
# plt.show()

# im_blur and phase_im are different datatypes, have different ranges
# This makes it a float AND rescales
phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

# # Show both images
# plt.figure()
# plt.imshow(phase_float, cmap=plt.cm.viridis)
# plt.title('original')
# plt.show()
#
# plt.figure()
# plt.imshow(phase_float - im_blur, cmap=plt.cm.viridis)
# plt.title('background subtracted')
# plt.show()

# apply Otsu filter
thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh

# # Plot our segementation
# plt.imshow(seg, cmap=plt.cm.Greys_r)
# plt.show()

# Label the bacteria
seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)

# plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)
# plt.show()

# # Look at individual cells
# plt.close()
# n_cell = 1
# plt.imshow(seg_lab==n_cell)
# plt.show()

# Compute region properties and extra area of each object
ip_dist = 0.063 # um between pixel
props = skimage.measure.regionprops(seg_lab)

# Get the areas as an array
areas = np.array([prop.area for prop in props])
cutoff_sm = 300 # everything should be bigger than this

# Make a copy so you don't affect the original
im_cells = np.copy(seg_lab)

for i, _ in enumerate(areas):
    if areas[i] < cutoff_sm:
        im_cells[im_cells==props[i].label] = 0

# Also, with labeled cells
im_cells_lab, num_cells = skimage.measure.label(im_cells, return_num=True, background=0)

# Check that it worked
plt.figure()
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)
plt.title('Original')
plt.show()

plt.figure()
plt.imshow(im_cells_lab, cmap=plt.cm.Spectral_r)
plt.title('Remove Stuff')
plt.show()
