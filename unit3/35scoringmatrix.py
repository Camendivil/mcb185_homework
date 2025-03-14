#35scoringmatrix.py by Carolina_mendivil

'''
Write a program that can print out a match-mismatch scoring matrix. 
The alphabet, match, and mismatch are all command line parameters.
'''

import sys

nts = sys.argv[1]
matched = sys.argv[2]
mismatched = sys.argv[3]



print('   ', end='')         
for nt in nts:
	print(nt, end='  ')        
print()


for nt0 in nts:
	print(nt0, end=' ')                 
	for nt1 in nts:       
		if nt0 == nt1:
			print(matched, end=' ')     
		else:
			print(mismatched, end=' ')   
	print('\n', end='') 


'''
write it in the terminal like this:
python3 35scoringmatrix.py ACGT +1 -1

'''


