# 12phred.py by Carolina_Mendivil
# Write functions that convert quality value symbols into error rates and vice-versa. The ord() function returns the ASCII value of a letter. The chr() function turns an ASCII value into a letter.
# Q score
# Quality score
# PHRED score
# P is the probability of an incorrect call
#10**(Q/-10) = P
# Q = -10 * (math.log10(P))

import math

print('phred score to error probability')
def char_to_prob(char):
    q=ord(char)-33 # conversion from character to quality score
    if q<0: return None
    return 10 ** (-q/10)
print (char_to_prob('A'))

print('error probability to phred score')
def prob_to_char(prob):
    if prob <=0 or prob > 1: return None
    q=-10 * math.log10(prob)
    asciival = round(q + 33) # convert back to ascii value
    if asciival < 33 or asciival > 126: return None
    return chr(asciival)
print (prob_to_char(0.001))