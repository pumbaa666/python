# -*- coding: UTF-8 -*-
from Solution import Solution
import pygame
from data import *
from time import sleep
from myGlobal import *

class Population:
    def __init__(self, screen):
        self.listeSolution = []
        self.nbIterationSansModif = 0
        self.nbAmelioration = -1
        self.nbGeneration = 0
        self.screen = screen
    
    def afficher(self):
        for i in range(0, len(self.listeSolution)):
            print str(i)+" : "+str(self.listeSolution[i])
    
    def trier(self):
        domaine = range(0, len(self.listeSolution))
        domaine.reverse()
        for i in domaine:
            for j in range(0, i):
                soluce = Solution()
                soluce.addTrajet(self.listeSolution[j])
                distance = soluce.calculerDistanceTotale()
                
                soluce2 = Solution()
                soluce2.addTrajet(self.listeSolution[j+1])
                distance2 = soluce2.calculerDistanceTotale()
                if(distance > distance2):
                    temp = self.listeSolution[j+1]
                    self.listeSolution[j+1] = self.listeSolution[j]
                    self.listeSolution[j] = temp
   
    def addSoluce(self, soluce):
        self.listeSolution.append(soluce)
    
    def getSoluce(self, indice):
        return self.listeSolution[indice]
    
    def getLastSoluce(self):
        return self.listeSolution[-1]
    
    def viderPartiellement(self):
        numeroFin = int(2 * taillePopDepart * propSurvivant)
        self.listeSolution = self.listeSolution[0:numeroFin]
    
    def drawChemin(self, indice):
        self.screen.fill(0)
        soluce = Solution()
        soluce.addTrajet(self.listeSolution[-1])
        self.nbAmelioration += 1
        newDistance = soluce.calculerDistanceTotale()
        text = "Amelioration n "+str(int(self.nbAmelioration)) + " / Gen n "+str(int(self.nbGeneration))
        ecrire(self.screen, text, blanc, 10, screen_h-60)

        
        text = "Best distance = "+str(int(newDistance))
        ecrire(self.screen, text, blanc, 250, screen_h-60)
        
        pygame.draw.lines(self.screen,bleu,True,self.getSoluce(indice))
        drawPoint(self.screen, self.listeSolution[-1])
        drawBouton(self.screen, "Stop", screen_w-200, screen_h-50, 190, 40)
        pygame.display.flip()

    def drawLast(self):
        self.drawChemin(len(self.listeSolution)-1)
    
    def iterer(self):
        self.nbGeneration +=1