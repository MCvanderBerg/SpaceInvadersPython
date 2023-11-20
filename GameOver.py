from Constants import SCREEN_WIDTH, SCREEN_HEIGHT, CLEAR, screen
import pygame




def game_over():
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        titleFont = pygame.font.SysFont('arial', 60)

        title = titleFont.render('Game Over', True, (255, 255, 255))
        restart = font.render('Restart', True, (255, 255, 255))
        mainMenu = font.render('Main Menu', True, (255, 255, 255))

        screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2))
        screen.blit(mainMenu, (SCREEN_WIDTH/2 - mainMenu.get_width()/2, SCREEN_HEIGHT/2 + 60))
        screen.blit(restart, (SCREEN_WIDTH/2 - restart.get_width()/2, SCREEN_HEIGHT/2 + 100))

        pygame.display.update()

        result = "startMenu"
        run = True
        while run:
                for event in pygame.event.get(): 
                        if event.type == pygame.MOUSEBUTTONUP:
                                x,y = pygame.mouse.get_pos()

                                if (
                                x >  SCREEN_WIDTH/2 - mainMenu.get_width()/2 and
                                x <  SCREEN_WIDTH/2 + mainMenu.get_width()/2 and
                                y > SCREEN_HEIGHT/2 + 60 and 
                                y < SCREEN_HEIGHT/2 + 60 + mainMenu.get_height()
                                ):
                                        result = "startMenu" 
                                        run = False
                                        break

                                if (
                                x >  SCREEN_WIDTH/2 - restart.get_width()/2 and
                                x <  SCREEN_WIDTH/2 + restart.get_width()/2 and
                                y > SCREEN_HEIGHT/2 + 100 and 
                                y < SCREEN_HEIGHT/2 + 100 + restart.get_height()
                                ):
                                        result = "runGame" 
                                        run = False
                                        break
                                          
        print('returning result',result)
        return result
