from Constants import SCREEN_WIDTH, SCREEN_HEIGHT, CLEAR, screen
import pygame


def run_menu():
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('My Game', True, (255, 255, 255))
        start_button = font.render('Start', True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/2))
        screen.blit(start_button, (SCREEN_WIDTH/2 - start_button.get_width()/2, SCREEN_HEIGHT/2 + start_button.get_height()/2))
        pygame.display.update()