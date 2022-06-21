import pygame 
import random 
import sys
from util import Enemy
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
alien_sprites = ["./images/Faction5-Spaceships-by-MillionthVector/F5S1.png", 
                 "./images/Faction5-Spaceships-by-MillionthVector/F5S2.png",
                 "./images/Faction5-Spaceships-by-MillionthVector/F5S3.png",
                 "./images/Faction5-Spaceships-by-MillionthVector/F5S4.png"]
alien = Enemy(alien_sprites, (100, 100))

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
