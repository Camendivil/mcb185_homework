#33birthday.py by Carolina_Mendivil

'''
In this program, you must use a list for the birthdays. 
For example, if there are 23 people in the classroom, you will list.append() 23 times
(unless you're extra-clever and figure out how to make a short-circuit).
'''


import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared=0
for i in range(trials):
	birthday_list_of_23 = []
	
	for peep in range(people):
		bday = random.randint(1,days) 
		if bday in birthday_list_of_23:
			shared = shared + 1
								#print(bday, 'is duplicate birthday')
			break
		birthday_list_of_23.append(bday)

print(shared/trials, 'for shared/trials')


'''
use this in terminal:
33birthday.py 10000 365 23
 '''