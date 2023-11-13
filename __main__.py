import pygame
from Game import run_game
from MainMenu import run_menu
import sys
from Constants import screen, SCREEN_HEIGHT, SCREEN_WIDTH, CLEAR 

gameState = "startMenu"

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.draw.rect(screen, CLEAR, pygame.Rect(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT))
                gameState = "runGame"

    if gameState == "startMenu":
        run_menu()
    elif gameState == "runGame":
        #Run game
        gameState = run_game()


    print("game over")