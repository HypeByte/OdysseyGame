import pygame 
import sys 

#Start game
pygame.init()

#Make game window called game
game = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Odyssey")
icon = pygame.image.load(".\images\gameicon.png")
pygame.display.set_icon(icon)
rungame = True

#Initialize player
player = pygame.image.load("./images/spaceship.png")
player = pygame.transform.scale(player, (100, 100))
playerX = 450
playerY = 600
playerSpeed = 0
def spawnPlayer(x,y):
    game.blit(player, (x,y) )


#game loop
while rungame:
    game.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
        
        #Add x-axis movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #Move left
                playerSpeed = -0.7
            if event.key == pygame.K_RIGHT:
                #Move right
                playerSpeed = 0.7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #Don't move
                playerSpeed = 0
    #Modify x-position of player based on their input
    playerX+= playerSpeed
    #Adds boundaries to the player ship so they can't go out of game window
    if playerX <= 0:
        playerX = 0
    elif playerX >= 900:
        playerX = 900
 
    spawnPlayer(playerX, playerY)
    pygame.display.update()
