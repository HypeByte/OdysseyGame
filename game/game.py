import pygame 
import random 
import sys 

#Start game
pygame.init()

#Make game window called game
game = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Odyssey")
icon = pygame.image.load(".\images\gameicon.png")
pygame.display.set_icon(icon)
rungame = True

#Make game background
background = pygame.image.load("./images/background.jpg")
background = pygame.transform.smoothscale(background, (1000,800))

#Initialize player
player = pygame.image.load("./images/spaceship.png")
player = pygame.transform.smoothscale(player, (75, 75))
playerX = 450
playerY = 675
playerSpeed = 0
def spawnPlayer(x,y):
    game.blit(player, (x,y) )

#Initialize alien
alien = pygame.image.load("./images/alien.png")
alien = pygame.transform.smoothscale(alien, (75, 75))
alienX = random.randint(0, 925)
alienY = random.randint(0,350)
alienSpeed = 0
def spawnAlien(x,y):
    game.blit(alien, (x,y) )



#game loop
while rungame:
    game.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
        
        #Add x-axis movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #Move left
                playerSpeed = -1
            if event.key == pygame.K_RIGHT:
                #Move right
                playerSpeed = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #Don't move
                playerSpeed = 0
    #Modify x-position of player based on their input
    playerX+= playerSpeed
    #Adds boundaries to the player ship so they can't go out of game window
    if playerX <= 0:
        playerX = 0
    elif playerX >= 925:
        playerX = 925
 
    spawnPlayer(playerX, playerY)
    spawnAlien(alienX, alienY)
    pygame.display.update()
