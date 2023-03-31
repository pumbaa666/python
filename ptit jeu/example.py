# -*- coding: UTF-8 -*-
"""
Exemple d'utilisation des classes de livewires pour créer un petit jeu simple
Matthieu Amiguet, 2006
"""

from livewires import games
from livewires import colour
from random import randint

SCREENWIDTH=800
SCREENHEIGHT=600

class Rond (games.Circle):
	def __init__ (self, screen):
		self.init_circle (
			screen = screen, 
			x = randint(0,SCREENWIDTH), y = randint(0,SCREENHEIGHT), 
			radius = randint(10,30), 
			colour = colour.grey
		)

class Triangle (games.Polygon, games.Mover):
	LIST_POINTS = ((0,0),(12,0),(6,-20))
	def __init__ (self, screen):
		self.init_polygon (
			screen=screen, 
			x=randint(0,SCREENWIDTH), y=randint(0,SCREENHEIGHT), 
			shape = Triangle.LIST_POINTS, 
			colour = colour.red
		)
		self.init_mover(dx=randint(1,3),dy=randint(1,3))

	def moved(self): #games.Mover.moved
		(x,y) = self.pos()
		(dx,dy) = self.get_velocity()
		
		self.rotate_by(randint(-180,180))
		
		if x<0 or x > SCREENWIDTH: dx = -dx
		if y<0 or y > SCREENHEIGHT: dy = -dy
		
		if self.screen.is_pressed(games.K_LSHIFT): 
			dx = dy
			dy= dx
		
		
		
		self.set_velocity(dx,dy)
		
		obj = self.overlapping_objects()
		for o in obj:
			self.hit(o)
		
	def hit(self, hitter):
		if isinstance(hitter,Rond):
			hitter.destroy()
			
class Ship(games.Polygon, games.Mover):
	LIST_POINTS = ((0,0),(15,0),(15,15),(0,15))
	def __init__ (self, screen):
		self.init_polygon (
			screen=screen, 
			x=randint(0,SCREENWIDTH), y=randint(0,SCREENHEIGHT), 
			shape = Ship.LIST_POINTS, 
			colour = colour.blue
		)
		self.init_mover(dx=0,dy=0)
	
	def moved(self): # games.Mover.moved
		(x,y) = self.pos()
		(dx,dy) = self.get_velocity()
		
		if self.screen.is_pressed(games.K_LEFT): dx -= .1
		if self.screen.is_pressed(games.K_RIGHT): dx += .1
		if self.screen.is_pressed(games.K_UP): dy -= .1
		if self.screen.is_pressed(games.K_DOWN): dy += .1
		
		dx *= .99
		dy *= .99
		
		if x<0 : x = dx = 0
		if x > SCREENWIDTH - 15 : x =  SCREENWIDTH - 15; dx = 0
		if y<0 : y = dy= 0
		if y > SCREENHEIGHT - 15 : y = SCREENHEIGHT - 15; dy = 0
		
		self.move_to(x,y)
		self.set_velocity(dx,dy)
		
		obj = self.overlapping_objects()
		for o in obj:
			self.hit(o)
		
	def hit(self, hitter):
		self.destroy()
		lost()
			
def lost():
	games.Message(my_screen,
		SCREENWIDTH/2, SCREENHEIGHT/2,
		"You Lost!", 
		size = 50, 
		colour = colour.green, 
		lifetime=500,
		after_death=the_end)
	
def the_end():
	import sys
	sys.exit(0)
		
my_screen = games.Screen (width = SCREENWIDTH, height = SCREENHEIGHT)
for i in range(10):
	Rond (screen = my_screen)
for i in range(5):
	Triangle(screen = my_screen)

Ship(my_screen)

my_screen.mainloop ()