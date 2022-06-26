import pygame 
import random 
import sys
from pygame import K_DOWN, mixer
from explosion import Explosion
from blueprints import Element
from blueprints import Enemy
from blueprints import Player
import bulletsystem



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
alien_sprites = ["./asset/images/enemy1.png",
                 "./asset/images/enemy2.png",
                 "./asset/images/enemy3.png",
                 "./asset/images/enemy4.png"]
alien = Enemy(alien_sprites, (100, 100), game)
alien2 = Enemy(alien_sprites, (100, 100), game)
alien3 = Enemy(alien_sprites, (100, 100), game)
player = Player(player_sprites[3], (100, 100), [450, 625], 40, game, alien)





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
    alien.spawn()
    alien2.spawn()
    alien3.spawn()
    player.shoot()
    alien.autoshoot()
    alien2.autoshoot()
    alien3.autoshoot()
    pygame.display.update()
    
   
