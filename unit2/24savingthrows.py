#24savingthrows.py by Carolina_Mendivil

'''
One of the core mechanics of D&D is the "saving throw". 
When certain events happen, you need to roll a d20 to figure out if you succeed or not.
For example, you are walking across a frozen lake and it begins to crack underfoot. 
If you make a saving throw, you step aside. If you fail, you fall in. 
Some saving throws are more difficult than others. 
If the ice is very thick, the "difficulty class" (DC) may be only 5. 
This means you only need to roll a 5 or higher to succeed. 
However, if the ice is thin and has a DC of 15, you will need a roll of 15 or 
higher to succeed. Certain events may give you "advantage" or "disadvantage". 
For example, if you have a rope tied around your waist and a friend is 
instructed to pull you aside if anything bad happens, you could have "advantage". 
This allows you to roll two d20s and take the larger value. 
You may also have disadvantage, for example another "friend" pushes you from behind,
causing you to stumble forward. In this case, you have "disadvantage" and must take 
the lower of two d20 rolls.
'''
'''
Write a program that simulates saving throws against DCs of 5, 10, and 15. 
Make a table showing the probability of success normally, with advantage, 
and with disadvantage.
'''

import random

trials = 100
def savingthrowsnormal(dc):
    success = 0
    for i in range(trials):
        roll1 = random.randint(1, 20)
        if roll1 >= dc:
            success += 1
    print(i, dc, roll1,'success', success/trials)
    print('probability of success is', success/trials)


trials = 100
def savingthrowsadvantage(dc):
    success = 0
    for i in range(trials):
        roll1 = random.randint(1, 20)
        roll2 = random.randint(1, 20)
        if roll1 < roll2:
            roll1 = roll2
        if roll1 >= dc:
            success += 1
    print(i,dc,roll1,roll2,'success', success/trials)
    print('probability of success with advantage is', success/trials)


trials = 100
def savingthrowsdisadvantage(dc):
    success = 0
    for i in range(trials):
        roll1 = random.randint(1,20)
        roll2 = random.randint(1,20)
        if roll1 > roll2:
            roll1 = roll2
        if roll1 >= dc:
            success += 1
    print(i,dc,roll1,roll2,'success', success/trials)
    print('probability of success with disadvantage is', success/trials)

# more
rolls = savingthrowsnormal, savingthrowsadvantage, savingthrowsdisadvantage
for dc in range(5, 16, 5):
    for roll in rolls:
        roll(dc)


for dc in range(5, 16, 5):
    adv = 0
    dis = 0
    norm = 0
    for i in range(trials):
        r1=random.randint(1,20)
        r2=random.randint(1,20)
        if r1 >= dc: norm += 1
        if r1 >= dc and r2 >= dc: dis += 1
        if r1 >= dc or r2 >= dc: adv +=1
    print(norm/trials, adv/trials, dis/trials) 