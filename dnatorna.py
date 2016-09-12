"""
Convert DNA sequences to RNA
"""

def rna(seq):
    """Convert a DNA sequence to RNA"""

    # Want to return uppercase sequences
    seq = seq.upper()

    return seq.replace('T', 'U')
