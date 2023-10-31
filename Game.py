import pygame
import Alien as invader


def run_game(screen):
    gameState = True
    ALIEN_AMOUNT_ROW = 10
    ALIEN_AMOUNT_COLUMN = 4
    alien = []

    for i in range(ALIEN_AMOUNT_ROW):
        for j in range(ALIEN_AMOUNT_COLUMN):
            alien.append(invader.Alien(i*30*3 + 30,j*30*2 + 30))

    while gameState:
        myFirstAlien = invader.Alien(10,10)

        
        #pygame.draw.rect(screen,myFirstAlien.color, myFirstAlien.image)
        for a in alien:
            a.printAlien(screen)

        gameState = False
