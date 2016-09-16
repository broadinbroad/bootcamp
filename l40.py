# Lesson 40: Practice with images

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

# Part A: In bootcamp_utils, define a function to segment for us.

# Import data
ecoli_img_phase= skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')
ecoli_img_fl = skimage.io.imread('data/HG105_images/noLac_FITC_0004.tif')

bsub_img_phase = skimage.io.imread('data/bsub_100x_phase.tif')
bsub_img_fl = skimage.io.imread('data/bsub_100x_cfp.tif')

# Test each part of the function


# Plot all results

plt_image = ecoli_img_phase
with sns.axes_style('dark'):
    skimage.io.imshow(plt_image)

plt.show()
