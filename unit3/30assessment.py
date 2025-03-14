import math


def isprobdist(prob):
	for p in prob:
		if p < 0 or p > 1: return False
		
	total = 0
	for p in prob:
		total += p
	return math.isclose(total, 1.0)
	
	
p1= [0.2, 0.3, 0.5]
p2= [0.3, 0.3, 0.3, 0.4]
print(isprobdist(p1))
print(isprobdist(p2))