#-*- coding: utf-8-*-
print "Convertisseur de Celsius / Fahrenheit"
try:
    temperature = int(raw_input("Entrez une temperature : "))
except ValueError: print "Avec un NOMBRE ça ira mieux"

def celsius(x) : return float(5)/9*(float(temperature)-32)
def fahrenheit(x) : return float(9)/5*(float(temperature)+32)
sens = raw_input("Convertir vers (C)elsius ou (F)ahrenheit ? ")

pauvreVadi = {'C' : celsius(temperature),
              'F' : fahrenheit(temperature)}

print "Resultat = %f"% pauvreVadi[sens]
