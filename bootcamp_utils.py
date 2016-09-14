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

    returnnp.array([x, y])
