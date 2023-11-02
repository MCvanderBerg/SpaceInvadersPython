import pygame
import Enemies as en
import Player as pl
import Missle 
import sys
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT

running = True
clock = pygame.time.Clock()

aliens = en.Enemies()
player = pl.Player()

def checkEvents():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.clearPlayer()
                if event.key == pygame.K_a:
                    player.updatePlayer(-1)
                if event.key == pygame.K_d:
                    player.updatePlayer(1)
                
                player.printPlayer()


            if event.key == pygame.K_SPACE:
                player.createNewMissle()

            if event.key == pygame.K_ESCAPE:
                running = False


player.printPlayer()
def run_game():
    while running:
        #Check for user inputs
        #Print update, clear player
        checkEvents()

        #Print Enemies, Missles to screen
        aliens.printEnemies()
        player.printMissles()

        #Double buffer. Display all printed elements
        pygame.display.flip()
        clock.tick(10)


        #Print Enemies, Missles to screen
        aliens.clearEnemies()
        player.clearMissles()

        #Print Enemies, Missles to screen
        aliens.updateEnemies()
        player.updateMissles()







