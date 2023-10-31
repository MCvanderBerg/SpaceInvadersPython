import pygame

class Alien:
    def __init__(self, xPos, yPos):
        self.width = 50
        self.height = 50
        self.x = xPos
        self.y = yPos
        self.color = (255,255,255)
        self.image = pygame.Rect(xPos ,yPos ,self.width, self.height)

    def printAlien(self, screen):
        pygame.draw.rect(screen, self.color, self.image)

