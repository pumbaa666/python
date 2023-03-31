#!/usr/bin/python
# -*- coding: latin-1 -*-

from random import randint

to_guess = randint(0,100)

while True:
	try:
		guessed = float(raw_input("Entrez un nombre (entre 0 et 100): "))
		break
	except ValueError:
		print "Vous devez entrer un nombre!"

if guessed == to_guess:
	print "Gagné!"
else:
	print "Perdu!"