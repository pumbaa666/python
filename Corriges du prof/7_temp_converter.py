#!/usr/bin/python
# -*- coding: latin-1 -*-


""" Convertisseur de temp�rature - sans conditionnelle """

convertisseur = {
	'F' : lambda t: (t-32)*5.0/9,
	'C' : lambda t: (t*9.0/5)+32
}

print "Convertisseur de temp�rature\n"

temp = None

while not temp:
	try:
		temp = float(raw_input("Entrez une temp�rature: "))
	except ValueError:
		print "Vous devez entrer un nombre!"

while 1:
	sens = raw_input("Convertir vers des degr�s (C)elsius ou (F)ahrenheit? ")
	try:
		result = convertisseur[sens](temp)
		break
	except KeyError:
		print 'Entrez "C" ou "F" uniquement!'

print "R�sultat: %.2f" % result

