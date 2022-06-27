import pygame 
import random 
import sys
from pygame import K_DOWN, mixer
from explosion import Explosion
from blueprints import Element
from blueprints import Enemy
from blueprints import Player
import bulletsystem
import globaldata
from globaldata import *



#Start game
pygame.init() 
clock = pygame.time.Clock()

#Make game window called game
game = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Odyssey")
icon = pygame.image.load("./asset/images/gameicon.png")
pygame.display.set_icon(icon)
rungame = True

#Making the space border
border = Element("./asset/images/border.png", (1150, 150), (-50, 650))


#Make game background
background = Element("./asset/images/background.jpg", (1000, 800), (0,0))
bomb = Explosion(game, (450, 400), (300, 300))

#Initialize player
player_sprites = ["./asset/images/player1.png",
                  "./asset/images/player2.png",
                  "./asset/images/player3.png",
                  "./asset/images/player4.png" ]



#Initialize aliens or the enemy ships
alien = Enemy((100, 100))
alien2 = Enemy((100, 100))
alien3 = Enemy((100, 100))
enemies = [alien, alien2, alien3]
player = Player(player_sprites[3], (100, 100), [450, 625], 70, game, enemies)
alien.target = player
alien2.target = player
alien3.target = player





#game loop
while rungame:
    clock.tick(20) #Caps the fps to 30 so that there is no fps lag or display lag
    background.spawn(game)

    #Input scan loop   
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Exit window of x button is pressed
            rungame = False
    
        #Our input scan functions that take in event as the event_handler       
        player.input(event)
        
    bomb.explode()   
    border.spawn(game)
    player.move()
    player.spawn()
    player.shoot()
    for enemy in player.target:
        enemy.spawn()
        enemy.autoshoot(player)
       
    pygame.display.update()
    
   
