# Bootcamp Utilities:
"""A collection of statistical functions proved
useful for 55 students."""


# Import modules needed
import numpy as np

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
