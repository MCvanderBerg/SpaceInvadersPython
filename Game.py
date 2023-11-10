import pygame
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

def checkEvents():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
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




player.print()
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

        pygame.draw.rect(screen, CLEAR, pygame.Rect(1500, 20, 10*player.width, player.height + 20))
        for i in range(3-len(player.missles)):
           mle.printMissle(1500 + 40*i, 25)

        if player.lives:
            for i in range(player.lives):
                screen.blit(player.livesUrl, (1610 + 60*i, 10))
        #else game over

        #Print Enemies, Missles to screen
        enemies.printEnemies()
        player.printMissles()
        missles.print()

        #Double buffer. Display all printed elements
        pygame.display.flip()
        clock.tick(10)

        #Print Enemies, Missles to screen
        enemies.clearEnemies()
        player.clearMissles()
        missles.clear()

        #Print Enemies, Missles to screen
        enemies.updateEnemies()
        player.updateMissles()
        missles.update()
    


        #Do colition detection
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
            #Create random new missles
            for a in range(len(enemies.aliens)):
                missles.add(enemies.aliens[a].x, enemies.aliens[a].y)

        if (len(player.missles)):
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
        








