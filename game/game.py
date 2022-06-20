import pygame 
import random 
import sys
from util import element


#Start game
pygame.init()

#Make game window called game
game = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Odyssey")
icon = pygame.image.load(".\images\gameicon.png")
pygame.display.set_icon(icon)
rungame = True

#Make game background
background = element("./images/background.jpg", (1000, 800), (0,0), 0)

#Initialize player
'''
player = pygame.image.load("./images/spaceship.png")
player = pygame.transform.smoothscale(player, (75, 75))
playerX = 450
playerY = 675
playerSpeed = 0
def spawnPlayer(x,y):
    game.blit(player, (x,y) )
'''
player = element("./images/spaceship.png", (75,75), [450, 675], 1)

#Initialize alien
alienX = random.randint(0, 925)
alienY = random.randint(0,350)
alien = element("./images/alien.png", (75, 75), (alienX, alienY), 0)

#game loop
while rungame:
    background.spawn(game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
        
        #Add x-axis movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #Move left
                player.move(True)
            if event.key == pygame.K_RIGHT:
                #Move right
                player.move(False)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pass
                #Don't move
                #player.velocity = 0
    #Modify x-position of player based on their input
    #Adds boundaries to the player ship so they can't go out of game window
    '''
    if playerX <= 0:
        playerX = 0
    elif playerX >= 925:
        playerX = 925
    '''
 
    player.spawn(game)
    alien.spawn(game)
    pygame.display.update()
