import pygame 
import random 
import sys
from pygame import mixer
from util import Enemy
from util import Player
from util import Element


pygame.init() 

#Make game window called game
game = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Odyssey")
icon = pygame.image.load("./asset/images/gameicon.png")
pygame.display.set_icon(icon)
rungame = True

#Make game background
background = Element("./asset/images/background.jpg", (1000, 800), (0,0))

#Initialize player
player = Player("./asset/images/spaceship.png", (100, 100), [450, 675], 1)

#Initialize alien
alien_sprites = ["./asset/images/enemy1.png",
                 "./asset/images/enemy2.png",
                 "./asset/images/enemy3.png",
                 "./asset/images/enemy4.png"]
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
