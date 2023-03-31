#-*- coding: utf-8-*-
print "Convertisseur de Celsius / Fahrenheit"
try:
    temperature = int(raw_input("Entrez une temperature : "))
except ValueError: print "Avec un NOMBRE ca ira mieux"

try:
    print {
        'C' : lambda x: 5.0/9.0*x-32),
        'F' : lambda x: 9.0/5.0*x+32)
        }[raw_input("Convertir vers (C)elsius ou (F)ahrenheit ? ")](temperature)
except KeyError : print "erreur"