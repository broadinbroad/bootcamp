# Exercise 2.2

# Import data as lines
with open('data/salmonella_spi1_region.fna', 'r') as f:
    f_lines = f.readlines()

salm_str = ''

# Data is stored on all lines except the first, so make a string with these
for i in range(len(f_lines) - 1):
    line_str = f_lines[i + 1][:-2]
    salm_str += line_str

# Write this string to a text file
with open('salmonella.txt', 'w') as f:
    f.write(salm_str)

# Exercise 2.3

# Part A

def gc_content(seq):
    """Compute GC content of seq"""

    return (seq.count('G') + seq.count('C'))  / len(seq)

def gc_blocks(seq, block_size):
    """
    seq = DNA sequence
    block_size = cut DNA sequence into non overlapping blocks of this size

    Compute GC content for each block, returns as tuple.
    """

    # Check that block_size is valid
    if type(block_size) is not int or block_size < 1 or block_size > len(seq):
        return RuntimeError('Block size must be positive integer less than sequence length.')

    gc_list = []

    # Use floor division to find number of blocks
    n_blocks = len(seq) // block_size

    for i in range(n_blocks):
        start_idx = block_size * i
        end_idx = block_size * (i+1)
        block_gc = gc_content(seq[start_idx : end_idx])
        gc_list.append(block_gc)

    return tuple(gc_list)

# Part B

def gc_map(seq, block_size, gc_thresh):
    """
    Takes seq, and computes gc content of each block of size block_size
    Blocks with gc content above gc_thresh are returned uppercase
    Blocks with gc content below gc_thresh are returned lowercase
    """
    # GC threshold should be >0 and < 1
    if gc_thresh < 0 or gc_thresh > 1:
        return RuntimeError('GC threshold should be between 0 and 1.')

    # Compute GC content of each block
    gc_seq_blocks = gc_blocks(seq, block_size)

    # Store number of blocks
    n_blocks = len(gc_seq_blocks)

    # Build return sequence by iterating through blocks
    return_seq = ''
    for i in range(n_blocks):
        start_idx = block_size * i
        end_idx = block_size * (i+1)

        # Make sequence uppercase if GC content >= threshold
        if gc_seq_blocks[i] >= gc_thresh:
            return_seq += seq[start_idx:end_idx].upper()

        # Make sequence lowercase if GC content < threshold
        else:
            return_seq += seq[start_idx : end_idx].lower()

    return return_seq

# Part C

# Read in sequence as string
with open('salmonella.txt', 'r') as f:
    salm_list = f.readline()

salm_str = str(salm_list)

# Specify block size and gc threshold
block_size = 1000
gc_thresh = 0.45

# Map the salmonella sequence
salm_map = gc_map(salm_str, block_size, gc_thresh)

# Part D

# Define a function to tidy output before writing to file
def tidy_output(str, line_len=60, sep='\n'):
    """Returns str as blocks of length line_len separated by sep character"""

    sepd_str = ''
    for i in range(0, len(str), line_len):
        sepd_str += str[i : i+line_len] + sep

    return sepd_str

# Steal header from original FASTA file
f_direc = 'C:\\Users\\hklum\\Documents\\Year 3\\BE 203 Programming Bootcamp\\git\\bootcamp\\data\\'

with open(f_direc + 'salmonella_spi1_region.fna', 'r') as f:
    header = f.readline()

header_str = str(header)

# Tidy and store the salmonella Map
salm_map_tidy = tidy_output(salm_map, line_len=60)

with open(f_direc + 'salmonella_map.fna', 'w') as f:
    f.write(header_str + salm_map_tidy)

# Exercise 2.4

# Part A

def find_start(seq):
    """Find indices of first base of all start codons in seq"""

    start_idx = []

    for i in range(len(seq)):
        current_codon = seq[i : i+3]
        if current_codon == 'ATG':
            start_idx += i

    return tuple(start_idx)

def find_stop(seq):
    """Find indices of first of all stop codons in seq"""

    stop_idx = []

    for i in range(len(seq)):
        current_codon = seq[i : i+3]
        if current_codon == 'TGA' or current_codon == 'TAG' or current_codon == 'TAA':
            stop_idx += i

    return tuple(stop_idx)

def in_frame(start,stop):
    """
    Determines if indices of start and stop codons
    allow those codons to be in frame
    """

    # Start and stop codon indices should be natural numbers
    if type(start) is not int or type(stop) is not int or start < 1 or stop < 1:
        return RuntimeError('Start and stop codon indices should be positive integers.')

    if (stop - start) % 3 == 0:
        return True
    else:
        return False
