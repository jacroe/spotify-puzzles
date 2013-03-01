#TITLE:      Reversed Binary Numbers
#AUTHOR:     Jacob Roeland
#DATE:       Mar 1, 2013
#USE:        echo 13 | python caesar.py
#OUTPUT:     11
#PUZZLE      https://www.spotify.com/uk/jobs/tech/reversed-binary/

def reverse(number):
	from math import pow

	x,bigNumber,binary,firstOne = 1,number,"",False

	while(x < bigNumber): x = x*2
	while(bigNumber != 0):
		if bigNumber-x>=0:
			binary = binary+"1"
			bigNumber = bigNumber-x
			firstOne = True
		elif firstOne: binary = binary+"0"
		x = x/2
	while(x != 0): 
		binary = binary+"0"
		x = x/2

	revBigNumber = 0

	for i in range(0, len(binary)):
		revBigNumber += int(binary[i])*pow(2,i)

	return str(int(revBigNumber))

import sys
data = sys.stdin.readlines()
print reverse(int(data[0]))
