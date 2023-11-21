import pygame
from pygame import Rect, draw
from Enemies import Enemies
from Player import Player
from Missle import Missle as mle
from Missles import Missles
import sys
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT, CLEAR, screen

running = True
clock = pygame.time.Clock()

#Initialize pygame
pygame.init()
enemies = Enemies()
player = Player()
missles = Missles()

score = 0
scoreFont = pygame.font.SysFont("monospace", 36)
scoreLabel = scoreFont.render("Score: ", True, (255,255,0))
result = "startMenu"

def clearGameScreen(printPlayer = False):
    global player

    pygame.draw.rect(screen, CLEAR, pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    if printPlayer:
        player.print()
    pygame.display.flip()



def checkEvents():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                pause_game()

            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.clear()
                if event.key == pygame.K_a:
                    player.update(-1)
                if event.key == pygame.K_d:
                    player.update(1)
                
                player.print()


            if event.key == pygame.K_SPACE:
                player.createNewMissle()

            if event.key == pygame.K_ESCAPE:
                running = False


def pause_game():
    global running
    global result
    pauseState = True
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    titleFont = pygame.font.SysFont('arial', 60)

    pausedText = titleFont.render('Paused', True, (255, 255, 255))
    continueText = font.render('Continue', True, (255, 255, 255))
    exitText = font.render('Exit', True, (255, 255, 255))
   
    draw.rect(screen, CLEAR, Rect(0, 0, SCREEN_WIDTH , SCREEN_HEIGHT))

    screen.blit(pausedText, (SCREEN_WIDTH/2 - pausedText.get_width()/2, SCREEN_HEIGHT/2))
    screen.blit(continueText, (SCREEN_WIDTH/2 - continueText.get_width()/2, SCREEN_HEIGHT/2 + 60))
    screen.blit(exitText, (SCREEN_WIDTH/2 - exitText.get_width()/2, SCREEN_HEIGHT/2 + 100))

    pygame.display.update()

    while pauseState:
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()

                if (
                x >  SCREEN_WIDTH/2 - continueText.get_width()/2 and
                x <  SCREEN_WIDTH/2 + continueText.get_width()/2 and
                y > SCREEN_HEIGHT/2 + 60 and 
                y < SCREEN_HEIGHT/2 + 60 + continueText.get_height()
                ):
                    pauseState = False
                    break

                if (
                x >  SCREEN_WIDTH/2 - exitText.get_width()/2 and
                x <  SCREEN_WIDTH/2 + exitText.get_width()/2 and
                y > SCREEN_HEIGHT/2 + 100 and 
                y < SCREEN_HEIGHT/2 + 100 + exitText.get_height()
                ):
                    pauseState = False
                    running = False
                    result = "startMenu"
                    break
    clearGameScreen(True)


                



def run_game():
    global enemies
    global player
    global missles
    global running
    global clock
    global score
    global scoreLabel
    #Initialize pygame
    pygame.init()
    enemies = Enemies()
    player = Player()
    missles = Missles()

    running = True
    clock = pygame.time.Clock()

    clearGameScreen(True)

    score = 0
    scoreFont = pygame.font.SysFont("monospace", 36)
    scoreLabel = scoreFont.render("Score: ", True, (255,255,0))

    while running:
        checkEvents()

        pygame.draw.rect(screen, CLEAR, pygame.Rect(100, 25, 100, 50))
        scoreValue = scoreFont.render(str(score), True, (255,255,0))
        screen.blit(scoreLabel, (10,25))
        screen.blit(scoreValue, (100, 25))

        pygame.draw.rect(screen, CLEAR, pygame.Rect(1500, 20, 10*player.width, player.height + 20))
        for i in range(3-len(player.missles)):
           mle.printMissle(1500 + 40*i, 25)

        if player.lives:
            for i in range(player.lives):
                screen.blit(player.livesUrl, (1610 + 60*i, 10))

        enemies.printEnemies()
        player.printMissles()
        missles.print()

        pygame.display.flip()
        clock.tick(10)

        enemies.clearEnemies()
        player.clearMissles()
        missles.clear()

        enemies.updateEnemies()
        player.updateMissles()
        missles.update()
    
        for m in reversed(range(len(missles.missles))):
            if (
            missles.missles[m].x >= player.x and
            missles.missles[m].x <= player.x + player.width and
            missles.missles[m].y >= player.y and
            missles.missles[m].y <= player.y + player.height):
                missles.missles[m].clear()
                del missles.missles[m]
                player.print()
                player.lives -=1

        if (enemies.aliens):            
            for a in range(len(enemies.aliens)):
                missles.add(enemies.aliens[a].x, enemies.aliens[a].y)

        if len(player.missles):
            for i in reversed(range(len(player.missles))):
                for j in range(len(enemies.aliens)):
                    if (
                    player.missles[i].x >= enemies.aliens[j].x and
                    player.missles[i].x <= enemies.aliens[j].x + enemies.aliens[j].width and
                    player.missles[i].y > enemies.aliens[j].y and
                    player.missles[i].y < enemies.aliens[j].y + enemies.aliens[j].height
                    ):
                        del player.missles[i]
                        del enemies.aliens[j]
                        score += 10
                        break

        if not enemies.aliens:
            pygame.draw.rect(screen, CLEAR, pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.flip()
            running = False
            return "startMenu"

        if not player.lives:
            pygame.draw.rect(screen, CLEAR, pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.flip()
            running = False
            return "gameOver"

        if not running:
            return result


        








