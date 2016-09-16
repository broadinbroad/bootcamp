# Bootcamp Utilities:
"""A collection of statistical functions proved
useful for 55 students."""

# Import modules needed
import numpy as np

# For image analysis
import skimage.io
import skimage.exposure
import skimage.measure
import skimage.segmentation

# Define function for ecdf
def ecdf(data):
    """
    Compute x, y values for an empirical cumulative distribtuion
    function
    """

    # Sort the data
    x = np.sort(data)

    # each data point is 1/n_pts fraction of data
    # use to computed ecdf
    y = np.arange(1, len(data)+1) / len(data)

    return np.array([x, y])

# Define function to compute Bootstrap
def draw_bs_reps(data, func, size=1):
    """
    Draw bootstrap replicates from an array of data

    Input:
    data = NumPy aray of data
    func = the statistical function to be tested on each replicate
    size = number of times to compute the boostrap statistic

    Return:
    reps = func computed on boostrap sample, 'size' times

    """

    reps = np.empty(size)

    # Compute bootstrap the specified number of times
    for i in range(size):
        # Draw from the data set len(data) number of times
        bs = np.random.choice(data, replace=True, size=len(data))

        # Perform the specified statistical function
        reps[i] = func(bs)

    return reps

# Define function to compute confidence interval
def conf_int(data, interval=95):
    """Returns confidence interval on data"""

    margin = (100 - interval) / 2

    confidence_interval = np.percentile(data, [margin, 100-margin])

    return confidence_interval

# Define function to compute coefficient of variation
def coeff_var_data(data):

    return np.std(data) / np.mean(data)

# Define function to correct for uneven illumination.

def even_illumin(image, blur_size):
    """Corrects for uneven illumination by subtracting
    large Guassian blur"""

    # Blur image
    image_blur = skimage.filters.gaussian(image, blur_size)

    # Convert image to float and rescale
    image_float = skimage.img_as_float(image)

    # Subtract background
    image_sub = image_float - image_blur

    return image_sub

# Define a function to remove outlier pixels

def outlier_pixel(image, blur_size, selem_shape='square'):
    """Remove outlier pixels by taking median of small structuring element"""

    if selem_shape is 'square':
        selem = skimage.morphology.square(blur_size)
    elif selem_shape is 'disk':
        selem = skimage.morphology.disk(blur_size)
    else:
        return RuntimeError('Structural element shape must be square or disk.')
    img_filt = skimage.filters.median(image, selem)

    return img_filt

# Define a function to threshold an image
def thresh_img(img, thresh_type='min', thresh='otsu'):
    """
    Threshold an image, using a specified threshold, or Otsu threshold

    Returns Boolean where segmented objects are True and background is False
    """

    if thresh is 'otsu':
        img_thresh = skimage.filters.threshold_otsu(img)
    elif type(thresh)==str:
        return RuntimeError('Threshold should be "otsu" or an integer.')
    else:
        img_thresh = thresh

    if thresh_type is 'min':
        return img > img_thresh
    elif thresh_type is 'max':
        return img < img_thresh
    else:
        return RuntimeError('Threshold type should be "max" or "min."')

# Define a function to remove objects from Boolean image
def remove_obj(img_filt, bool_img, rmv_small=True, too_small=50,
                                   rmv_large=True, too_large=5000,
                                   rmv_ecc=True, ecc_thresh=0.85):
    """
    Input: Filtered image and boolean image and a threshold size
    Output: Boolean image with objects that are too small (if rmv=small)
            or too slarge (if rmv=large)

    Note that regions are not numbered
    """

    # Enumerate all objects (takes boolean image)
    bool_img_lab, n_cells = skimage.measure.label(bool_img, return_num=True,
                                                  background=0)

    # Feed enumerated objects to region props, to get area of each object
    bool_img_props = skimage.measure.regionprops(bool_img_lab,
                                                intensity_image=img_filt)

    # Iterate through each object
    n_rmv = 0
    for prop in bool_img_props:
        # Check for objects that are too small.
        if rmv_small:
            if prop.area < too_small:
                bool_img_lab[bool_img_lab==prop.label] = 0
                n_rmv +=1

        # Check for objects that are too large.
        if rmv_large:
            if prop.area > too_large:
                bool_img_lab[bool_img_lab==prop.label] = 0
                n_rmv +=1

        # Check for objects that are not eccentric enough
        if rmv_ecc:
            if prop.eccentricity < ecc_thresh:
                bool_img_lab[bool_img_lab==prop.label] = 0
                n_rmv +=1

        # Make it a boolean again
        bool_img_bw = bool_img_lab > 0

    return bool_img_bw

# Define a function to (in order): remove outlier pixels, remove uneven illumination,
# segment cells with a threshold, remove cells of wrong size and shape, and
# return a labeled image

def img_analyze(img, pix_blur=3, selem_shape='square',
                back_blur=500,
                thresh_type='min', thresh='otsu',
                too_small=50, too_large=5000, ecc_thresh=0.85):
    """
    Input:
    img = data
    pix_blur = size of structuring element to remove outlier pixels
    selem_shape = shape of structuring element to remove outlier pixels
    back_blur = size of Gaussian blur to remove uneven illumination
    thresh_type = 'min' cells are brighter, 'max' cells are darker
    thresh = threshold with otsu or a number
    too_small = minimum object size
    too_large = maximum object size

    Returns:
    Labeled image with segmented cells
    """

    # Remove outlier pixels
    # This line fails
    # img = outlier_pixel(img, pix_blur, selem_shape=selem_shape)
    img_filt = outlier_pixel(img, pix_blur, selem_shape=selem_shape)

    # Remove uneven illumination (after outlier pixels are gone)
    img_filt = even_illumin(img_filt, back_blur)

    # Threshold the filtered image
    img_bool = thresh_img(img_filt, thresh_type=thresh_type, thresh=thresh)

    # Remove objects that are wrong size or shape
    img_bool_rmv = remove_obj(img_filt, img_bool,
                              too_small=too_small, too_large=too_large,
                              ecc_thresh=ecc_thresh)

    # Return the labeled mask
    return skimage.measure.label(img_bool_rmv, background=0)
