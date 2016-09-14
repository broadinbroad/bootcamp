import pandas as pd
import numpy as np

# Import cross sectional area data
# (no header, so misinterprets first data point as header)
df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('data/xa_low_food.csv', comment='#', header=None)

# Give better column names
df_low.columns = ['low']
df_high.columns = ['high']

# Concatenate the two together
df = pd.concat((df_low, df_high), axis=1)

# Write to a file (when index has no meaning, don't put indices in file)
df.to_csv('xa_combined.csv', index=False)

# Tidy the data
df_tidy = pd.melt(df, var_name='food density', value_name='cross-sectional area (sq. microns)').dropna()

# Using boolean logic is like wrting English sentences
print(df_tidy.loc[(df_tidy['food density'] == 'low') & (df_tidy['cross-sectional area (sq. microns)'] > 2100), :])

## Import lac data
# Example of header
# df = pd.read_csv('data/wt_lac.csv', comment='#')

## World Cup examples of indexing
#
# # Make dictionary of world cup gold records
# wc_dict = {'Klose': 16,
#            'Ronaldo': 15,
#            'Muller': 14,
#            'Fontaine': 13,
#            'Pele': 12,
#            'Koscis': 11,
#            'Klinsmann': 11}
#
# nation_dict = {'Klose': 'Germany',
#            'Ronaldo': 'Brazil',
#            'Muller': 'Germany',
#            'Fontaine': 'France',
#            'Pele': 'Brazil',
#            'Koscis': 'Hungary',
#            'Klinsmann': 'Germany'}
#
# # Making a data frame
# s_goals = pd.Series(wc_dict)
# s_nation = pd.Series(nation_dict)
#
# # Add things that have same indices, with dictionary of the two series
# df_wc = pd.DataFrame({'nation': s_nation, 'goals': s_goals})
#
# # Can't do df_wc['Fontaine'] because the name is the index.
# # instead, we can do mixed indexing! of strings and not strings
# df_wc.loc['Fontaine', :]
#
# # Use Boolean indexing
# df_wc.loc[df_wc['nation']=='Germany', :]
