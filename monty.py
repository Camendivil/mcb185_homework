#Monty Pi-thon by carolina_mendivil
'''
Write a program that estimates pi using Monte Carlo methods. 
Generate random values for x and y from 0 to 1. 
Calculate the distance to the origin. If the distance is less than 1, 
the point is inside the circle. 
The ratio of points that fall inside compared to the total is pi/4. 
Output each iteration and watch as the ratio gets closer to pi. 
Use an endless while loop in your program and stop it with ^C.
'''

import random
inside = 0
total = 0

while True:
	total += 1
	x = random.random()
	y = random.random()
	
	distance = x**2 + y**2
	if distance <= 1:
		inside += 1
		piestimate = 4 * (inside/total)
	print(piestimate)
	