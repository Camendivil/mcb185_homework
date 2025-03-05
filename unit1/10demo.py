# 10demo.py by Carolina_mendivil
"""
Its currently 12
PM 
"""

print('hello again') # greeting
import math

#Basic math operations
print(1.5e-2)   	# 0.015
print(1 + 1) 		# 2 addition
print(1 - 1)		# 0 subtraction
print(2 * 2)		# 4 multiplication 
print(1 / 2)		# 0.5 division
print(2 ** 3)		# 8 exponentiation
print(5 // 2)		# 2 integer divide
print(5 % 2)		# 1 remainder
print(5 * (2 + 1))	# 15 precedence

#Using math functions
print(abs(-5))		# absolute value of 5

print(pow(x, y))	# x to the power of y
print(pow(2,3))		#2^3 = 8

print(round (x, ndigits=3)) 	# round off x to 3 digits
print(round(3.14159, 3))		#rounding = 3.142

#Using math library functions
print(math.ceil(x)) 			#round x up
print(math.ceil(3.1))			#round up to 4
print(math.floor(3.9)) 			#round down to 3
print(math.log(2))				# natural log = ~0.693
print(math.sqrt(2))				#square root = 1.41

#Math constants
print(math.pi)			#3.14159...
print(math.e)			#2.71828...
print(math.inf)			#infinity
print(math.nan)			#not a number
print(1/0) 				#divide by zero error

#The = sign is used to assign numbers (and other types of values)
The code below computes the hypotenuse c given sides a and b.
a=3							#side of the triangle
b=4							#side of the triangle
c = math.sqrt(a**2 + b**2)	# hypotenuse
print(c)


#Functions
def pythagoras(a, b): 				#creating a function
	return math.sqrt(a**2 + b**2))	#calculating the hypotenuse
print (pythagoras(3,4)) 			#output is 5.0

# UNIT 1 practice functions
# area of a circle
print('area of a circle')
def circle_area(r): 				#creating function
	return math.pi * (r**2) 		#calculating the radius of a circle
print(circle_area(3))				#output = 28.27

#area of a triangle
print ('area of a triangle')
def triangle_area (w,h): 
	return rectangle_area(w,h) / 2 # calulating area of a triangle
print(triangle_area(2,4)) 			#output= 4

#F to C conversion
C= (F - 32) * 5/9

print( 'farenheit to celsius')
def ftoc_conversion (f):
	return ((ftoc_conversion(70)) 	#output= 21.11

#MPH to KPH conversion
# MPH * 1.60934 = KPH

print('mph to kph')
def mphtokph(m):
	return (m*1.60934)
print(mphtokph(65)) 				#output= 104.6


#Compute DNA Concentration from an OD 260
C+ A260 * dilution factor * conversion factor 
A260= Absorbance @ 260 nm
Dilution factor = 1, if undiluted
Conversion factor= 50 mu-m/mL per OD260

print('dna conc from od 260 (WIP)')	
#WIP def dna_conc(m):

#Compute the arithmetic mean of 3 numbers
mean = (X1 + X2 + X3)/3

print ('mean')
def mean3(a,b,c):
	return ((a+b+c)/3)
print (mean3(5,10,15)) 				#output = 10

# Geometric Mean (cubed root of a x b x c)
print ('geometric mean')
def geo_mean3(a,b,c):
	return ((a*b*c) ** (1/3))
print (geo_mean3(4,5,6))			 #output = 4.93

# Harmonic mean of 3 numbers
print ('harmonic mean')
def harm_mean3(a,b,c):
	n = 3
	sum = (1/a) + (1/b) + (1/c)
	return n/sum
print (harm_mean3(5,10,15)) 		#output = 8.18

#Distance between two points
d = sqrt (X2-X1)^2 + (Y2-Y1)^2

print ('distance between two points')
def distance(X1,Y1,X2,Y2):
	diffx = X2-X1
	diffy = Y2-Y1
	return math.sqrt(((diffx)**2)+((diffy)**2))
print (distance(1,5,5,10))			 #output = 6.40

#Conditionals
# if statements
a = 2
b = 2
if a == b:
	print ('a equals b')
	print (a, b)

== #equality if a==b
!= #inequality if a !=b
<  #less tha   if a<b
>  #greater than if a>b
<= #less or equal 
>= #greater or equal

def is_even(x):
	if x % 2 == 0: return True
	return False
	
#Boolean
# c = a == b
c = 3 == 2
print(c)
print(type(c))

#if-elif-else
a = 5
b = 10
if a < b:
	print ('a < b')
elif a > b:
	print ('a > b')
else:
	print('a == b')

a = 7
b = 2
if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

a = 4
b = 4
if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')


print(is_even(2))
print(is_even(3))

#Chaining
a = 2
b = 3
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print (True)

#Floating point numbers
a = 0.3
b = 0.1 * 3

if a < b:
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b') # This does not print as expected

print(abs(a - b)) #5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

#String Comparison
s1 = 'A' # = 65
s2 = 'B' # = 66
s3 = 'a' # = 97
if s1 < s2: print ('A < B')
if s2 < s3: print ('B < a')

#None Type
def silly(m, x, b):
	y = m * x + b # y is computed but not returned
print(silly(2,3,4))

#More practice
print('determining if a number is an integer')
def is_integer(n):
	if n % 1== 0: return True 	#If between 0 and 1, it's a valid probability
	return False
print(is_integer(3))

print('determining if number is of valid probability')
def is_validprob(p):
	if p<1 and p>0: return True 	#If between 0 and 1, it is a valid probability
	return False
print(is_validprob(0.98))

print('molecular weight of DNA letter')
def molecularweight(nt):
	if nt == 'A': return 331.2 		#Must be enclosed in '' because they are strings
	elif nt == 'C': return 307.2
	elif nt == 'G': return: 347.2
	elif nt == 'T': return 322.2
	else: return None
print(molecularweight('B'))

print('DNA complement')
def dnacomplement(nt):
	if nt == 'A': return 'T'
	if nt == 'C': return 'G'
	if nt == 'G': return 'C'
	if nt == 'T': return 'A'
print(dnacomplement('A'))


#Even More Practice
print('max of three')
def max3(x, y, z):
	if x >= y and x>= z: return x
	elif y >= x and y >= z: return y
	else: return z
print(max3(12, 15, 17))

print('sensitvity, specificity, f1')
"""
true postives = tp (sick identified as sick)
false positives = fp (healthy identfied as sick)
true negatives = tn (healthy identified as healthy)
false negatives = fn (sick identified as healthy)
"""
def sensitivity(tp, fn):
	return tp / (tp + fn)
print(sensitivity(50, 20))

def specifity(tn, fp):
	return tn / (tn + fp)
print(specifity(30, 5))

def f1_score(tp, fp, fn):
	return (2*tp) / ((2*tp)+fp+fn)
print (f1_score(50, 10, 10))

print('shannon entropy')
def shannonentropy(a,c,t,g):
	total = a + c + t + g
	if total == 0: return 0
	entropy = 0
	if a > 0:
		pa = a / total
		entropy -= pa * math.log2(pa)
	if c > 0:
		pc = c / total
		entropy -= pc * math.log2(pc)
	if g > 0:
		pg = g / total
		entropy -= pg * math.log2(pg)
	if t > 0:
		pt = t / total
		entropy -= pt * math.log2(pt)
	
	return entropy
print(shannonentropy(10,10,10,10))




