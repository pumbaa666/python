#!/usr/bin/python
# -*- coding: latin-1 -*-


""" Convertisseur de temp�rature - Premi�re version """

def CtoF(t):
	""" Convertit la temp�rature t des degr�s Celsius aux degr�s Fahrenheit"""
	return (t-32)*5.0/9
	
def FtoC(t):
	""" Convertit la temp�rature t des degr�s Fahrenheit aux degr�s Celsius"""
	return (t*9.0/5)+32

print "Convertisseur de temp�rature\n"

temp = None

# Lire un float de mani�re s�re � la console...
while not temp:
	try:
		temp = float(raw_input("Entrez une temp�rature: "))
	except ValueError:
		print "Vous devez entrer un nombre!"

sens = ""

while not (sens=='C' or sens=='F'):
	sens = raw_input("Convertir vers des degr�s (C)elsius ou (F)ahrenheit? ")

if sens == "C": result = FtoC(temp)
if sens == "F": result = CtoF(temp)

print "R�sultat: %.2f" % result

