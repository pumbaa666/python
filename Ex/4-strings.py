#-*- coding: utf-8-*-from sys import argv
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR')

import sys.string

usage = """
usage: strings.py<filename>
"""

try:
    filename = sys.argv[1]
except:
    print usage
    sys.exit(1)
    
try:
    f = file(filenam, 'rb')
except IOError, e:
    print "Erreur en ouvrant le fichier:"
    print e.strerror
    sys.exit(1)
    
toprint = ""

while 1:
    ch = f.read(1)
    if ch == '':
        if len(toprint) > 3 : print toprint
        break
    if ch in string.printable:
        toprint += ch
    else:
        if len(toprint) > 3 : print toprint
        toprint = ""

f.close()