# -*- coding: UTF-8 -*-
import pygame
from data import *

font = pygame.font.Font(None,20)
def ecrire(screen, texte, color, x, y, size = 20):
    global font
    font = pygame.font.Font(None,size)
    text = font.render(texte, True, color)
    textRect = text.get_rect()
    textRect = textRect.move(x,y)
    screen.blit(text, textRect)
    pygame.display.flip()

def effacer(screen, texte, x, y, color = noir):
    text = font.render(texte, True, color)
    textRect = text.get_rect()
    textRect = textRect.move(x,y)
    pygame.draw.rect(screen, color, textRect, 0)
    pygame.display.flip()

def drawPoint(screen, positions):
    for pos in positions: 
        pygame.draw.circle(screen,rouge,pos,city_radius)
    pygame.display.flip()

def drawBouton(screen, texte, x, y, w, h, couleur = bleu):
    fontSize = 30
    font = pygame.font.Font(None,fontSize)
    text = font.render(texte, True, bleu)
    rectText = text.get_rect()
    rectangle = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, noir, rectangle, 0)
    pygame.draw.rect(screen, couleur, rectangle, 5)
    ecrire(screen, texte, couleur, x+w/2-rectText.w/2, y+h/2-rectText.h/2, fontSize)

def testerParametre():
    if taillePopDepart < 10 or taillePopDepart > 50:
        return True
    elif propSurvivant <= 0.1 or propSurvivant > 1:
        return True
    elif nbIterationSansChangementMax > 10*taillePopDepart:
        return True
    elif nbMutation < 5 or nbMutation > 100:
        return True
    return False