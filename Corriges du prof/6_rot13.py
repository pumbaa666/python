import string
import sys

MIN = string.ascii_letters[:26]
MAJ = string.ascii_letters[26:]
	
def rot13(c):
	try:
		i = MAJ.index(c)
		return MAJ[i-13]
	except ValueError: pass
	
	try:
		i = MIN.index(c)
		return MIN[i-13]
	except ValueError: pass
		
	return c
		

while True:
	s = raw_input(' -> ')
	if s == "": sys.exit(0)
	s = "".join([rot13(c) for c in s])
	print s