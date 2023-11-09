import pygame
from Missle import Missle
import time
from Constants import SCREEN_HEIGHT, SCREEN_WIDTH, CLEAR, PLAYERCOLOR, screen

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT - 80
        self.vx = 11
        self.color = PLAYERCOLOR
        self.missles = []
        self.missleDebouncing = 1
        self.missleStartTime = time.time() - self.missleDebouncing
        self.imageUrl = pygame.image.load("./src/assets/icons/player.png")
        self.imageScale = 0.1
        self.image = pygame.transform.scale(self.imageUrl, (self.imageUrl.get_width() * self.imageScale, self.imageUrl.get_height() * self.imageScale))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.lives = 3
        livesUrl = pygame.image.load("./src/assets/icons/live.webp")
        self.livesUrl = pygame.transform.scale(livesUrl, (60, 60))
    def createNewMissle(self):
        currentTime = time.time()
        if len(self.missles) < 3 and currentTime > self.missleStartTime + self.missleDebouncing:
            self.missleStartTime = currentTime
            self.missles.append(Missle(self.x + self.width/2, self.y))

    def updateMissles(self):
        if self.missles:
            for i in reversed(range(len(self.missles))):
                if self.missles[i].y <=0:
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
                         
    def clear(self):
        pygame.draw.rect(screen, CLEAR, pygame.Rect(self.x, self.y, self.width, self.height))

    def print(self):
        screen.blit(self.image,(self.x, self.y))

    def update(self,direction):
        if ((direction > 0 and self.x + direction*self.vx + self.width < SCREEN_WIDTH) or
        (direction < 0 and self.x + direction*self.vx > 0)):
            self.x += direction*self.vx
