import pygame
from Constants import *

class Missle:
    def __init__(self, x, y):
        self.imageUrl = pygame.image.load("./src/assets/icons/missle.png")
        self.imageScale = 1.5
        self.image = pygame.transform.scale(self.imageUrl, (self.imageUrl.get_width() * self.imageScale, self.imageUrl.get_height() * self.imageScale))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y - self.height
        self.vy = 10
        self.damage = 20

    @staticmethod
    def printMissle(x,y):
        imageUrl = pygame.image.load("./src/assets/icons/missle.png")
        imageScale = 1.5
        image = pygame.transform.scale(imageUrl, (imageUrl.get_width() * imageScale, imageUrl.get_height() * imageScale))
        screen.blit(image,(x, y))

    def getX(self):
        return self.x

    def update(self):
        self.y -= self.vy

    def print(self):
        screen.blit(self.image,(self.x, self.y))

    def clear(self):
        pygame.draw.rect(screen, CLEAR, pygame.Rect(self.x, self.y, self.width, self.height))
        




