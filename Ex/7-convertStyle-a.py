#-*- coding: utf-8-*-
print "Convertisseur de Celsius / Fahrenheit"
try:
    temperature = int(raw_input("Entrez une temperature : "))
except ValueError: print "Avec un NOMBRE ça ira mieux"

sens = raw_input("Convertir vers (C)elsius ou (F)ahrenheit ? ")

pauvreVadi = {'C' : float(5)/9*(float(temperature)-32),
              'F' : float(9)/5*(float(temperature)+32)}

print "Resultat = %f"% pauvreVadi[sens]
