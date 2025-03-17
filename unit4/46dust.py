#46dust.py by Carolina_mendivil

'''
Prior to doing sequence searches, people often mask low complexity 
sequence to prevent finding huge numbers of meaningless alignments. 
One of the common programs that does this task is called dust. 

Write a python version.

Input: multi-FASTA file of DNA
Output: multi-FASTA file of DNA with low complexity regions masked
Change all low-complexity regions to 'N' in the output
Provide parameters for fasta file, window size, and entropy
Your command line should look like the one below, 
provided you soft-linked the FASTA file and defined the window size as 20 
and entropy threshold at 1.4.
'''

#p(x) = # of nt in window / window size

import mcb185
import sys
import math

w = int(sys.argv[2])			#window= 20 characters long
ent_thresh = float(sys.argv[3])	#entropy is 1.4

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for nt in seq:
		for nt in range(len(seq) - w + 1):
			s = seq[nt:nt+w]
			a = s.count('A')
			c = s.count('C')
			g = s.count('G')
			t = s.count('T')
			nts = a, c, g, t
			for i in nts:
				hlist = []
				if i == 0: continue
				p = i/w
				h = p * math.log2(p)
				hlist.append(h)
			H = -1 * math.fsum(hlist)
			if H < ent_thresh:
				newseq = seq.replace(seq[nt], 'N')
			print(newseq)
			
'''
command:
python3 46dust.py ecoli.fa.gz 20 1.4
= 
