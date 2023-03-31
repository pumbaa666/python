# -*- coding: UTF-8 -*-
from livewires import games, colour
from Solution import Solution
from Population import Population
import pygame
from pygame.locals import KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_RETURN, K_ESCAPE, KEYUP, QUIT
import sys
from data import *
from myGlobal import *
from random import shuffle, randrange

#~ init ~#
pygame.init() 
window = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Voyageur de commerce')
screen = pygame.display.get_surface() 

#~ messages d'avertissements éventuels ~#
if testerParametre():
    ecrire(screen, "ATTENTION, les parametres donnes", rouge, 50, 50)
    ecrire(screen, "dans le fichier data.py semblent incorrects !", rouge, 50, 70)
    ecrire(screen, "Je ne peux pas garantir le fonctionnement du programme", rouge, 50, 100)
    ecrire(screen, "CONTINUER         QUITTER", rouge, 50, 200, 30)
    
    x1 = 40
    x2 = 200
    y = 190
    w = 145
    h = 45
    drawBouton(screen, "Continuer", x1, y, w, h, rouge)
    drawBouton(screen, "Quitter", x2, y, w, h, rouge)
    pygame.display.flip()
    collecting = True
    event = pygame.event.wait()
    
    while collecting:
        for events in pygame.event.get():
            if events.type == MOUSEBUTTONDOWN:
                if event.type == QUIT:
                    sys.exit(0)
                elif pygame.mouse.get_pos()[0] > x1  and pygame.mouse.get_pos()[0] < x1+w and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y+h:
                    collecting = False
                elif  pygame.mouse.get_pos()[0] > x2  and pygame.mouse.get_pos()[0] < x2+w and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y+h:
                    sys.exit(0)


screen.fill(0)
ecrire(screen, "Placez vos villes a la souris", vert, 10, 10, 26)
x = screen_w-200
y = screen_h-50
w = 145
h = 45
drawBouton(screen, "Go", x, y, w, h)
pygame.display.flip()

#~ collect des villes ~#
solution = Solution()
collecting = True
nombreDeVille = 0
while collecting:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN and event.key == K_RETURN:
            collecting = False
        elif event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > x  and pygame.mouse.get_pos()[0] < x+w and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y+h:
                collecting = False
            else:
                newVille = pygame.mouse.get_pos()
                solution.addVille(newVille)
                drawPoint(screen, solution.getTrajet())
                nombreDeVille += 1

#~ Pas assez de villes ~#
if nombreDeVille < 2:
    ecrire(screen, "Entrez au moins 2 ville svp...", rouge, 50, 50, 30)

#~ 2 ou 3 villes, il n'existe qu'un seul chemin ~#
elif nombreDeVille < 4:
    population = Population(screen)
    population.addSoluce(solution.getTrajet())
    population.drawLast()    
    ecrire(screen, "Le meilleur chemin !", vert, 10, 10, 30)

#~ La partie interessante ~#
else:
    #~ init ~#
    population = Population(screen)
    bestSoluces = Population(screen)
    
    population.addSoluce(solution.getTrajet())
    bestSoluces.addSoluce(solution.getTrajet())
    
    population.drawLast()
    heure = pygame.time.Clock()
    heure.tick()
    
    #~ mutations du trajet de base ~#
    listeIndiceRandom = range(0, solution.getSizeTrajet())
    for i in range(0, taillePopDepart-1):
        shuffle(listeIndiceRandom)
        soluce = Solution()
        for j in range(0, len(listeIndiceRandom)):
            soluce.addVille(solution.getVille(listeIndiceRandom[j]))
        population.addSoluce(soluce.getTrajet())
    
    iterationSansChangement = 0
    bestDistanceInt = bestSoluces.getLastSoluce()
    count = 0
    text_gen = ""
    text_gen_sans = ""
    quitter = False
    
    #~ boucle principale ~#
    while iterationSansChangement < nbIterationSansChangementMax and quitter == False:
        #~ récolte des éventuels evenements (pour le Stop) ~#
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > screen_w-200  and pygame.mouse.get_pos()[0] < screen_w-200+190 and pygame.mouse.get_pos()[1] > screen_h-50 and pygame.mouse.get_pos()[1] < screen_h-50+40:
                    quitter = True

        #~ Traitement de la population ~#
        max = len(population.listeSolution)
        for i in range(0 , taillePopDepart):
            #~ séléction aléatoire de 2 villes ~#
            num1 = randrange(0, max)
            num2 = num1
            while num2 == num1:
                num2 = randrange(0, max)
    
            #~ crossOver ~#
            soluce = Solution()
            soluce.crossOver(population.getSoluce(num1), population.getSoluce(num2))
            population.addSoluce(soluce.getTrajet())
            
        #~ Mutation au hasard ~#
        for i in range (0, nbMutation): 
            soluceATrier = randrange(0, max)
            soluce = Solution()
            soluce.addTrajet(population.getSoluce(soluceATrier))
            soluce.muter()
        
        population.trier()
        
        #~ On récupère la meilleure soluce de la liste en cours ~#
        soluceATester = Solution()
        soluceATester.addTrajet(population.getSoluce(0))
        
        iterationSansChangement += 1
        bestSoluces.iterer()
        if(soluceATester.calculerDistanceTotale() < bestDistanceInt):
            iterationSansChangement = 0
            bestDistanceInt = soluceATester.calculerDistanceTotale()
            bestSoluces.addSoluce(soluceATester.getTrajet())
            bestSoluces.drawLast()
        
        #~ Un peu de bla-bla rassurant ~#
        effacer(screen, text_gen, 10,screen_h-40, noir)
        text_gen = "Generation n "+str(count)
        ecrire(screen,text_gen,blanc,10,screen_h-40)        
    
        effacer(screen,text_gen_sans,10,screen_h-20, noir)
        text_gen_sans = "Generation sans changements "+str(iterationSansChangement)
        ecrire(screen,text_gen_sans,blanc,10,screen_h-20)        
        
        population.viderPartiellement()
        count += 1
        
    #~ fin ~#
    if quitter == True:
        ecrire(screen, "Interrompu par l'utilisateur", vert, 10, 10, 30)
    else:
        ecrire(screen, "Un bon chemin, pas forcement le meilleur !", vert, 10, 10, 30)
    heure.tick()
    text = str(int(heure.get_time()/100.0)/10.0)+" secondes"
    ecrire(screen, text, blanc, 250, screen_h-40)
    
#~ getch ~#
x = screen_w-200
y = screen_h-50
w = 190
h = 40
drawBouton(screen, "Quitter", x, y, w, h)
while True:
    for events in pygame.event.get():
        if events.type == MOUSEBUTTONDOWN:
            if event.type == QUIT:
                sys.exit(0)
            elif  pygame.mouse.get_pos()[0] > x  and pygame.mouse.get_pos()[0] < x+w and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y+h:
                sys.exit(0)
