import pygame
import Game

#Contants
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000

#Initialize pygame
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        Game.run_game(screen)
        pygame.display.flip()

pygame.quit()