#42ntcomp.py by Carolina_mendivil

'''
Let's write a program 42ntcomp.py that calculates the composition of nucleotides in a FASTA file.
This is a very simple modification of the previous program. 
We will make several variations of this program. 
The first one calculates the GC composition of each sequence separately.
'''


import sys
import mcb185


for defline,seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
	