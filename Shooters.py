from Alien import Alien
from Missle import Missle
from  random import randint
from Constants import SCREEN_HEIGHT


class Shooter(Alien): 
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos)
        self.missles = []

    def createNewMissle(self):
        if randint(0,1000) <= 1:
            self.missles.append(Missle(self.x + self.width/2, self.y, True))

    def updateMissles(self):
        if self.missles:
            for i in reversed(range(len(self.missles))):
                if self.missles[i].y >= SCREEN_HEIGHT:
                    del self.missles[i]
                else:
                    self.missles[i].update(1)


    def printMissles(self):
        if self.missles:
            for m in self.missles:
                m.print()

    def clearMissles(self):
        if self.missles:
            for m in self.missles:
                m.clear()