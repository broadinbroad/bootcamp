def ratio(x, y):
    """The ratio of 'x' to 'y'. """
    return x / y


# Functions need not have arguments
def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    """Simpler program than Deep Thought's, JB bets."""
    return 42


# Functions need not have return statements
def think_too_much():
    """Express Caeser's skepticism about Cassius"""

    print("""Yond Cassius has a lean and hungry look,
    He thinks too much; such men are dangerous.""")


def complement_base(base, material='DNA'):
    """Returns the Watson-Crick complement of my base."""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else:
            raise RuntimeError('Invalid material.')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return'C'
    else:
        return 'G'


def reverse_complement(seq, material='DNA'):
    """Make reverse complement of seq"""

    # Initialize an empty string
    rev_comp = ''

    # Loop through sequence in reverse
    for base in reversed(seq):

        # For each base, find and concatenate with complement
        rev_comp += complement_base(base, material=material)

    return rev_comp
