#!/usr/bin/python
# -*- coding: latin-1 -*-


""" Convertisseur de temp�rature - Deuxi�me version """

import sys

usage = """
%s <temp�rature> <sens>

Convertit <temp�rature> en fonction de <sens>:
	<sens> = 'C' : de Fahrenheit � Celsius
	<sens> = 'F' : de Celsius � Fahrenheit
""" % sys.argv[0]

def CtoF(t):
	return (t-32)*5.0/9
	
def FtoC(t):
	return (t*9.0/5)+32

try:
	temp = float(sys.argv[1])
	sens = sys.argv[2]
	if sens not in ['C','F']: raise Exception
except:
	print usage
	sys.exit(1)

if sens == "C": result = FtoC(temp)
if sens == "F": result = CtoF(temp)

print "R�sultat: %.2f" % result

