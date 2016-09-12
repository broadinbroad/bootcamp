# codon = 'AUG' # Methionine and start codon
codon = input("What is the codon? ")
codon_list = ['UAA', 'UAG', 'UGA']
codon_tuple = tuple(codon_list)

if codon == 'AUG':
    print('This codon is the start codon.')
elif codon in codon_tuple:
    print('This is a stop codon.')
else:
    print('This codon is not the start or stop codon.')

print('This always prints.')
