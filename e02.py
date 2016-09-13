# Exercise 2.2

# Import data as lines
with open('data/salmonella_spi1_region.fna', 'r') as f:
    f_lines = f.readlines()

salm_str = ''

# Data is stored on all lines except the first, so make a string with these
for i in range(len(f_lines) - 1):
    # Keep all characters except new line chracter
    line_str = f_lines[i + 1][:-1]
    if i < 3:
        print(line_str)
        print(f_lines[i + 1])
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
    """Find first index of all start codons in seq"""

    start_idx = []

    for i in range(len(seq)):
        current_codon = seq[i : i+3]
        if current_codon == 'ATG':
            start_idx.append(i)

    return tuple(start_idx)

def find_stop(seq):
    """Find first index of all stop codons in seq"""

    stop_idx = []

    for i in range(len(seq)):
        current_codon = seq[i : i+3]
        if current_codon == 'TGA' or current_codon == 'TAG' or current_codon == 'TAA':
            stop_idx.append(i)

    return tuple(stop_idx)

def in_frame(start,stop):
    """
    Determines if indices of start and stop codons
    allow those codons to be in frame
    """

    # Start and stop codon indices should be natural numbers
    if type(start) is not int or type(stop) is not int or start < 0 or stop < 0:
        return RuntimeError('Start and stop codon indices should be positive integers.')

    if (stop - start) % 3 == 0:
        return True
    else:
        return False

def longest_orf(seq):
    """Returns indices of largest open reading frame"""

    # Dummy value for longest_orf_len
    longest_orf_len = 0

    # Find indices of start and stop codons
    start_codons = find_start(seq)
    stop_codons = find_stop(seq)

    # Loop through start codons
    for i, start_codon in enumerate(start_codons):
        possible_stop = []

        for j, stop_codon in enumerate(stop_codons):

            # Check only stop codons downstream of the start codon
            if stop_codon > start_codon and in_frame(start_codon, stop_codon):
                # Append the index of possible stop codons
                possible_stop.append(stop_codon)

        # If possible stop codons were found
        if len(possible_stop) > 0:
            # Compute shortest length, i.e. difference from first (closest) stop codon
            length = possible_stop[0] - start_codon
        else:
            length = 0

        if length > longest_orf_len:
            longest_orf_len = length
            print(longest_orf_len)
            long_start = start_codon
            long_stop = possible_stop[0]

    return (long_start, long_stop, longest_orf_len)

# Part B

# Read in sequence as string
with open('salmonella.txt', 'r') as f:
    salm_list = f.readline()

salm_str = str(salm_list)

# Look for longest orf
salm_start, salm_stop, _ = longest_orf(salm_str)

# Part C

import bioinfo_dicts

def trans_seq(seq, material='DNA'):
    """translates a DNA or RNA sequence to protein
    Assumes start / stop codons are first and last codons"""

    # Check for valid material
    if material is not 'RNA' and material is not 'DNA':
        return RuntimeError('Invalid material')

    # Check for valid sequence length
    if len(seq) % 3 > 0:
        return RuntimeError('Sequence length should be divisible by 3 (only complete codons).')

    # Convert RNA to DNA, so that all input is uniform
    if material == 'RNA':
        seq = seq.replace('U','T')

    # Loop through sequence one codon at a time
    aa_seq = ''
    for i in range(0, len(seq), 3):
        next_codon = seq[i : i+3]

        # Check that next codon is legal
        if next_codon not in bioinfo_dicts.codons.keys():
            return RuntimeError(next_codon + ' is not a valid codon.')
        else:
            aa_seq += bioinfo_dicts.codons[next_codon]

    return aa_seq

# Translate the longest orf
salm_orf_dna = salm_str[salm_start : salm_stop + 3]

salm_orf_aa = trans_seq(salm_orf_dna, material='DNA')

# Write output to file
with open('longest_salm_orf.txt', 'w') as f:
    f.write(salm_orf_aa)

# Blast the longest ORF,
# get two-component sensor histidine kinase BarA [Salmonella enterica]
