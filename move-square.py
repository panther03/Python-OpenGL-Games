import pygame
import sys
import math
import pygame.draw
import time
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

size = (600, 800)
black = (0, 0, 0)
white = (255, 255, 255)

phi = 0.0
theta = 75.0
delta_angle = 10.0
boxy=0

screen = pygame.display.set_mode(size, pygame.OPENGL|pygame.DOUBLEBUF)

glMatrixMode(GL_PROJECTION) 
glLoadIdentity()

gluPerspective(100, 3.0/4.0,10, 1000)
glMatrixMode(GL_MODELVIEW)

x = 100.0
y = 430.0
t = 0
vx = 0.0
vy = 00.0

def mod(x,y):
    res = x
    while res > y:
        res -= y
    return res

def looparound(x):
    if x < 20:
        return x
    elif x>20:
        return mod(x,20)
    else:
        return -10

def update():
    global x, y, vx, vy
    ax = 300.0 - x
    ay = 400.0 - y
    
    vx += 0.001 * ax
    vy += 0.001 * ay
    
    x += vx
    y += vy

def draw_cube():
    glBegin(GL_QUADS)
    glColor3f(1, abs(math.cos(t)), abs(math.sin(t)))
    glVertex3f(-10, 0, 0)
    glVertex3f(-8, 0, 0)
    glVertex3f(-8, 2, 0)
    glVertex3f(-10, 2, 0)
    glEnd()

def draw():
    print looparound(t),t
    glPushMatrix()
    glTranslatef(0, 0, -10)
    glTranslatef(looparound(t),boxy,0)
    #glRotatef(t, 0, 1, 0)
    
    draw_cube()
    glPopMatrix()


while True:
    t += 1
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
        elif ev.type == pygame.KEYDOWN:
            if (ev.key == pygame.K_ESCAPE or 
                ev.key == pygame.K_q):
                draw()
            elif ev.key == pygame.K_LEFT:
                sys.exit()
            elif ev.key == pygame.K_RIGHT:
                sys.exit()
            elif ev.key == pygame.K_UP:
                boxy+=5
                draw()
            elif ev.key == pygame.K_DOWN:
                boxy-=5
                draw()        
    
    update()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw()

    pygame.display.flip()    
    time.sleep(0.01)
