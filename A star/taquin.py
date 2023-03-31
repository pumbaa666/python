#-*- coding: utf-8-*-from sys import argv
from random import randint
DROITE = 0
GAUCHE = 1
HAUT = 2
BAS = 3
class Taquin:
    def __init__(self, ligne, colone):
        self.ligne = ligne
        self.colone = colone
        
        self.ligneCaseLibre = ligne-1
        self.coloneCaseLibre = colone-1
        
        self.create()
        
        #~ self.OperateurHaut = 1
        #~ self.OperateurBas = 1
        #~ self.OperateurGauche = 1
        #~ self.OperateurDroite = 1
        self.distParc = 0
        self.whatOp()
        
    def incDistParc(self):
        self.distParc += 1
        
    def create(self):
        self.tab = self.ligne*[0]
        for i in range(0,self.ligne):
            self.tab[i] = self.colone*[0]
        num = 1
        for i in range(0,self.ligne):
            for j in range(0,self.colone):
                self.tab[i][j] = num
                num += 1
        self.tab[self.ligne-1][self.colone-1] = 0
                
    def afficher(self):
        for i in range(0,self.ligne):
            print self.tab[i]
                
    def isFinal(self):
        num = 1
        for i in range(0, self.ligne):
            for j in range(0, self.colone):
                if self.tab[i][j] == num or (i == self.ligne-1 and j == self.colone-1 and self.tab[i][j] == 0):
                    num += 1
                else:
                    return 0
        return 1
    
    def move(self, sens):
        if sens == HAUT and HAUT in self.whatOp():
            self.tab[self.ligneCaseLibre][self.coloneCaseLibre] = self.tab[self.ligneCaseLibre+1][self.coloneCaseLibre]
            self.tab[self.ligneCaseLibre+1][self.coloneCaseLibre] = 0
            self.ligneCaseLibre += 1
        elif sens == BAS and BAS in self.whatOp():
            self.tab[self.ligneCaseLibre][self.coloneCaseLibre] = self.tab[self.ligneCaseLibre-1][self.coloneCaseLibre]
            self.tab[self.ligneCaseLibre-1][self.coloneCaseLibre] = 0
            self.ligneCaseLibre -= 1
        elif sens == GAUCHE and GAUCHE in self.whatOp():
            self.tab[self.ligneCaseLibre][self.coloneCaseLibre] = self.tab[self.ligneCaseLibre][self.coloneCaseLibre+1]
            self.tab[self.ligneCaseLibre][self.coloneCaseLibre+1] = 0
            self.coloneCaseLibre += 1
        elif sens == DROITE and DROITE in self.whatOp():
            self.tab[self.ligneCaseLibre][self.coloneCaseLibre] = self.tab[self.ligneCaseLibre][self.coloneCaseLibre-1]
            self.tab[self.ligneCaseLibre][self.coloneCaseLibre-1] = 0
            self.coloneCaseLibre -= 1
            
    def whatOp(self):
        #~ self.OperateurHaut = 1
        #~ self.OperateurBas = 1
        #~ self.OperateurGauche = 1
        #~ self.OperateurDroite = 1
        
        #~ if self.coloneCaseLibre == 0:
            #~ self.OperateurDroite = 0
        #~ elif self.coloneCaseLibre == self.colone-1:
            #~ self.OperateurGauche = 0
        #~ if self.ligneCaseLibre == self.ligne-1:
            #~ self.OperateurHaut = 0
        #~ elif self.ligneCaseLibre == 0:
            #~ self.OperateurBas = 0
            
        ops = []
        if self.coloneCaseLibre != 0:
            ops.append(DROITE)
        if self.coloneCaseLibre != self.colone-1:
            ops.append(GAUCHE)
        if self.ligneCaseLibre != self.ligne-1:
            ops.append(HAUT)
        if self.ligneCaseLibre != 0:
            ops.append(BAS)
        return ops

    def shuffle(self):
        for i in range(0, 25*self.ligne*self.colone):
            mouvement = randint(0, 3)
            if mouvement == 0:
                self.move(HAUT)
            elif mouvement == 1:
                self.move(BAS)
            elif mouvement == 2:
                self.move(GAUCHE)
            else:
                self.move(DROITE)
    
    def nbPieceFalse(self):
        bonNum = 1
        nbFalse = 0
        for i in range(0, self.ligne):
            for j in range(0, self.colone):
                if self.tab[i][j] != bonNum and self.tab[i][j] != 0:
                    nbFalse += 1
                bonNum +=1
        return nbFalse
    
    def distanceManathan(self, l, c):
        bonNum = 1
        dif = 0
        numATrouver = self.tab[l][c]
        if numATrouver != 0:
            #print "numATrouver="+str(numATrouver)
            for i in range(0, self.ligne):
                for j in range(0, self.colone):
                    if bonNum == numATrouver:
                        dif = abs(i-l) + abs(j-c)
                        return dif
                    bonNum +=1
        else:
            return 0
                
    def distanceManathanTot(self):
        distance = 0
        for i in range(0, self.ligne):
            for j in range(0, self.colone):
                x = self.distanceManathan(i, j)
                distance += x
        return distance
    
    def resoudre(self):
        i = 0
        frontiere = [self]
        history = []
        while frontiere:
            etat = frontiere.pop()
            history.append(etat)
            if etat.isFinal():
                print "Bravo, c'est fini"
                return etat
            ops = etat.whatOp()
            for op in ops:
                new = etat.move(op)
                if(new not in frontiere and (new not in history)):
                    insert(frontiere, new)

    def insert(self, frontiere, new):
        


plateau = Taquin(3,3)
print "init : "
plateau.afficher()
plateau.shuffle()
print "mélangé : "
plateau.afficher()
print ""
plateau.resoudre()
print ""

