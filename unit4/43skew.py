#43skew.py by Carolina_mendivil

'''
Let's write a program that uses a sliding window algorithm to compute GC 
composition and GC-skew along the length of a sequence.
'''

import sequence

seq = 'ACGTACGTGGGGACGTACGTCCCCC'
w = 10	# window is 10 characters long
for i in range(len(seq) - w + 1):	
	s = seq[i:i+w]	# substring for each window
	print(i, sequence.gc_comp(s), sequence.gc_skew(s)) #composition and skew functions you just added to your library