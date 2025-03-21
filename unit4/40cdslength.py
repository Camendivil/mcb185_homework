import gzip
import sys 

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] == '#': continue
        words = line.split()
        if words[2] != 'CDS': continue
        beg = int(words[3])
        end = int(words[4])
        print(end - beg + 1)
        
        
'''
put this into terminal:
python3 40cdslength.py ../..//MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz
'''
