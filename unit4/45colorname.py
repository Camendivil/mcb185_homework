#45colorname.py by Carolina_mendivil

'''
Write a program that provides the closest official color name given 
some red, green, and blue values. For example, given the color 
values 200, 0, 50, your program should report a shade of red. 
You will find color definitions in the colors_basic.tsv 
and colors_extended.tsv in MCB185/data.
'''

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2]) #red
G = int(sys.argv[3]) #green
B = int(sys.argv[4]) #blue
minimum = 245
min_color = 'none'

#distance
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

with open(colorfile, 'rt') as fp:
	for line in fp:
		colorprofile = line.split()	
		colorvalues = colorprofile[2].split(',')		
		diff1 = abs(int(colorvalues[0]) - R)
		diff2 = abs(int(colorvalues[1]) - G)
		diff3 = abs(int(colorvalues[2]) - B)
		sum = diff1 + diff2 + diff3
		if sum < minimum: 
			minimum = sum
			min_color = colorprofile[0]
	print(min_color)
	
	
'''
command:
python3 45colorname.py ~/Code/MCB185/data/colors_extended.tsv 200 0 50
= crimson

command: 
python3 45colorname.py ~/Code/MCB185/data/colors_extended.tsv 250 0 45
= red

command:
python3 45colorname.py ~/Code/MCB185/data/colors_extended.tsv 100 20 46
= brown
'''