# pip install pygame
# sudo apt-get install python3-tk

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

class snake(object):
    body = []
    turns = {}
    """ Each snake contains many cubes """
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos) # new cube to be head
        self.body.append(self.head) # first cube is the head
        # no diagonal directions
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                if keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                if keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                if keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        
        for i, c in enumerate(self.body): # index, cube
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p] # dirnx, dirny
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                # border collisions
                if c.dirnx == -1 and c.pos[0] <=0 : c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)
                else: c.move(c.dirnx, c.dirny)


    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBetween = w // rows

    x = 0 
    y = 0
    for l in range(rows):
        x += sizeBetween
        y += sizeBetween

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w)) # vertical lines
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y)) # horizontal lines
    
def redrawWindow(surface):
    global width, rows
    surface.fill((0, 0, 0)) # black background
    drawGrid(width, rows, surface)
    pygame.display.update()
    

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    rows = 20

    win = pygame.display.set_mode((width, width)) # surface
    clock = pygame.time.Clock()

    s = snake((255, 0, 0), (10, 10)) # red color, start_position

    flag = True
    while flag:
        pygame.time.delay(50)
        clock.tick(10) # 10 frames per second

        redrawWindow(win)
    
    pass

main()