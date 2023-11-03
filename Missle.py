import pygame
from Constants import *

class Missle:
    def __init__(self, x, y):
        self.width = 2
        self.height = 5
        self.x = x
        self.y = y - self.height
        self.color = (255,0,255)
        self.vy = 10
        self.damage = 20

    def getX(self):
        return self.x

    def update(self):
        self.y -= self.vy

    def print(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def clear(self):
        pygame.draw.rect(screen, CLEAR, pygame.Rect(self.x, self.y, self.width, self.height))
        




