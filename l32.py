# Lesson 32: Practice with pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils

# Pretty plot settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 13,
        'legend.fontsize': 16}
sns.set(rc=rc)

# Read in frog data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

## Problem 1
# Part A: Extract time of all impacts that had adhesive strength > 2000 Pa
df_time_sticky = df.loc[df['adhesive strength (Pa)'] < -2000, ['impact time (ms)']]

# Part B: Impact force and adhesive force for all Frog II's strikes.
II_forces = df.loc[df['ID']=='II', ['impact force (mN)', 'adhesive force (mN)']]

# Part C: Extract adhesive force and time for juvenile frogs (III and IV)
juv_force_time = df.loc[ df['ID'].isin(['III', 'IV']),
                        ['adhesive force (mN)', 'impact time (ms)']]

# Same thing
juv_force_time_2 = df.loc[ (df['ID']=='III') & (df['ID']=='IV'),
                           ['adhesive force (mN)', 'impact time (ms)']]

## Problem 2

# Long way
frog_ids = ('I', 'II', 'III', 'IV')

# Iterate through frogs and compute means
means = np.empty(len(frog_ids))
for i, ID in enumerate(frog_ids):
    df_one_frog = df.loc[ df['ID']==ID, ['impact force (mN)']]
    means[i] = df_one_frog.mean()

# Part A: Use groupby() to compute standard deviation for each frog_ids
df_impf = df.loc[:, ['ID', 'impact force (mN)']]
df_impf_grp = df_impf.groupby('ID')
df_impf_std = df_impf_grp.apply(np.std)

# Part C: Can apply function to more than one column of numbers
df_forces = df.loc[:, ['ID', 'impact force (mN)', 'adhesive force (mN)']]
df_forces_grp = df_forces.groupby('ID')
df_forces_cv = df_forces_grp.apply(bootcamp_utils.coeff_var_data)

# Part D: use .agg() to do many functions
# (generates a DataFrame with a two level header!)
df_forces_allstat = df_forces_grp.agg([np.mean, np.median, np.std,
                                      bootcamp_utils.coeff_var_data])
