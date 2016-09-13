import numpy as np
import scipy.special
import matplotlib.pyplot as plt

# Seaborn settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 18, 'lines.markersize': 10}
sns.set(rc=rc)

# X-values to evaluate
x = np.linspace(-15, 15, 400)

# The normalized intensity (the y-value)
norm_I = 4 * (scipy.special.j1(x) / x)**2

# Plot the Airy Disk
plt.plot(x, norm_I, marker='.', linestyle='none')

# Axis labels
plt.xlabel('$x$')
plt.ylabel('$I(x)/I_0$')

# DOn't cut off data
plt.margins(0.02)

# plt.show()

# Processing spike data
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')

# Slice out time and voltage
t = data[:,0]
V = data[:,1]

# Plot the data (close all other plots first)
plt.close()
plt.plot(t, V)
plt.xlabel('t (ms)')
plt.ylabel('V ($\mu V$)')

# X limit of single spike
plt.xlim(1395, 1400)

plt.show()
