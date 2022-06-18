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
def spawnPlayer(x,y):
    game.blit(player, (x,y) )


#game loop
while rungame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False 

    spawnPlayer(playerX, playerY)
    pygame.display.update()
