# Lesson 28

import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils

# Pretty plot settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 20,
        'legend.fontsize': 16}
sns.set(rc=rc)

# Load beak depth data
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

# Compute confidence intervals of mean and standard deviation of
# beak depth data
n_reps = 10000
bs_1975_mean = bootcamp_utils.draw_bs_reps(bd_1975, np.mean, size=n_reps)
bs_1975_std = bootcamp_utils.draw_bs_reps(bd_1975, np.std, size=n_reps)

bs_2012_mean = bootcamp_utils.draw_bs_reps(bd_2012, np.mean, size=n_reps)
bs_2012_std = bootcamp_utils.draw_bs_reps(bd_2012, np.std, size=n_reps)

# Compute confidence intervals
mean_1975_ci = bootcamp_utils.conf_int(bs_1975_mean,interval=95)
std_1975_ci = bootcamp_utils.conf_int(bs_1975_std,interval=95)
mean_2012_ci = bootcamp_utils.conf_int(bs_2012_mean,interval=95)
std_2012_ci = bootcamp_utils.conf_int(bs_2012_std,interval=95)

# Plot ECDF random samples n_rep times
n_reps = 100
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    x_bs, y_bs = bootcamp_utils.ecdf(bs_sample)
    _ = plt.plot(x_bs, y_bs, '.', color='gray', alpha=0.2)

# Compute ECDF
x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)

# Plot the ECDF
_ = plt.plot(x_1975, y_1975, '-g')

# Axis labels
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')

plt.show()
