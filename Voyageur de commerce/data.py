# -*- coding: UTF-8 -*-
screen_w = 800
screen_h = 600

city_radius = 3 #~ taille des villes (points)
rouge = [250,10,10]
blanc = [255,255,255]
noir = [0,0,0]
bleu = [10,10,255]
vert = [50, 250, 50]

taillePopDepart = 50 #~ Bien entre 20 et 50. Au dessus devient vraiment tres lent
propSurvivant = 0.3 #~ Proportion du tableau a rester en vie apres les crossover. Représente un pourcentage --> interval = [0.1 , 1]
nbIterationSansChangementMax = 100 #~ A moduler selon la taillePopDepart
nbMutation = 50 #~ Nombre de mutation a effectuer avant de proceder aux crossover