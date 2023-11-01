import pygame
import Enemies as en
import sys

#CONSTANTS
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000

running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

aliens = en.Enemies()

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
        checkEvents()
        aliens.printEnemies(screen)
        pygame.display.flip()
        aliens.clearEnemies(screen)
        aliens.updateEnemies()
        clock.tick(10)






