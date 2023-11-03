import pygame
import Enemies as en
import Player as pl
import Missle 
import sys
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT

running = True
clock = pygame.time.Clock()

enemies = en.Enemies()
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
        enemies.printEnemies()
        player.printMissles()

        #Double buffer. Display all printed elements
        pygame.display.flip()
        clock.tick(10)


        #Print Enemies, Missles to screen
        enemies.clearEnemies()
        player.clearMissles()

        #Print Enemies, Missles to screen
        enemies.updateEnemies()
        player.updateMissles()

        #Do colition detection
        if (len(player.missles)):
            for i in reversed(range(len(player.missles))):
                for j in range(len(enemies.aliens)):
                    print(player.missles[i].x)
                    print(enemies.aliens[j].x)
                    if player.missles[i].x >= enemies.aliens[j].x and  player.missles[i].x <= enemies.aliens[j].x + enemies.aliens[j].width:
                        if  player.missles[i].y > enemies.aliens[j].y and  player.missles[i].y < enemies.aliens[j].y + enemies.aliens[j].height:
                            del player.missles[i]
                            del enemies.aliens[j]
                            break
                







