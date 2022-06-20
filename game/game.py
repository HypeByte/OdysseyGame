import pygame 
import random 
import sys
from util import player
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
background = element("./images/background.jpg", (1000, 800), (0,0))

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
Player = player("./images/spaceship.png", (75,75), [450, 675], 1)

#Initialize alien
alienX = random.randint(0, 925)
alienY = random.randint(0,350)
alien = element("./images/alien.png", (75, 75), (alienX, alienY))

#game loop
while rungame:
    background.spawn(game)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            rungame = False
        
        Player.xmove(event)
        
    
 
    Player.spawn(game)
    alien.spawn(game)
    pygame.display.update()
