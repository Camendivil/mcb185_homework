# 25deathsaves.py by Carolina_Mendivil

'''
Death saves are a little different than normal saving throws. 
If your health drops to 0 or below, you are unconscious and may die. 
Each time it is your turn, roll a d20 to determine if you get closer to life 
or fall deeper into death. If the number is less than 10, you record a "failure". 
If the number is 10 or greater, you record a "success". 
If you collect 3 failures, you "die". If you collect 3 successes, you are 
"stable" but unconscious. If you are unlucky and roll a 1, it counts as 2 failures. 
If you're lucky and roll a 20, you gain 1 health and have "revived". 
Write a program that simulates death saves. What is the probability one dies,
stabilizes, or revives?
'''


import random

stable = 0
rounds = 100 # replaceable
revivals = 0
death = 0

for i in range(rounds): # outside for loop
    successes = 0 # initialization
    failures = 0
    for turn in range(6): # run 6 turns
        roll = random.randint(1,20)

        if roll == 1: # rolling a 1 = 2 fails
            failures += 2 # means failures = failures + 2
        elif roll == 20: # rolling a 20 means revived
            revivals += 1
            break
        elif roll >= 10: # rolling > 10 = 1 success
            successes += 1
        else: # if roll < 10
            failures += 1 # means failures = failures + 1

        if successes == 3: # if you get three successes you are stable
            stable += 1
            break
        elif failures >= 3:
            death += 1
            break

print('Probability of death', death/rounds)
print('Probability of being stabilized', stable/rounds)
print('Probability of being revived', revivals/rounds)