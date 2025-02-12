# 11oligo.py by Carolina_Mendivil

# Write a function that returns the oligo melting temperature given the number of As, Cs, Gs, and Ts in the oligo. Use these two methods.

import math
def mT(a, t, g, c):
    length = a+t+g+c
    if length <= 13: return (a+t)*2 + (g+c)*4
    if length > 13: return 64.9 + 41*(g+c -16.4) / (a+t+g+c)

print(mT(10,20,30,40)) 		#output = 86.876
print(mT(1,2,3,4))			#output = 34
print(mT(0,1,0,0))			#output = 2
print(mT(0,0,0,0))			#output = 0
print(mT(5,7,3,4))			#output = 44.61
print(mT(-2,2,4,4))			#output = 32
print(mT(-1,20,30,40))		#output = 89.59
	