#34birthday.py by Carolina_mendivil

'''
This is the same problem as above, but instead of making a list of birthdays (e.g. 23) 
make a list from the calendar (e.g. 365). In the previous program, you appended birthdays to a 
list. In this one, all possible days are already in a list, so assigning a birthday is: 
calendar[birthday] += 1.

Another way to think about this problem is to imagine you're throwing darts 
at a calendar. A shared birthday is when 2 darts hit the same day.
'''

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


shared = 0

for i in range(trials):
	calendar = [0]* days
	for j in range(people):
		bday = random.randint(0, days-1) #endpoints.
		calendar[bday] = calendar[bday] + 1
		if calendar[bday] >= 2:
			shared += 1
			break
			
print(shared/trials)