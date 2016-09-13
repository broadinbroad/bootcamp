# Import dictionaries for bioinformatics
import bioinfo_dicts as bi_dicts

def one_to_three(seq):
    """Take a protein sequence from one to three letter abbreviations"""
    # uppercase
    seq = seq.upper()

    # BUild conversion
    aa_list = []
    for amino_acid in seq:
        # Check for legal amino amino_acid
        if amino_acid in bi_dicts.aa.keys():
            aa_list += [bi_dicts.aa[amino_acid], '-']
        else:
            raise RuntimeError(amino_acid + ' is not a valid amino acid.')

    # Join every element except for the last, because we don't want the trailing dash
    return ''.join(aa_list[:-1])


try:
    import gc_content
    have_gc = True
except ImportError as e:
    have_gc = False

seq = 'ATCGCACGTGCGCGATATACGCCACAGT'

if have_gc:
    print(gc_content.gc(seq))
else:
    print((seq.count('G') + seq.count('C'))/len(seq))
