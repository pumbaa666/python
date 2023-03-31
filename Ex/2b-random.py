#!/usr/bin/python
#-*- coding: utf-8-*-from random import randint
to_guess = randint(0,100)
guessed = raw_input("Entrez un chiffre entre 1 et 100 pour gagner :")
if int(guessed) == to_guess:
	print "Gagné!"
else:
	print "Perdu!"