import pygame
import sys
import math
import pygame.draw
import time
import os
from OpenGL.GL import *
from OpenGL.GLU import *
import pyglet
import subprocess
from threading import Thread

#def play_music():
#    return subprocess.call('mpg123 "Awolnation - Sail.mp3"', shell=True)

#thread = Thread(target = play_music, args = ())
#thread.daemon = true
#thread.start()

size = (600, 800)
black = (0, 0, 0)
white = (255, 255, 255)

phi = 0.0
theta = 75.0
delta_angle = 10.0
boxy=0
boxx=0
obsty=1

screen = pygame.display.set_mode(size, pygame.OPENGL|pygame.DOUBLEBUF)

glMatrixMode(GL_PROJECTION) 
glLoadIdentity()

gluPerspective(100, float(size[0]) / size[1],10, 1000)
glMatrixMode(GL_MODELVIEW)

x = 100.0
y = 430.0
t = 0
vx = 0.0
vy = 00.0

class Obstacle:

	def __init__(self,posarg,lengtharg):
		self.mispos = posarg
		self.length = lengtharg
		self.pos = 2.5

	def drawx(self):
		glBegin(GL_QUADS)
    		glColor3f(0.5, 1, 0.5)
    		glVertex3f(0, self.mispos, 0)
    		glVertex3f(self.length, self.mispos, 0)
   		glVertex3f(self.length, self.mispos+self.length, 0)
    		glVertex3f(0, self.mispos+self.length, 0)
    		glEnd()
	
	def drawx_matrix(self):
		print self.pos
    		glPushMatrix()
    		glTranslatef(0,0,-10)
    		if self.pos >= 17.5:
			self.pos = -10
    		else:
    			self.pos += 0.5
    		glTranslatef(self.pos-10,0,0)
    		self.drawx()
    		glPopMatrix()


def mod(x,y):
    if x == y:
        return 0
    else:
        res = x
        while res > y:
            res -= y
        return res

def looparound(x):
    if mod(x,20) <= 10:
        return mod(x,20)
    elif mod(x,20) > 10:
        return mod(x,20) - 20


def update():
    global x, y, vx, vy
    ax = 300.0 - x
    ay = 400.0 - y
    
    vx += 0.001 * ax
    vy += 0.001 * ay
    
    x += vx
    y += vy

def draw_player():
    glBegin(GL_QUADS)
    glColor3f(1, 0.5, 0.5)
    glVertex3f(-10, 0, 0)
    glVertex3f(-8, 0, 0)
    glVertex3f(-8, 2, 0)
    glVertex3f(-10, 2, 0)
    glEnd()

def draw_player_matrix():
    glPushMatrix()
    glTranslatef(0, 0, -10)
    glTranslatef(boxx,boxy,0)
    #glRotatef(t, 0, 1, 0)
    
    draw_player()
    glPopMatrix()

def draw_obstacles():
    glBegin(GL_QUADS)
    glColor3f(0.5, 1, 0.5)
    glVertex3f(2, 0, 0)
    glVertex3f(2, 2, 0)
    glVertex3f(0, 2, 0)
    glVertex3f(0, 0, 0)
    glEnd()

def draw_obstacles_matrix():
    global obsty
    print t,obsty,boxx,boxy
    glPushMatrix()
    glTranslatef(0,0,-10)
    if obsty >= 20:
	obsty = -10
    else:
    	obsty += 0.5
    glTranslatef(0,obsty,0)
    draw_obstacles()
    glPopMatrix()

def draw_goal():
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.5, 1)
    glVertex3f(7.5, 1, 0)
    #glVertex3f(7.5, 2, 0)
    #glVertex3f(9.5, 2, 0)
    glVertex3f(9.5, 2, 0)
    glVertex3f(9.5, 0, 0)
    glEnd()

		
def draw_goal_matrix():
    glPushMatrix()
    glTranslatef(0,0,-10)
    draw_goal()
    glPopMatrix()

Obstacle2 = Obstacle(2.5,2)
Obstacle3 = Obstacle(-2.5,2)



while True:
    t += 1
    if boxx == 10 and boxy == obsty:
        print "Looozer: You touched a square of death! YOU DIE!"  
	sys.exit()
    elif boxx == 17.5 and boxy == 0.0:
    	print "Winner: You reached the triangle of life! YOU WIN!" 
   	sys.exit() 
    elif boxx == Obstacle2.pos and boxy == Obstacle2.mispos:
	print "Loozer: You touched a square of death! YOU DIE!"
	sys.exit()
    elif boxx == Obstacle3.pos and boxy == Obstacle3.mispos:
	print "Loozer: You touched a square of death! YOU DIE!"
	sys.exit()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()

        elif ev.type == pygame.KEYDOWN:
            if (ev.key == pygame.K_ESCAPE or 
                ev.key == pygame.K_q):
                draw_player_matrix()
            elif ev.key == pygame.K_LEFT:
                if boxx<=0:
                    boxx=0
                else:                
                    boxx-=2.5
            elif ev.key == pygame.K_RIGHT:
                if boxx>=17.5:
                    boxx=17.5
                else:
                    boxx+=2.5
            elif ev.key == pygame.K_UP:
                if boxy>=10:
                    boxy=10
                else:                
                    boxy+=2.5
                draw_player_matrix()

            elif ev.key == pygame.K_DOWN:
                if boxy<=-10:
                    boxy=-10
                else:                    
                    boxy-=2.5
                draw_player_matrix()        
    
    update()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_player_matrix()      
    draw_obstacles_matrix()
    draw_goal_matrix()
    Obstacle2.drawx_matrix()
    Obstacle3.drawx_matrix()
    pygame.display.flip()    
    time.sleep(0.01)

