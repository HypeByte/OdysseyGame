import pygame 
import random 
import sys
from pygame import mixer
from util import Enemy
from util import Player
from util import Element


pygame.init() 
clock = pygame.time.Clock()
#Make game window called game
game = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Odyssey")
icon = pygame.image.load("./asset/images/gameicon.png")
pygame.display.set_icon(icon)
rungame = True

#Making space base
border = Element("./asset/images/border.png", (1150, 150), (-50, 650))



#Make game background
background = Element("./asset/images/background.jpg", (1000, 800), (0,0))

#Initialize player
player_sprites = ["./asset/images/player1.png",
                  "./asset/images/player2.png",
                  "./asset/images/player3.png",
                  "./asset/images/player4.png" ]
player = Player(player_sprites[3], (100, 100), [450, 625], 20)

#Initialize alien
alien_sprites = ["./asset/images/enemy1.png",
                 "./asset/images/enemy2.png",
                 "./asset/images/enemy3.png",
                 "./asset/images/enemy4.png"]
alien = Enemy(alien_sprites, (100, 100))
alien2 = Enemy(alien_sprites, (100, 100))

#game loop
while rungame:
    clock.tick(30)
    background.spawn(game)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
        
        player.input(event)
        
       
        
    border.spawn(game)
    player.move()
    player.spawn(game)
    alien.spawn(game)
    alien2.spawn(game)
    pygame.display.update()
   
