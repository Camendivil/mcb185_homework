#32stats.py by Carolina_mendivil

'''
Write a program that reports descriptive stats for numbers on the command line. 
Your program should report the following values:

The number of values
The minimum and maximum values
The mean and standard deviation
The median value
'''

import math
import sys

numbers = [1, 2, 3, 4]  # sets a list

# Read numbers from command-line arguments
for arg in sys.argv[1:]:
    f = float(arg) 
    numbers.append(f)  

# Find min and max
min_val = numbers[0]
max_val = numbers[0]
for val in numbers[1:]:
    if val < min_val:
        min_val = val
    if val > max_val:
        max_val = val
print('min:', min_val)
print('max:', max_val)

# Compute mean
total = sum(numbers)  
mean = total / len(numbers)
print('mean:', mean)

# Compute standard deviation
variance = sum((val - mean) ** 2 for val in numbers) / (len(numbers) - 1)
stddev = math.sqrt(variance)
print('sd:', stddev)

# Compute median
numbers.sort()  	#sort numbers in ascending order
n = len(numbers)
if n % 2 == 1:  	#odd length
    median = numbers[n // 2]
else:  				#even length
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
print('median:', median)

# Compute N50
numbers.sort(reverse=True)  #sort in descending order
cumulative_sum = 0
half = sum(numbers) / 2  	
n50 = 0

for num in numbers:
    cumulative_sum += num
    if cumulative_sum >= half:
        n50 = num
        break

print('N50:', n50)

