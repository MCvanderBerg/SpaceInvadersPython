import pygame
from Game import run_game
from MainMenu import run_menu
from GameOver import game_over
import sys
from Constants import screen, SCREEN_HEIGHT, SCREEN_WIDTH, CLEAR 

gameState = "gameOver"
while True:
    if gameState == "startMenu":
        gameState = run_menu()
    elif gameState == "runGame":
        gameState = run_game()
    elif gameState == "gameOver":
        gameState = game_over()



