# -*- coding: UTF-8 -*-
from math import sqrt, pow
from random import randrange
from data import *
import pygame

class Solution:
    def __init__(self):
        self.trajet = []
        
    def addTrajet(self, trajet): # sorte de constructeur de copie, vu qu'on peut pas surcharger ¬_¬
        self.trajet = trajet
    
    def addVille(self, ville):
        self.trajet.append(ville)
    
    def getVille(self, indice):
        return self.trajet[indice]
    
    def getTrajet(self):
        return self.trajet
    
    def getSizeTrajet(self):
        return len(self.trajet)
        
    def muter(self):
        num1 = randrange(0, self.getSizeTrajet())
        num2 = num1
        while num2 == num1:
            num2 = randrange(0, self.getSizeTrajet())
        temp = self.trajet[num1]
        self.trajet[num1] = self.trajet[num2]
        self.trajet[num2] = temp
    
    def crossOver(self, list1, list2):
        fa = True
        fb = True
        
        i = randrange(0, len(list1))
        t= list1[i]
        pos = self.findPos(list1,t)
        pos2 = self.findPos(list2,t)
        self.trajet = []
        self.trajet.append(t)
        while fa == True or fb == True:
            x=pos-1%(len(list1)-1)
            y=pos2+1%(len(list2)-1)
            if fa:
                if self.appartientPasList(self.trajet,list1[x]):
                    self.trajet.insert(0,list1[x])
                else:
                    fa= False
                
            if fb:
                if self.appartientPasList(self.trajet,list2[y]):
                    self.trajet.append(list2[y])
                else:
                    fb= False
                    
        if len(self.trajet) < len(list1):
            for i in range(len(list1)):
                if self.appartientPasList(self.trajet,list1[i]):
                    self.trajet.append(list1[i])
    
    def findPos(self, list,element):
        for i in range(len(list)-1):
            if list[i] == element:
                return i
        return False
            
    def appartientPasList(self, list, element):
        for i in range(len(list)):
            if list[i] == element:
                return False
        return True        
        
    def calculerDistanceTotale(self):
        distance = 0
        for i in range(1, self.getSizeTrajet()):
            distance += sqrt((pow(self.trajet[i][0]-self.trajet[i-1][0],2))+pow((self.trajet[i][1]-self.trajet[i-1][1]),2))
        return distance