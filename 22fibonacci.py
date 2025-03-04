# 22fibonacci.py by Carolina_ Mendivil

'''
Write a program that finds all Pythagorean triples for triangles with sides 
a and b less than 100. For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2. 
Hint: all sides, including the hypotenuse, must be integers.
 A good way to test for an integer is like: if c % 1 == 0.
 '''
 
 
a = 0 # set initial vals
b = 1
print(a,b) 
for i in range(4): 
    a += b 
    b = a + b
    print(a,b)