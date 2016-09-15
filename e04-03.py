# Exercise 4.3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils
import numba

# Pretty plot settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 13,
        'legend.fontsize': 16, 'xtick.labelsize': 16,
        'ytick.labelsize': 16}
sns.set(rc=rc)

# If the RNA Polymerase spends more time walking backward than
# you expect from random diffusive motion, then it is actually
# backtracking. Instead of deriving an analytical expression for
# the distribution of times spent walking backward, we can find
# it by Monte Carlo simulation and drawing random numbers from
# known probability distributions.

# Part A

# Define a function that returns how many steps a wandering walker
# takes to get to x=+1 (i.e. exit the backtrack)

@numba.jit(nopython=True)
def back_track_steps(start=0, stop=1):
    """Returns number of steps for a random walker to get from start to stop"""

    w_loc = start
    n_steps = 0

    # Stop when walker location = stop, or when it falls off RNA
    while w_loc < stop and w_loc > -2000:
        next_step = np.random.random()
        if next_step < 0.5:
            w_loc -= 1
        else:
            w_loc += 1
        n_steps += 1

    return n_steps

# # Part B: Take many backtracks

n_reps = 10000
t_bt = np.empty(n_reps)

for i in range(n_reps):
    t_bt[i] = back_track_steps()

# Part C: Plot the results
plt.close()

_ = plt.hist(t_bt, bins=100, normed=True)

plt.show()

# Part D: Compute and plot ECDF
x_t_bt, y_t_bt = bootcamp_utils.ecdf(t_bt)

# Plot options
alpha = 0.5

plt.figure()
_ = plt.semilogx(x_t_bt, y_t_bt, '.', alpha=alpha)

# Plot settings
plt.xlabel('Number of steps')
plt.ylabel('eCDF')

plt.show()

# Part E: Plot CCDF on loglog plot

plt.figure()

_ = plt.loglog(x_t_bt, 1 - y_t_bt, '.', alpha=alpha)

# Plot settings
plt.xlabel('Number of steps')
plt.ylabel('CCDF')

plt.show()
