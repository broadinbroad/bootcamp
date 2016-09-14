# Use random number generation to simulate Luria-Delbruck distribution

import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils

# Pretty plot settings
import seaborn as sns
rc = {'lines.linewidth': 4, 'axes.labelsize': 25,
        'axes.titlesize': 30, 'lines.markersize': 13,
        'legend.fontsize': 16}
sns.set(rc=rc)

# Specify parameters
n_gen = 16 # generations

# Chance of having a beneficial mutation (v. small)
r = 1e-6

# Total number of cells at end of expt (survivors)
n_cells = 2**(n_gen - 1)

# Draw adaptive immunity samples from binomial distribution
n_samples = 100000
ai_samples = np.random.binomial(n_cells, r, size=n_samples)

# Plot results
# Count number of times each discrete result occurs
counts = np.bincount(ai_samples)
plt.plot(np.arange(len(counts)), counts, '.')

plt.show()

# Report mean and standard deviation
print('AI mean:', np.mean(ai_samples))
print('AI standard:', np.std(ai_samples))
print('AI Fano:', np.var(ai_samples) / np.mean(ai_samples))

# Function to draw out of random mutation hypothesis
def draw_random_mutation(n_gen, r):
    """Draw sample under random mutation hypothesis."""

    # Initiliaze number of mutations
    n_mut = 0

    # Through each generations
    for g in range(n_gen):

        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    # Initiliaze samples
    samples = np.empty(size)

    # Draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

# Do for random samples
rm_samples = sample_random_mutation(n_gen, r, size=100000)

print('Rm mean:', np.mean(rm_samples))
print('Rm standard:', np.std(rm_samples))
print('Rm Fano:', np.var(rm_samples) / np.mean(rm_samples))

# Plot ecdf
x_ai, y_ai = bootcamp_utils.ecdf(ai_samples)

x_rm, y_rm = bootcamp_utils.ecdf(rm_samples)

plt.close()
_ = plt.plot(x_ai, y_ai, '.')
_ = plt.plot(x_rm, y_rm, '.')

# Set margins, scale
plt.xscale('log')
plt.margins(0.02)

# axis labels
plt.xlabel('Number of survivors')
plt.ylabel('ECDF')

plt.show()
