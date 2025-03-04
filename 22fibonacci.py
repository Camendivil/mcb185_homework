# 22fibonacci.py by Carolina_ Mendivil

'''
A classic programming interview question is to write a program that reports the 
first 10 numbers from the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. 
This is a tricky problem. You need to initialize and keep track of 2 previous values.
 '''
 
 
a = 0 # set initial vals
b = 1
print(a,b) 
for i in range(4): 
    a += b 
    b = a + b
    print(a,b)