import pygame
import sys
import random
import bulletsystem
import engine
import explosion
from explosion import *
from engine import bulletCollide
from bulletsystem import bullet_map
from bulletsystem import BulletSet
from bulletsystem import Bullets 
import globaldata
from globaldata import *
from pygame import mixer
pygame.init() 
pygame.mixer.pre_init()
playerfiresound = pygame.mixer.Sound("./asset/sound/playershoot.mp3")
explosionsound = pygame.mixer.Sound("./asset/sound/explosion.flac")
spawnsound = pygame.mixer.Sound("./asset/sound/spawnsound.wav")

#Shield mechanic function used to spawn a shield around a sprite object
def spawnShield(target, screen):
    shield = pygame.image.load("./asset/images/spr_shield.png")
    shield = pygame.transform.smoothscale(shield, (150,150))
    screen.blit(shield, (target.coords[0] - 25, target.coords[1] - 25))


#Simple element class that allows for easy initializing of surfaces and sprites
class Element:

    def __init__(self, sprite, scale, coords):
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale).convert_alpha()
        self.scale = scale
        self.coords = coords
        
    #spawn element on gui
    def spawn(self, screen):
        screen.blit(self.sprite, (self.coords[0], self.coords[1]))

                    
#Player object
class Player(Element):

    shiptype = "Player"
    def __init__(self, sprite, scale, coords, velocity, screen, target, delta=0):
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale).convert_alpha()
        self.scale = scale
        self.coords = coords
        self.velocity = velocity
        self.delta = delta 
        self.screen = screen
        self.target = target
        self.gunpos = bullet_map[sprite]
        self.bullets = Bullets(self)
        self.explosions = []
        self.triggertime = 0
        self.addbulletstate = False
        self.score = 0
        self.health = 10

    #Detects if arrow keys are pressed, then appropriately changes the delta value which is the the change in x pos for the player so that the player can move
    def input(self, event_handler):
    
        if event_handler.type == pygame.KEYDOWN:

            if event_handler.key == pygame.K_LEFT or event_handler.key == pygame.K_a:
                #Move left
                self.delta = -self.velocity

            if event_handler.key == pygame.K_RIGHT or event_handler.key == pygame.K_d:
                #Move right
                self.delta = self.velocity
            
            if event_handler.key == pygame.K_UP or event_handler.key == pygame.K_w: #Checks if the up arrow has been pressed
                self.addbulletstate = True #makes add bullet state true, meaning that it is possible to append a new bullet
               
        if event_handler.type == pygame.KEYUP: 

            if event_handler.key == pygame.K_LEFT or event_handler.key == pygame.K_RIGHT or event_handler.key == pygame.K_a or event_handler.key == pygame.K_d:
                self.delta = 0

            if event_handler.key == pygame.K_UP or event_handler.key == pygame.K_w:
                playerfiresound.play(maxtime=1000)
                self.addbulletstate = False #If the up arrow is released make the add bullet state false
            
            
    #Updates the x pos of the player with the appropriate change or delta based on input
    def move(self):
        self.coords[0]+= self.delta

    #Returns the coordinates of the player as a tuple      
    def getCords(self):
        return (self.coords[0], self.coords[1])

    #Displays the player on the screen
    def spawn(self):

        if self.coords[0] <= 0:
             self.coords[0] = 0

        elif self.coords[0] >= 900:
             self.coords[0] = 900

        self.screen.blit(self.sprite, self.getCords())
        spawnShield(self, self.screen)
        for explosion in self.explosions:
            if explosion.state == False:
                self.explosions.remove(explosion)
            else:
                explosion.explode()
                explosion.update()

    
    def shoot(self):
        for bullet in self.bullets.bullets: #Animates the bullets to shoot
            if bullet.fire(None):
                self.bullets.bullets.remove(bullet)
            else:
                for target in self.target:
                    if bulletCollide(bullet, target) and target.state == "display":
                        explosionsound.play()
                        self.score+=1
                        self.target.remove(target)
                        if self.score >= 0 and self.score <= 10:
                            self.target.append( Enemy((100,100), 10, 12) )
                        elif self.score > 10 and self.score <= 20:
                            self.target.append( Enemy((100,100), 14, 15) )
                        elif self.score > 20 and self.score <= 30:
                            self.target.append( Enemy((100,100), 25, 18) )
                        elif self.score > 30:
                            self.target.append( Enemy((100,100), 35, 24) )
                            self.velocity = 95
                        self.explosions.append( Explosion(self.screen, [target.coords[0] - 75, target.coords[1]], (250, 250)) )
                        
        
        if self.addbulletstate == True: #Prepares to add a new bullet
            if len(self.bullets.bullets) == 0:
                self.bullets.newBullet()
                self.triggertime = pygame.time.get_ticks()
                
            elif pygame.time.get_ticks() - self.triggertime > 450: #Adds a firerate for firing new bullets
                self.bullets.newBullet()
                self.triggertime = pygame.time.get_ticks()
                
          
#Enemy object
class Enemy(Element):
     shiptype = "Enemy"
     def __init__(self, scale, spawnspeed, bulletspeed):
        self.sprites = enemy_sprites
        self.screen = game
        rand = random.choice(self.sprites)
        self.sprite = pygame.transform.smoothscale(pygame.image.load(rand), scale).convert_alpha()
        self.sprite = pygame.transform.rotozoom(self.sprite, 180, 1)
        self.scale = scale
        self.state = "spawn"
        self.spawnspeed = spawnspeed
        self.bulletspeed = bulletspeed
        self.coords = [random.randint(0, 925), -300]
        self.randY = random.choice(range(self.spawnspeed, 351, self.spawnspeed))
        self.gunpos = bullet_map[rand]
        self.enemybullet = BulletSet(self, self.screen)
        self.soundrep = 0

     #Displays enemy on screen
     def spawn(self):
        if self.state == "spawn":

            if self.coords[1] < self.randY:
                while self.soundrep == 0:
                    spawnsound.play()
                    self.soundrep+=1
                self.coords[1]+= self.spawnspeed
                self.screen.blit(self.sprite, (self.coords[0], self.coords[1]))
                spawnShield(self, self.screen)

            elif self.coords[1] >= self.randY:
                self.state = "display"
                

        elif self.state == "display":
            self.screen.blit(self.sprite, ((self.coords[0], self.coords[1])))
    
     def autoshoot(self, target):
        if self.state == "display":
            self.enemybullet.fire(target, self.bulletspeed)
        

               
        

    
    
                    
       
        
    
        
        
                 

        

