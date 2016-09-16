# Lesson 40: Practice with images

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import bootcamp_utils as boot
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

## Part A: In bootcamp_utils, define a function to segment for us.

# # Import data
ecoli_img_phase= skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')
ecoli_img_fl = skimage.io.imread('data/HG105_images/noLac_FITC_0004.tif')

bsub_img_phase = skimage.io.imread('data/bsub_100x_phase.tif')
bsub_img_fl = skimage.io.imread('data/bsub_100x_cfp.tif')
#
# # Do it all at once!
# e_phase = boot.img_analyze(ecoli_img_phase, thresh_type='max')
# e_fl = boot.img_analyze(ecoli_img_fl, thresh_type='min')
#
# # Otsu doesn't work on B.sub.
# b_phase = boot.img_analyze(bsub_img_phase, thresh_type='max', thresh=-0.002)
# b_fl = boot.img_analyze(bsub_img_fl, thresh_type='min', thresh=0.0005)
#
# #  Plot all results
#
# plt_image = b_fl
# with sns.axes_style('dark'):
#     skimage.io.imshow(plt_image, cmap=plt.cm.viridis)
#
# plt.show()

## Part B: Make data frame of mean intensities of all regions in fluor. e coli image

# Get intensity image
im_filt = boot.outlier_pixel(ecoli_img_fl, 3)
im_filt = boot.even_illumin(im_filt, 500)

# Get segmentation mask
im_seg_mask = boot.img_analyze(ecoli_img_fl, thresh_type='min')
n_cells = np.max(im_seg_mask)

# Get region properties
im_props = skimage.measure.regionprops(im_seg_mask,
                        intensity_image=im_filt)

# Make a data frame
cell_int = np.empty(n_cells)
for prop in im_props:
    cell_int[prop.label] = prop.mean_intensity

df = DataFrame(data=cell_int, name='fluor. int.')
