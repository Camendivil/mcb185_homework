# 31entropy.py by Carolina_Mendivil

import sys
import math


probs = [] 				#initialize empty list probs
for arg in sys.argv[1:]: #gets all command line arguments except program name
    f = float(arg) 		#must convert to float since sys.argv store everything as a string
    if f <= 0 or f >= 1: sys.edit('error: not a probability') #makes sure all prob are 0-1
    probs.append(f) 	#adds valid probability to probs list


#Check if the probability sum up to 1
total = 0 						#initialize a variable to hold the sum of all probs
for p in probs: total += p 		#iterates through all probs and adds each value to total
if not math.isclose(total, 1.0): #checks if sum of all probs is very close to 1.0
    sys.exit('error: probs must sum to 1.0') #if does not sum up to 1.0, program is exited

h = 0 								#initializes variable to store entropy
for p in probs: 					#interate through each probability
    h -= p * math.log2(p) 			#entropy formula

print(f'{h:.4f}') 					#formats h to 4 decimal places before printing