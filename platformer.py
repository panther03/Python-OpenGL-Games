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
playerx=5
playery=0

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
    glVertex3f(0, 0, 0)
    glVertex3f(2, 0, 0)
    glVertex3f(2, 2, 0)
    glVertex3f(0, 2, 0)
    glEnd()

def draw_player_matrix():
    glPushMatrix()
    glTranslatef(0, 0, -10)
    glTranslatef(playerx,playery,0)
    #glRotatef(t, 0, 1, 0)    
    draw_player()
    glPopMatrix()

def draw_platform():
    glBegin(GL_QUADS)
    glColor3f(0.5, 1, 0.5)
    glVertex3f(-6, 3, 0)
    glVertex3f(-2, 3, 0)
    glVertex3f(-2, 5, 0)
    glVertex3f(-6, 5, 0)
    glEnd()

def draw_platform_matrix():
    glPushMatrix()
    glTranslatef(0, 0, -10)
    draw_platform()
    glPopMatrix()


while True:
    t += 1
    for ev in pygame.event.get():
	if ev.type == pygame.QUIT:
	    sys.exit()
	elif ev.type == pygame.KEYDOWN:
	    if (ev.key == pygame.K_ESCAPE or 
		ev.key == pygame.K_q):
		draw_player_matrix()
	    elif ev.key == pygame.K_SPACE:
		if (playery <= 3 and -7.5 < playerx < -2):
			playery+=2
		else:		
			playery+=6
		draw_player_matrix()
	    elif ev.key == pygame.K_LEFT:
		if playerx<=-10:
		    playerx=-10
		else:                
		    playerx-=1
		draw_player_matrix()
	    elif ev.key == pygame.K_RIGHT:
		if playerx>=18:
		    playerx=18
		else:
		    playerx+=1
		draw_player_matrix()
    if not (playery <= 0 or (playery == 5 and -7.5 < playerx < -2)):
	playery -= 0.25
    #for ev in pygame.event.get():
        #if ev.type == pygame.QUIT:
       #     sys.exit()
      #  elif ev.type == pygame.KEYDOWN:
     #       if (ev.key == pygame.K_ESCAPE or 
    #            ev.key == pygame.K_q):
   #          elif ev.key == pygame.K_LEFT:
 #               if playerx <= -10:
#		else:
#			playerx-=2
#
         #   elif ev.key == pygame.K_RIGHT:
        #        sys.exit()
        #    elif ev.key == pygame.K_UP:
        #        playery+=5
        #        draw_player_matrix()
        #    elif ev.key == pygame.K_DOWN:
        #        playery-=5
        #        draw_player_matrix()        
    
    update()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    draw_player_matrix()
    draw_platform_matrix()
    pygame.display.flip()
    time.sleep(0.01)

