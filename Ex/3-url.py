#-*- coding: utf-8-*-
from sys import argv
from urllib2 import urlopen

if "http://" not in argv[1]:
	print "format inconu"
else:
	try:
		url = urlopen(argv[1])
	except: print "impossible d'accéder à l'URL"
	else: print "URL ok"
	