# pip install pygame
# sudo apt-get install python3-tk

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color
    
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
    
    def draw(self, surface, eyes=False):
        distance = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*distance+1, j*distance+1, distance-2, distance-2))
        if eyes:
            centre = distance // 2
            radius = 3
            circleMiddle = (i*distance+centre-radius, j*distance+8)
            circleMiddle2 = (i*distance + distance-radius*2, j*distance+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


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
                # the snake goes to the other side of the board
                if c.dirnx == -1 and c.pos[0] <=0 : c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)
                else: c.move(c.dirnx, c.dirny)


    def reset(self, pos):
        pass

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        # add body on the opposite direction of the head
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1]+1)))
        
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True) # first cube has eyes
            else:
                c.draw(surface)

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
    global width, rows, s, snack
    surface.fill((0, 0, 0)) # black background
    drawGrid(width, rows, surface)
    s.draw(surface)
    snack.draw(surface)
    pygame.display.update()
    

def randomSnack(rows, item):
    positions = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        # don't put the snack on the top of the snake
        if len(list(filter(lambda x:x.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x,y)


def message_box(subject, content):
    pass

def main():
    global width, rows, s, snack
    width = 500
    rows = 20

    win = pygame.display.set_mode((width, width)) # surface
    clock = pygame.time.Clock()

    s = snake((255, 0, 0), (10, 10)) # red color, start_position
    snack = cube(randomSnack(rows, s), color=(0,255,0)) # green snack

    flag = True
    while flag:
        pygame.time.delay(50)
        clock.tick(10) # 10 frames per second

        s.move()

        # if the head touches the snack, add one body and new random snack
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0,255,0))

        redrawWindow(win)


main()