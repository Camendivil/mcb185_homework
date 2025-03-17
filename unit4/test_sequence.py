#test_sequence.py by Carolina_Mendivil


import sequence

print(sequence.transcribe('ACGT'))
print(sequence.revcomp('AAACGT'))
print(sequence.translate('ATGCCCTAATAGTGA'))

s = 'ACGTGGGGGGCATATG'
print(sequence.gc_comp(s))
print(sequence.gc_skew(s), sequence.gc_skew(sequence.revcomp(s)))