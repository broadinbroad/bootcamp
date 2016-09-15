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
import skimage.morphology
import skimage.filters

# Load the image
phase_im = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('data/bsub_100x_cfp.tif')

# Plot with Python (can detect 12 bit)
# plt.imshow(phase_im)
# plt.show()

# PLot with other color matplotlib
# plt.imshow(phase_im, cmap=plt.cm.Greys_r)
# plt.imshow(phase_im, cmap=plt.cm.viridis)
# plt.show()


# Use histogram to find a threshold
# plt.figure()
# _ = plt.hist(np.ravel(phase_im), bins=100)
# plt.show()

# OR with skimage
# hist_phase, bins_phase = skimage.exposure.histogram(phase_im)
# _ = plt.plot(bins_phase, hist_phase)
#
# plt.xlabel('Pixel Value')
# plt.ylabel('Count')
# plt.show()

# Threshold the image. Picked 260 from histogram
# thresh = 250
# im_phase_thresh = phase_im < thresh
#
# plt.figure()
# with sns.axes_style('dark'):
#     plt.imshow(im_phase_thresh, cmap=plt.cm.viridis)
#
# plt.show()

# Doesn't look very good. Let's use the cfp image!
with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)

plt.show()

# Slice out single bright Pixel
# plt.close()
# with sns.axes_style('dark'):
#     plt.imshow(cfp_im[150:250, 450:550]/cfp_im.max(),
#                cmap=plt.cm.viridis)
#
# plt.show()

# Filter the image - use a structural element, and compute median of small
# area surrounding each pixel

# Generate a structural element
selem = skimage.morphology.square(3) # shoudld be much smaller than size of bacteria
cfp_filt = skimage.filters.median(cfp_im, selem)

# To see selem
# plt.imshow(selem, interpolation='nearest')

# Look at filtered image
# with sns.axes_style('dark'):
#     plt.imshow(cfp_filter, cmap=plt.cm.viridis)

# Plot histogram of CFP filtered image
# plt.figure()
# hist_phase, bins_phase = skimage.exposure.histogram(cfp_filter)
# _ = plt.plot(bins_phase, hist_phase)
#
# plt.xlabel('Pixel Value')
# plt.ylabel('Count')
# plt.show()

# Threshold cfp_filter and plot
# cfp_thresh = 120
# cfp_filt_thresh = cfp_filt > cfp_thresh
#
# with sns.axes_style('dark'):
#     plt.imshow(cfp_filt_thresh, cmap=plt.cm.viridis)
#
# plt.show()

# Find Otsu's Threshold
phase_thresh = skimage.filters.threshold_otsu(phase_im)
cfp_thresh = skimage.filters.threshold_otsu(cfp_filt)

# Apply threshold
phase_otsu = phase_im < phase_thresh
cfp_otsu = cfp_filt > cfp_thresh

# Plot images
plt.figure()
with sns.axes_style('dark'):
    plt.imshow(phase_otsu, cmap=plt.cm.Greys_r)
plt.title('Phase Image (Otsu\'s filter)')
plt.show()

plt.figure()
with sns.axes_style('dark'):
    plt.imshow(cfp_otsu, cmap=plt.cm.viridis)
plt.title('CFP Image (Otsu\'s filter)')
plt.show()
