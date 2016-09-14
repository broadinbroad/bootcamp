import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils

# Pretty plot settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 20,
        'legend.fontsize': 16}
sns.set(rc=rc)

# Import data (no header or comments)
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

# Compute mean of many boostrap repeats
n_reps = 100000
bs_replicates_1975 = np.zeros(n_reps)

for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates_1975[i] = np.std(bs_sample)

conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])

n_reps = 100000
bs_replicates_2012 = np.zeros(n_reps)

for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_replicates_2012[i] = np.std(bs_sample)

conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])

# ## ECDF plot
#
# # Compute ecdf
# x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)
# x_2012, y_2012 = bootcamp_utils.ecdf(bd_2012)
# x_1975_bs, y_1975_bs = bootcamp_utils.ecdf(bs_sample)
#
# # Plot ecdf
# _ = plt.plot(x_1975, y_1975, '.')
# _ = plt.plot(x_2012, y_2012, '.')
# _ = plt.plot(x_1975_bs, y_1975_bs, '.')
#
# # Axes and legend
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
#
# plt.legend(('1975', '2012', 'Bootstrap'), loc='lower right')
#
# plt.show()
