import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pretty plot settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 13,
        'legend.fontsize': 16}
sns.set(rc=rc)

# Import data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Practice selecting data subsets
df_big_force = df.loc[df['impact force (mN)'] > 1000, :]

# Good for viewing single experiment
df_42 = df.loc[42, :]

# To pull out a single day / specific parameters
df.loc[(df['date']=='2013_05_27') & (df['trial number']==3)
        & (df['ID']=='III'), :]

# Pull out only a specific set of measurements
df.loc[df['ID']=='I', ['impact force (mN)', 'adhesive force (mN)']]

# n.b. that this is a boolean operator - an array of Trues and Falses
df['ID']=='I'

# Make plots to investigate relationship between various observed quantities
plt.plot(df['total contact area (mm2)'], df['adhesive force (mN)'], '.')

plt.xlabel('total contact area (mm2)')
plt.ylabel('adhesive force (mN)')

plt.show()

# Same plot, using pandas
df.plot(x='total contact area (mm2)', y='adhesive force (mN)', kind='scatter')

plt.show()

# Automatically compute all correlation coefficients for any pairs of numerical data
df.corr()

# To look at a specific relationship
df.loc[:, ['impact force (mN)', 'adhesive force (mN)']].corr()

# Rename column names if you hate long columns (pandas does not do operations in place)
df_rename = df.rename(columns={'impact force (mN)': 'impf'})

# Names without spaces (or characters that imply python syntax) allow easier indexing!
df_rename['impf'] == df_rename.impf
