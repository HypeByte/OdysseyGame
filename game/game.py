import pygame 
import random 
import sys
from util import Player
from util import Element


#Start game
pygame.init()

#Make game window called game
game = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Odyssey")
icon = pygame.image.load(".\images\gameicon.png")
pygame.display.set_icon(icon)
rungame = True

#Make game background
background = Element("./images/background.jpg", (1000, 800), (0,0))

#Initialize player
player = Player("./images/spaceship.png", (100, 100), [450, 675], 1)

#Initialize alien
alienX = random.randint(0, 925)
alienY = random.randint(0,350)
alien = Element("./images/alien.png", (75, 75), (alienX, alienY))

#game loop
while rungame:
    background.spawn(game)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
        
        player.input(event)
        
       
        
    
    player.move()
    player.spawn(game)
    alien.spawn(game)
    pygame.display.update()
