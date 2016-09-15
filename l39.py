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

with sns.axes_style('dark'):
    plt.imshow(phase_im, cmap=plt.cm.Greys_r)

plt.show()
