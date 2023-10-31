import pygame
import Alien as invader
import time
import sys

#CONSTANTS
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
ALIEN_AMOUNT_ROW = 10
ALIEN_AMOUNT_COLUMN = 4
X_OFFSET = 30
Y_OFFSET = 30
WIDTH = 30

running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


#INITIALIZE ALIENS
aliens = []
for i in range(ALIEN_AMOUNT_ROW):
    for j in range(ALIEN_AMOUNT_COLUMN):
        aliens.append(invader.Alien(i*WIDTH*3 + X_OFFSET,j*WIDTH*2 + Y_OFFSET))


def printEnemies():
    for a in aliens:
        a.printAlien(screen)

def updateEnemies():
    for a in aliens:
        a.updateX()

def clearEnemies():
    for a in aliens:
        a.clearAlien(screen)

def checkEvents():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = False

def run_game():
    global running
    while running:
        print(aliens[0].x)

        checkEvents()
        printEnemies()
        pygame.display.flip()
        clearEnemies()
        updateEnemies()
        clock.tick(10)






