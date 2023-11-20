from Constants import SCREEN_WIDTH, SCREEN_HEIGHT, CLEAR, screen
import pygame


def run_menu():        
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('My Game', True, (255, 255, 255))
        start_button = font.render('Start', True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2))
        screen.blit(start_button, (SCREEN_WIDTH/2 - start_button.get_width()/2, SCREEN_HEIGHT/2 + 100))
        pygame.display.update()

        run = True
        result = "runGame"
        while run:
                for event in pygame.event.get(): 
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()

                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                        pygame.draw.rect(screen, CLEAR, pygame.Rect(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT))
                                        result = "runGame"
                                        run = False
                                        break

                                if event.key == pygame.K_ESCAPE:
                                        pygame.quit()
                                        quit()

                        if event.type == pygame.MOUSEBUTTONUP:
                                x,y = pygame.mouse.get_pos()

                                if (
                                x >  SCREEN_WIDTH/2 - start_button.get_width()/2 and
                                x <  SCREEN_WIDTH/2 + start_button.get_width()/2 and
                                y > SCREEN_HEIGHT/2 + 100 and 
                                y < SCREEN_HEIGHT/2 + 100 + start_button.get_height()
                                ):
                                        result = "runGame" 
                                        run = False
                                        break

        return result

