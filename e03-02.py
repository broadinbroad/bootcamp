# Exercise 3.2

import numpy as np
import matplotlib.pyplot as plt

# Pretty plot settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 20,
        'legend.fontsize': 20}
sns.set(rc=rc)

# Part A: Load data
wt_txt = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m_txt = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a_txt = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)

# Part B: Plot IPTG concentration (col 1) v. fold change (col 2)
wt_iptg = wt_txt[:,0]
wt_fc = wt_txt[:,1]
q18m_iptg = q18m_txt[:,0]
q18m_fc = q18m_txt[:,1]
q18a_iptg = q18a_txt[:,0]
q18a_fc = q18a_txt[:,1]

# Plot
_ = plt.plot(wt_iptg, wt_fc, marker='.', linestyle='none')
_ = plt.plot(q18m_iptg, q18m_fc, marker='.', linestyle='none')
_ = plt.plot(q18a_iptg, q18a_fc, marker='.', linestyle='none')

# Axes and title
plt.title('Fold change v. IPTG')
plt.xlabel('IPTG conc. (mM)')
ply.ylabel('Fold change')

plt.show()
