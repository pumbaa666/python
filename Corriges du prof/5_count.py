#!/usr/bin/python
# -*- coding: latin-1 -*-

import locale
locale.setlocale(locale.LC_ALL,'')

import sys

usage = """
usage: count.py <filename>
"""
try:
	filename = sys.argv[1]
except:
	print usage
	sys.exit(1)

try:	
	f = file(filename,'r')
except IOError, e:
	print "Erreur en ouvrant le fichier:"
	print e.strerror
	sys.exit(1)

words = f.read().split()
f.close()

# Se débarrasse des carcatères non-alphabétiques
# (ponctuation, chiiffres, ...)
# Attention: peut donner des choses bizarres avec des chaînes telles
# que "l'exemple" (donne "lexemple"...)
words = [filter(lambda x: x.isalpha(), word) for word in words]

# On a peut-être des mots vides dans words...
words = filter(lambda x:x, words)

counted = {}

for word in words:
	try:
		counted[word] += 1
	except KeyError:
		counted[word] = 1

sorted_words = counted.keys()
# Trie sans tenir compte de la casse
sorted_words.sort(key=str.lower)

for w in sorted_words:
	print "%5d: %s" % (counted[w],w)