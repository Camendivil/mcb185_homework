# 20demo.py by Carolina_Mendivil

t =1, 2							#tuple
print(t)
print (type(t))

person= 'Steve' , 21, 57891.50 	#name, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
'''
# practice midpoint code
print(midpoint(1, 2, 3, 4)) #Line 1 calls the midpoint() function and the output is directly sent to the print() function.
m = midpoint(1, 2, 3, 4)	#Line 2 assigns the variable m to the return value of the midpoint() function. m is a tuple. 
mx, my = midpoint(1, 2, 3, 4) #Line 3 "unpacks the tuple". That is, the caller knows that the function returns two values, so the caller provides 2 separate named variables, mx, and my
print(mx, my)				#Line 4 prints the separate values.
print(m[0], m[1])
'''


#breaking a loop

i = 0
while True:
	i = i +1
	print('hey' , i)
	if i ==3: break 


#for i in range()

for i in range(1, 10, 3):
	print(i)
'''
the range: initial value (1)
end-before limit (10)
increment (3)

use this instead: 
for i in range(5): print(i)

backwards:
for i in range(4, -1, -1): print(i)
'''

#containers are tuples

basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
	
#Nesting

for i in range(7):
	if i % 2 ==0: print(i, 'is even')
	else: 		print(i, 'is odd')
	
	

#Random Numbers
import random

for i in range(5):
	print(random.random())
	
# This generates a random number between two inclusive end points. 
#For example, the following code simulates rolling a 6-sided die 3 times.

for i in range(3):
    print(random.randint(1, 6))


random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

'''
Compound Assignment
operator	purpose				example
+=			increment			a += 1
-=			decrement			a -= 1
*=			multiply & assign	a*= 2
'''
