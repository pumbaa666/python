#!/usr/bin/python
# -*- coding: latin-1 -*-


""" Convertisseur de température - Première version """

def CtoF(t):
	""" Convertit la température t des degrés Celsius aux degrés Fahrenheit"""
	return (t-32)*5.0/9
	
def FtoC(t):
	""" Convertit la température t des degrés Fahrenheit aux degrés Celsius"""
	return (t*9.0/5)+32

print "Convertisseur de température\n"

temp = None

# Lire un float de manière sûre à la console...
while not temp:
	try:
		temp = float(raw_input("Entrez une température: "))
	except ValueError:
		print "Vous devez entrer un nombre!"

sens = ""

while not (sens=='C' or sens=='F'):
	sens = raw_input("Convertir vers des degrés (C)elsius ou (F)ahrenheit? ")

if sens == "C": result = FtoC(temp)
if sens == "F": result = CtoF(temp)

print "Résultat: %.2f" % result

