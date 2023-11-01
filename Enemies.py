import Alien as invader

#CONSTANTS
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
ALIEN_AMOUNT_ROW = 10
ALIEN_AMOUNT_COLUMN = 4
X_OFFSET = 30
Y_OFFSET = 30
WIDTH = 30

class Enemies:
    def __init__(self):
        self.aliens = []
        for i in range(ALIEN_AMOUNT_ROW):
            for j in range(ALIEN_AMOUNT_COLUMN):
                self.aliens.append(invader.Alien(i*WIDTH*3 + X_OFFSET,j*WIDTH*2 + Y_OFFSET))

    def getAliens(self):
        return self.aliens

    def printEnemies(self, screen):
        for a in self.aliens:
            a.printAlien(screen)

    def updateEnemies(self):
        reverseXdirection = False
        for a in self.aliens:
            if a.x + a.width >= SCREEN_WIDTH  or a.x <= 0: 
                reverseXdirection = True
                break

        for a in self.aliens:
            if reverseXdirection:
                a.inverseDirectionX()
                a.updateY()
            a.updateX()
                


    def clearEnemies(self, screen):
        for a in self.aliens:
            a.clearAlien(screen)