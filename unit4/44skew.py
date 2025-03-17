#44skew.py by Carolina_mendivil

'''
Re-write 43skew.py as 44skew.py using the more efficient algorithm and 
then calculate GC-skew and GC composition in 1000 nt windows in 
the E.coli genome.
'''

import mcb185
import sequence
import sys

w = int(sys.argv[2])	#window is 10 char long
g = 0
c = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	g = seq[0:w].count('G')
	c = seq[0:w].count('C')
	print(sequence.gc_comp(seq[0:w]), sequence.gc_skew(seq[0:w]))		
	for i in range(len(seq) - w - 1):	
		if seq[i] == 'G':
			g -= 1
		if seq[i] == 'C':
			c -= 1
		if seq[i+w+1] == 'G':
			g += 1
		if seq[i+w+1] == 'C':
			c += 1
		gc_comp = (g + c) / w
		if g + c == 0: skew = 0
		else: skew = (g - c)/(g + c)
		print(i, gc_comp, skew)
	
	
'''
use this to time it:
time python3 44skew.py ecoli.fa.gz 1000

terminal response:
python3 44skew.py ecoli.fa.gz 1000  7.47s user 1.62s system 83% cpu 10.847 total
'''