#-*- coding: utf-8-*-from sys import argv

if argv[2] == "C":
	print "Resultat = %f"% (float(5)/9*(float(int(argv[1]))-32))
elif argv[2] == "F":
	print "Resultat = %f"% (float(9)/5*(float(int(argv[1]))+32))
