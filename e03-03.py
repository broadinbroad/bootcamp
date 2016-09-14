# Exercise 3.3

import numpy as np
import matplotlib.pyplot as plt

# Pretty plot settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 20,
        'legend.fontsize': 16}
sns.set(rc=rc)

# Define functions for dr/dt and df/dt

def dr_dt(r, f, alpha=1, beta=0.2):
    """Compute dr/dt, time derivative of rabbit population"""

    return alpha * r - beta * f * r

def df_dt(r, f, delta=0.3, gamma=0.8):
    """Compute df/dt, time derivative of fox population"""

    return delta * f * r - gamma * f

# Define time range to numerically integrate over
delta_t = 0.001
t_range = np.arange(0, 60, delta_t)

# Initialize arrays to store rabbit and fox populations
r = np.zeros_like(t_range)
f = np.zeros_like(t_range)

# Set initial conditions (at time t=0)
r[0] = 10 # rabbits
f[0] = 1 # fox

# Numerically integrate
for i in range(1, len(t)):
    delta_r = dr_dt(r[i-1], f[i-1]) * delta_t
    delta_f = df_dt(r[i-1], f[i-1]) * delta_t

    r[i] = r[i-1] + delta_r
    f[i] = f[i-1] + delta_f
