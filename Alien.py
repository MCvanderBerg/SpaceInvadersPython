import pygame
from Constants import CLEAR, screen

class Alien:
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
        self.vx = 10
        self.vy = 10
        self.color = (255,255,255)
        self.imageUrl = pygame.image.load("./src/assets/icons/vanillaInvader.png")
        self.imageScale = 5
        self.image = pygame.transform.scale(self.imageUrl, (self.imageUrl.get_width() * self.imageScale, self.imageUrl.get_height() * self.imageScale))
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def printAlien(self):
        screen.blit(self.image,(self.x, self.y))

    def clearAlien(self):
        pygame.draw.rect(screen, CLEAR, pygame.Rect(self.x, self.y, self.width, self.height))

    def updateX(self):
        self.x += self.vx

    def inverseDirectionX(self):
        self.vx *= -1

    def updateY(self):
        self.y += self.vy


        

