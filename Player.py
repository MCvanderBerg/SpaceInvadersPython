import pygame

#CONSTANTS
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
CLEAR = (0,0,0)


class Player:
    def __init__(self, screen):
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT - 200
        self.width = 30
        self.height = 15
        self.vx = 11
        self.screen = screen
        self.color = (255,255,0)

    def clearPlayer(self):
        pygame.draw.rect(self.screen, CLEAR, pygame.Rect(self.x, self.y, self.width, self.height))

    def printPlayer(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def updatePlayer(self,direction):
        self.x += direction*self.vx
