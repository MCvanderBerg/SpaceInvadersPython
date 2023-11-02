import pygame
from Constants import CLEAR

class Alien:
    def __init__(self, xPos, yPos):
        self.width = 50
        self.height = 50
        self.x = xPos
        self.y = yPos
        self.vx = 10
        self.vy = 10
        self.color = (255,255,255)

    def printAlien(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def clearAlien(self,screen):
        pygame.draw.rect(screen, CLEAR, pygame.Rect(self.x, self.y, self.width, self.height))

    def updateX(self):
        self.x += self.vx

    def inverseDirectionX(self):
        self.vx *= -1

    def updateY(self):
        self.y += self.vy


        

