# Lesson 34

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pretty plot settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 200,
        'legend.fontsize': 16, 'xtick.labelsize': 16,
        'ytick.labelsize': 16}
sns.set(rc=rc)


# Import data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Rename columns
df = df.rename(columns={'impact force (mN)': 'impf'})

# Use groupby() to quickly compute means for different frogs
gb_frog = df.groupby('ID')

mean_impf = gb_frog['impf'].mean()
sem_impf = gb_frog['impf'].sem()

# Make a bad bar graph
plt.bar(np.arange(4), mean_impf, yerr=sem_impf, ecolor='black',
        tick_label=['I', 'II', 'III', 'IV'], align='center')
plt.ylabel('Impact Force')
plt.close()

# Use seaborn and tidy data!
sns.barplot(data=df, x='ID', y='impf')
plt.xlabel('')
plt.ylabel('impact force (mN)')
plt.close()

# Let's plot all of our data!
sns.swarmplot(data=df, x='ID', y='impf')
plt.close()

# Let's color the data by a different feature
sns.swarmplot(data=df, x='ID', y='impf', hue='date', size=15)
plt.gca().legend_.remove()

plt.show()

# Make a boxplot (better than bar graph because it includes uneven spread on both sides)
# percentiles do not assume a probability distribution, identifies outliers
plt.figure()
sns.boxplot(data=df, x='ID', y='impf')

plt.show()
