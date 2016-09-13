## Exercise 1.3

# Part A: Find reverse complement without reversed() function

def complement_base(base, material='DNA'):
    """Takes 'base', returns complement base"""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else:
            raise RuntimeError('Invalid material.')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Cc':
        return 'G'
    elif base in 'Gg':
        return 'C'
    else:
        raise RuntimeError('Invalid base input.')

def reverse_complement(seq, material='DNA'):
    """Return reverse complement of sequence, whether DNA or RNA."""

    # Reverse the sequence, so that it goes 3' -> 5'
    rev_seq = seq[::-1]

    # Initialize empty string
    rev_comp = ''

    for i, base in enumerate(rev_seq):
        rev_comp += complement_base(base, material=material)

    return(rev_comp)


## Part B: reverse complement without for loops!

def reverse_complement_no_loop(seq, material='DNA'):
    """Return reverse complement of seq, without using for loops"""

    # Make it uppercase
    seq = seq.upper()

    # Convert upper case letters to appropriate lower case (protects from replacing twice)
    if material == 'DNA':
        seq = seq.replace('A','t')
    elif material == 'RNA':
        seq = seq.replace('A','u')
    seq = seq.replace('T','a')
    seq = seq.replace('U','a')
    seq = seq.replace('C','g')
    seq = seq.replace('G','c')

    # Reverse the sequence
    seq = seq[::-1]

    # Return as upper case
    return seq.upper()



## Exercise 1.4

# Approach that starts with longest and moves to shortest slices

def common_substring(str_1, str_2):
    """Look for longest common substring of str_1 and str_2"""

    # Specify shorter and longer strings
    if len(str_1) <= len(str_2):
        short_str = str_1
        long_str = str_2
    else:
        short_str = str_2
        long_str = str_1

    # Initialize substring as longest possible substring
    substring = short_str

    # Save length of short string as variable
    len_short_str = len(short_str)

    # Iterate through decreasingly smaller fragments of ref_str
    if substring in long_str:
        return(substring)
    else:
        for i in range(len_short_str):
            length_substring = i + 1
            n_substrings = len_short_str - i
            for j in range(n_substrings):
                start_index = j
                end_index = j + length_substring
                substring = short_str[start_index:end_index]
                if substring in long_str:
                    answer = substring
        return(answer)

## Exercise 1.5

# Part A: A function compare number of open and closed parentheses

def valid_paren(structure):
    """
    Test that parentheses of a given structure are valid.
    Returns TRUE if number of ( is equal to number of ).
    """

    # Count the number of open and closed parentheses
    n_open = structure.count('(')
    n_closed = structure.count(')')

    # Compare the number
    return(n_open == n_closed)

# Part B: dot-parens to tuples of base pairs

def dotparen_to_bp(structure):
    """Given a valid dot-paren structure, return a tuple of base pairs"""

    # Check for an equal number of ( and )
    if valid_paren(structure) == False:
        raise RuntimeError('Not an equal number of ( and )')

    # Find indices of base pairs
    else:
        # Initialize empty lists of open and closes paren. indices
        open_paren = []
        closed_paren = []

        # Generate a list of the indices of open and closed parentheses
        for i, substruct in enumerate(structure):
            # If substructure is open paren, store index in open paren list
            if substruct == '(':
                open_paren += [i]

            # If substructure is closed paren, store index in closed paren list
            elif substruct == ')':
                closed_paren += [i]

        # Initialize list to store pairs
        pairs = []

        # Iterate through the closed_paren
        for i, index in enumerate(closed_paren):

            # Store the closed index
            closed_index = index

            # Iterate through open paren
            for j in range(len(open_paren)):
                # Overwrite open_index; since open_index is increasing,
                # we get the largest value of open_paren that is still
                # less than closed_index
                if open_paren[j] < closed_index:
                    open_index = open_paren[j]
                    index_to_pop = j

            # Store the base pair as a tuple in the list of pairs
            pairs += [(open_index, closed_index)]

            # Remove  open_index from the list open_paren so it cannot be a part of another base pair
            open_paren.pop(index_to_pop)

        # Convert our list of tuples to a tuple of tuples
        pairs_tuple = tuple(pairs)

        # Return the tuple of tuples
        return(pairs_tuple)

# Part C: Check for sterics

def valid_steric(bp_tuple):
    """Given base pairings as a tuple of tuples,
    return True if structure is sterically allowed."""

    for i in range(len(bp_tuple)):
        open_index = bp_tuple[i][0]
        closed_index = bp_tuple[i][1]
        if closed_index - open_index < 4:
            return False
        else:
            return True

# Part D: Write validator function

def rna_ss_validator(seq, sec_struc, wobble=True):
    '''
    Validates that sequence 'seq' can take on secondary structure 'sec_struc'
    specified in dot-paren notation
    '''

    # Turn structure to tuple of tuples of open and closed indices
    bp_tuple = dotparen_to_bp(sec_struc)

    # Check that the secondary structure is valid
    if valid_paren(sec_struc) == False:
        return RuntimeError('Not an equal number of ( and ).')
    if valid_steric(bp_tuple) == False:
        return RuntimeError('Structure is not sterically allowed.')

    # Check that nucleotide bases of pairs do in fact match
    for i in range(len(bp_tuple)):

        # Pull out indices of pairs in sequence list
        open_index = bp_tuple[i][0]
        closed_index = bp_tuple[i][1]

        # Check that the bases are complements
        if seq[open_index] == complement_base(seq[closed_index]):
            print('I didn\'t optimize.')
        # If they are not complements, check for wobble or return False
        else:
            # If wobble = True, check for wobble pair
            if wobble == True:
                if seq[open_index] == 'U' and seq[closed_index] == 'G':
                    print('I didn\'t optimize.')
                elif seq[open_index] == 'G' and seq[closed_index] == 'U':
                    print('I didn\'t optimize.')
                else:
                    return False
            # If wobble is false, don't check for wobble pair
            else:
                return False

    return True
