import pygame
import Enemies as en
import Player as pl
import sys
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT

running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

aliens = en.Enemies()
player = pl.Player(screen)

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

            if event.key == pygame.K_ESCAPE:
                running = False

def run_game():
    global running
    while running:
        checkEvents()
        aliens.printEnemies(screen)
        player.printPlayer()
        pygame.display.flip()
        aliens.clearEnemies(screen)
        aliens.updateEnemies()
        clock.tick(10)






