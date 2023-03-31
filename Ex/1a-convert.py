#-*- coding: utf-8-*-from sys import argv
restart = "a";
while restart != "Q":
	print "Convertisseur de Celsius / Fahrenheit"
	nombre = False
	while nombre == False:
		try:
			temperature = int(raw_input("Entrez une temperature : "))
			nombre = True
		except ValueError: print "Avec un NOMBRE ça ira mieux"
	
	sens = "a"
	while sens != "C" and sens != "F":
		sens = raw_input("Convertir vers (C)elsius ou (F)ahrenheit ? ")
		
	if sens == "C":
		print "Resultat = %f"% (float(5)/9*(float(temperature)-32))
	elif sens == "F":
		print "Resultat = %f"% (float(9)/5*(float(temperature)+32))
	else:
		print "J'avais dit C ou F, boulet !"
	restart = raw_input("Pressez Q pour quitter : ")