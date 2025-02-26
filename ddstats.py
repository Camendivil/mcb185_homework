# D&D stats by carolina_mendivil

'''
In Dungeons and Dragons, each character is described by 6 statistics 
(strength, intelligence, wisdom, dexterity, constitution, charisma). 
In the old days, each stat was decided by summing up the values on 
3 six-sided dice (3D6). Each stat therefore has a range of 3-18 and an 
average of 10.5. Over the years, the official rules have changed and 
many players have added their own house rules. Write a program that determines 
the average stat value using the various rules below.

3D6: roll 3 six-sided dice
3D6r1: roll 3 six-sided dice, but re-roll any 1s
3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
4D6d1: roll 4 six-sided dice, dropping the lowest die roll
'''

import random

#3D6: roll 3 six-sided dice
def roll3d6():
	total = 0 
	for i in range(3):
		n = random.randint(1, 6)
		total += n
	return total
print(roll3d6())



# 3D6r1: roll 3 six-sided dice, but re-roll any 1s
def roll3d6r1():
    total = 0
    for i in range(3):
        n = random.randint(1, 6)
        if n == 1:
            n = random.randint(1, 6)
        total += n
    return total
print(roll3d6r1())



# 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
def roll3d6x2():
    total = 0
    for i in range(3):
        a = random.randint(1,6)
        b = random.randint(1,6)
        if a < b: a = b
        total += a
    return total
print(roll3d6())



# 4D6d1: roll 4 six-sided dice, dropping the lowest die roll
def lowestdie(a,b,c,d):
    if a <= b and a <= c and a <= d: return a
    if b <= c and b <=d: return b
    if c <=d: return c
    else: return d
def roll4d6d1():
    total = 0
    for i in range(3):
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        d = random.randint(1,6)
        total = a + b + c + d
        finaltotal = total - (lowestdie(a,b,c,d))
    return finaltotal
print (roll4d6d1())