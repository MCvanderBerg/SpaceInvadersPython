import pygame
import Missle
from Constants import SCREEN_HEIGHT, SCREEN_WIDTH, CLEAR, PLAYERCOLOR, screen

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT - 200
        self.width = 30
        self.height = 15
        self.vx = 11
        self.color = PLAYERCOLOR
        self.missles = []

    def createNewMissle(self):
        self.missles.append(Missle.Missle(self.x + self.width/2, self.y))

    def updateMissles(self):
        if self.missles:
            for i in range(len(self.missles)):
                if self.missles[i].y <=0:
                    print("delete")
                    del self.missles[i]
                else:
                    self.missles[i].update()


    def printMissles(self):
        if self.missles:
            for m in self.missles:
                m.print()

    def clearMissles(self):
        if self.missles:
            for m in self.missles:
                m.clear()
                         
    def clearPlayer(self):
        pygame.draw.rect(screen, CLEAR, pygame.Rect(self.x, self.y, self.width, self.height))

    def printPlayer(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def updatePlayer(self,direction):
        self.x += direction*self.vx
