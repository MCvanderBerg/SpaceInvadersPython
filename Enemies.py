from Alien import Alien
from Shooters import Shooter
from Constants import SCREEN_WIDTH, ALIEN_AMOUNT_ROW, ALIEN_AMOUNT_COLUMN, X_OFFSET, Y_OFFSET, WIDTH

class Enemies:
    def __init__(self):
        self.aliens = []
        for i in range(ALIEN_AMOUNT_ROW):
            for j in range(ALIEN_AMOUNT_COLUMN):
                self.aliens.append(Shooter(i*WIDTH*3 + X_OFFSET,j*WIDTH*2 + Y_OFFSET))

    def getAliens(self):
        return self.aliens

    def printEnemies(self):
        for a in self.aliens:
            a.printAlien()

    def updateEnemies(self):
        reverseXdirection = False
        for a in self.aliens:
            if a.x + a.width >= SCREEN_WIDTH  or a.x <= 0: 
                reverseXdirection = True
                break

        for a in self.aliens:
            if isinstance(a, Shooter):
                a.createNewMissle()
                a.clearMissles()
                a.updateMissles()
                a.printMissles()

            if reverseXdirection:
                a.inverseDirectionX()
                a.updateY()
            a.updateX()

                


    def clearEnemies(self):
        for a in self.aliens:
            a.clearAlien()