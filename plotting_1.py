import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Plot options (set matplotlib rc params)
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18, 'legend.fontsize': 18}
sns.set(rc=rc)

# Load the food data. (no need to specify delimiter)
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Find range for bin boundaries
global_min = np.min(np.concatenate((xa_low, xa_high)))
global_max = np.max(np.concatenate((xa_low, xa_high)))

# Make bin boundaries (end should be > actual end, so it's included)
bins = np.arange(global_min-50, global_max+50, 50)

# Plot the data as a histogram
_ = plt.hist(xa_low, bins=bins, normed=True, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, bins=bins, normed=True, histtype='stepfilled', alpha=0.5)

# X and Y labels
plt.xlabel('Cross-sectional area ($\mu m^2$)')
plt.ylabel('Frequency')

# Legends
plt.legend(('low concentration', 'high concentration'), loc='upper right')

plt.show()

# Save the figure
plt.savefig('egg_area_histograms.svg', bbox_inches='tight')
