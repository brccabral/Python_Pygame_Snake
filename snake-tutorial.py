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
    """ Each snake contains many cubes """
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

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