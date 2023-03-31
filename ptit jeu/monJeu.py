# -*- coding: UTF-8 -*-

from livewires import games
from livewires import colour
from random import randint

SCREENWIDTH=1024
SCREENHEIGHT=768

def the_end():
    import sys
    sys.exit(0)
    
class Balle (games.Circle, games.Mover):
    def __init__ (self, screen, r):
        self.r = r
        self.init_circle (screen, SCREENWIDTH/2, SCREENHEIGHT/2, r, colour.red)
        self.init_mover(dx=randint(-2,2),dy=randint(-2,2))

    def moved(self): #games.Mover.moved
        (x,y) = self.pos()
        (dx,dy) = self.get_velocity()
        if dy == 0:
            dy = 1
        
        if x-self.r < 0 or x+self.r > SCREENWIDTH:
            dx = -dx
        if y-self.r < 0 or y+self.r > SCREENHEIGHT:
            self.lost()
        
        self.set_velocity(dx,dy)
        
        obj = self.overlapping_objects()
        for o in obj:
            self.hit(o)
            
    def hit(self, hitter):
        if isinstance(hitter,Raquette):
            (dx,dy) = self.get_velocity()
            self.set_velocity(dx,-dy)
            
    def lost(self):
        games.Message(my_screen, SCREENWIDTH/2, SCREENHEIGHT/2, "Perdu!", 50, colour.green, 500, the_end)
        self.destroy()
        
class Raquette(games.Polygon, games.Mover):
    def __init__ (self, screen, w, h, posDepart):
        self.y = posDepart
        self.w = w
        self.x = SCREENWIDTH/2-self.w/2
        self.h = h
        LIST_POINTS = ((0,0),(self.w,0),(self.w,self.h),(0,self.h))
        self.init_polygon(screen, self.x, self.y, LIST_POINTS, colour.green)
        self.init_mover(dx=0, dy=0)

    def moved(self): # games.Mover.moved
        (x,y) = self.pos()
        (dx,dy) = self.get_velocity()
    
        if self.screen.is_pressed(games.K_LEFT): dx -= .1
        if self.screen.is_pressed(games.K_RIGHT): dx += .1
        if self.screen.is_pressed(games.K_UP): dy -= .1
        if self.screen.is_pressed(games.K_DOWN): dy += .1
        
        dx *= .99
        dy *= .99
        
        if x <= 0 :
            x = 0
            dx = 0.01
        if x >= SCREENWIDTH - self.w :
            x =  SCREENWIDTH - self.w
            dx = -0.01
        
        self.move_to(x,y)
        self.set_velocity(dx,0)
        
        obj = self.overlapping_objects()
        for o in obj:
            self.hit(o)
        
    def hit(self, hitter):
        if isinstance(hitter,Balle):
            (x,y) = self.pos()
            games.Message(my_screen, x+self.w/2, y+self.h/2, "bing", 20, colour.red, 50, None)  
        
my_screen = games.Screen (SCREENWIDTH, SCREENHEIGHT)

Balle(my_screen, 15)
raq1 = Raquette(my_screen, 90, 15, 10)
raq2 = Raquette(my_screen, 90, 15, SCREENHEIGHT-20)

my_screen.mainloop ()