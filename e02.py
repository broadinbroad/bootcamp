# Exercise 2.2

# Import data as lines
with open('data/salmonella_spi1_region.fna', 'r') as f:
    f_lines = f.readlines()

# Data is stored on all lines except the first, so make a string with these
for i in range(len(f_lines) - 1):
    line_str = f_lines[i + 1][:-2]
    salm_str += line_str

# Write this string to a text file
with open('e02-2.txt', 'w') as f:
    f.write(salm_str)

# Exercise 2.3
