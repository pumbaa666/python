#-*- coding: utf-8-*-
import sys

usage = """
usage: compter_mot_fichier.py <filename>
"""

try:
    filename = sys.argv[1]
except:
    print usage
    sys.exit(1)
    
try:
    f = open(filename, 'r')
except IOError, e:
    print "Erreur en ouvrant le fichier:"
    print e.strerror
    sys.exit(1)
    
ch = " "
mot = ""
dico = {}
list_except = [" ", "", "\n", "\t", "\r", ",", ";", ":"]
while ch != "":
    ch = f.read(1)
    mot = ch
    #~ if not ch in list_except:
        #~ mot += ch
    #~ elif(mot != ""):
    if dico.has_key(mot):
        dico[mot] += 1
    else:
        dico[mot] = 1
    mot = ""

for k in dico.keys():
    print k, dico[k]
f.close()