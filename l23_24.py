# Lessons 23-24
import numpy as np
import scipy.stats

# import bootcamp_utils

# Plotting tool
import matplotlib.pyplot as plt

# Plot options in seaborn
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 20,
        'legend.fontsize': 20}
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

# Slice out data
iptg = data_txt[:,0]
gfp = data_txt[:,1]

# Slice out stanard error
sem = data_txt[:,2]


# plot the data
# plt.semilogx(iptg, gfp, linestyle='none', marker='.')
plt.errorbar(iptg, gfp, yerr=sem, linestyle='none',
             marker='.')

# Axes and Title
plt.xlabel('IPTG Concentration (mM)')
plt.ylabel('Normalized GFP')
plt.xscale('symlog')

plt.title('IPTG titration')

# margins
plt.margins(0.2)

plt.show()
plt.close()

# Plot CDFs (instead of histograms)

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

    return x, y

# Load the food data. (no need to specify delimiter)
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Compute ECDF
x_high, ecdf_high = ecdf(xa_high)
x_low, ecdf_low = ecdf(xa_low)

# Plot the ecdf
plt.plot(x_high, ecdf_high, marker='.', linestyle='none',
         alpha=0.5)
plt.plot(x_low, ecdf_low, marker='.', linestyle='none',
         alpha = 0.5)

# Axes and title
plt.xlabel('Crossectional area ($\mu m ^2$)')
plt.ylabel('ECDF')

plt.legend(('high concentration', 'low concentration'), loc='lower right')
plt.margins(0.05)

plt.show()
