import pygame
import Enemies as en
import Player as pl
from Missle import Missle as mle
import sys
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT, CLEAR, screen

running = True
clock = pygame.time.Clock()


#Initialize pygame
pygame.init()
enemies = en.Enemies()
player = pl.Player()


score = 0
scoreFont = pygame.font.SysFont("monospace", 36)
scoreLabel = scoreFont.render("Score: ", True, (255,255,0))

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
    global score
    while running:
        #Check for user inputs
        #Print update, clear player
        checkEvents()

        #Print Constants
        pygame.draw.rect(screen, CLEAR, pygame.Rect(100, 25, 100, 50))
        scoreValue = scoreFont.render(str(score), True, (255,255,0))
        screen.blit(scoreLabel, (10,25))
        screen.blit(scoreValue, (100, 25))

        pygame.draw.rect(screen, CLEAR, pygame.Rect(1500, 25, 5*player.width, player.height))
        for i in range(3-len(player.missles)):
           mle.printMissle(1500 + 50*i, 25)

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
                    if (player.missles[i].x >= enemies.aliens[j].x and  player.missles[i].x <= enemies.aliens[j].x + enemies.aliens[j].width and
                    player.missles[i].y > enemies.aliens[j].y and  player.missles[i].y < enemies.aliens[j].y + enemies.aliens[j].height):
                        del player.missles[i]
                        del enemies.aliens[j]
                        score += 10
                        break
                







