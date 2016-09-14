# Exercise 3.2

import numpy as np
import matplotlib.pyplot as plt

# Pretty plot settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 20,
        'legend.fontsize': 16}
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
_ = plt.semilogx(wt_iptg, wt_fc, marker='.', linestyle='none')
_ = plt.semilogx(q18m_iptg, q18m_fc, marker='.', linestyle='none')
_ = plt.semilogx(q18a_iptg, q18a_fc, marker='.', linestyle='none')

# Axes and title
plt.title('Fold change v. IPTG')
plt.xlabel('IPTG conc. (mM)')
plt.ylabel('Fold change')

# Legend
plt.legend(('Wildtype', 'q18m', 'q18a'), loc='upper left')

plt.show()
plt.close()

# Part C: Define a function to compute fold change

def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Compute fold change as in Monod-Wyman-Changeux model

    c = concentration [mM]
    RK = ratio of number of repressors in cell to dissoc. const. for
         active repressor binding operator [mM]
    """

    KdA_exp = (1 + c/KdA)**2
    KdI_exp = (1 + c/KdI)**2

    large_fraction = RK * KdA_exp / (KdA_exp + Kswitch*KdI_exp)

    return (1 + large_fraction)**-1

# Part D: Compare data to theoretical fold change, using parameters

# Find range of concentrations
conc_min = np.min(np.concatenate((wt_iptg, q18m_iptg, q18a_iptg)))
conc_max = np.max(np.concatenate((wt_iptg, q18m_iptg, q18a_iptg)))

# Specify RK values
wt_RK = 141.5 # mM**-1
q18a_RK = 16.56 # mM**-1
q18m_RK = 1332 # mM**-1

# Generate theoretical data
conc_theor = np.logspace(np.log10(conc_min), np.log10(conc_max), 400)
wt_theor = fold_change(conc_theor, wt_RK)
q18m_theor = fold_change(conc_theor, q18m_RK)
q18a_theor = fold_change(conc_theor, q18a_RK)

# Plot theoretical and experimental data
_ = plt.semilogx(wt_iptg, wt_fc, '.b')
_ = plt.semilogx(q18m_iptg, q18m_fc, '.g')
_ = plt.semilogx(q18a_iptg, q18a_fc, '.r')

_ = plt.semilogx(conc_theor, wt_theor, '-b')
_ = plt.semilogx(conc_theor, q18m_theor, '-g')
_ = plt.semilogx(conc_theor, q18a_theor, '-r')

# Axes and title
plt.title('Fold change v. IPTG')
plt.xlabel('IPTG conc. (mM)')
plt.ylabel('Fold change')

# Legend
plt.legend(('Wildtype', 'q18m', 'q18a',
            'Wildtype model', 'q18m model', 'q18a model'),
            loc='upper left')

plt.show()
plt.close()

# Part E: Bohr parameter

def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """Compute Bohr parameter"""

    KdA_exp = (1 + c/KdA)**2
    KdI_exp = (1 + c/KdI)**2

    large_fraction = RK * KdA_exp / (KdA_exp + Kswitch*KdI_exp)

    return - (np.log(RK) + np.log(large_fraction))

def fold_change_bohr(bohr_parameter):
    """Return fold-change, computed from bohr_parameter"""

    return (1 + np.exp(-bohr_parameter))**-1

# Specify RK values
wt_RK = 141.5 # mM**-1
q18a_RK = 16.56 # mM**-1
q18m_RK = 1332 # mM**-1

# Generate theoretical data
conc_theor = np.logspace(np.log10(conc_min), np.log10(conc_max), 400)

# Compute bohr_parameters
wt_bohr = bohr_parameter(conc_theor, wt_RK)
q18m_bohr = bohr_parameter(conc_theor, q18m_RK)
q18a_bohr = bohr_parameter(conc_theor, q18a_RK)
theor_bohr = np.linspace(-6, 6, 400)

# Compute fold changes
wt_fc_bohr = fold_change_bohr(wt_bohr)
q18m_fc_bohr = fold_change_bohr(q18m_bohr)
q18a_fc_bohr = fold_change_bohr(q18a_bohr)
theor_fc_bohr = fold_change_bohr(theor_bohr)

# Plot theoretical fold change
alpha = 0.3
_ = plt.plot(theor_bohr, theor_fc_bohr, color='gray')
_ = plt.plot(wt_bohr, wt_fc_bohr, '.b', alpha=alpha)
_ = plt.plot(q18m_bohr, q18m_fc_bohr, '.g', alpha=alpha)
_ = plt.plot(q18a_bohr, q18a_fc_bohr, '.r', alpha=alpha)


# Axes and title
plt.title('Fold change v. Bohr parameter')
plt.xlabel('Bohr parameter')
plt.ylabel('Fold change')

# Legend
plt.legend(('Model', 'Wt', 'q18m', 'q18a'),
            loc='upper left')

plt.show()
