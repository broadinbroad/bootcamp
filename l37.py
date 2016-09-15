# Lesson 37: Performing regressions

import numpy as np
import pandas as pd

# We'll use scipy.optimize.curve_fit to do the nonlinear regression
import scipy.optimize

import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 20,
        'legend.fontsize': 16, 'xtick.labelsize': 16,
        'ytick.labelsize': 16}
sns.set(rc=rc)

# Import data
df = pd.read_csv('data/bcd_gradient.csv', comment='#')

# Rename columns (with dictionary)
df = df.rename(columns={'fractional distance from anterior': 'x',
                '[bcd] (a.u.)': 'I_bcd'})

# Plot
_ = plt.plot(df['x'], df['I_bcd'], '.')

plt.show()

# Specify function for curve first

def gradient_model(x, I_0, a, lam):
    """Model for bicoid gradient: exponential decay + background"""

    if np.any(np.array(x) < 0):
        raise RuntimeError('x must be positive.')
    if np.any(np.array([I_0, a, lam]) < 0):
        raise RuntimeError('all params must be positive')

    return a + I_0 * np.exp(-x / lam)

# Specify initial guess
# one decay length is to got to ~1/3 of its value
I_0_guess = 0.6
a_guess = 0.2
lam_guess = 0.25

p0 = np.array([I_0_guess, a_guess, lam_guess])

# Fit the curve
popt, _ = scipy.optimize.curve_fit(gradient_model, df['x'], df['I_bcd'], p0=p0)

# Plot the fit
I_0_opt, a_0_opt, lam_opt = p0
x_opt = np.linspace(0, 1, 400)

# Asterisk splits up the tuple!
_ = plt.plot(x_opt, gradient_model(x_opt, *tuple(popt)), '-k')
