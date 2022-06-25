import pygame
import sys
import random
import bulletsystem
from bulletsystem import bullet_map
from bulletsystem import BulletSet
from bulletsystem import Bullets 


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
    def __init__(self, sprite, scale, coords, velocity, screen, delta=0):
        
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale).convert_alpha()
        self.scale = scale
        self.coords = coords
        self.velocity = velocity
        self.delta = delta 
        self.screen = screen
        self.gunpos = bullet_map[sprite]
        self.laser = Bullets(self)
        self.firerate = 0

    #Detects if arrow keys are pressed, then appropriately changes the delta value which is the the change in x pos for the player so that the player can move
    def input(self, event_handler):
    
        if event_handler.type == pygame.KEYDOWN:

            if event_handler.key == pygame.K_LEFT:
                #Move left
                self.delta = -self.velocity

            if event_handler.key == pygame.K_RIGHT:
                #Move right
                self.delta = self.velocity
            
            if event_handler.key == pygame.K_UP: 
                #shot has been fired
                if len(self.laser.bullets) == 0:
                    self.laser.newBullet()
                    self.firerate = pygame.time.get_ticks()
                
                elif pygame.time.get_ticks() - self.firerate > 100:
                    self.laser.newBullet()
                    self.firerate = pygame.time.get_ticks()
                
                else:
                    print("Firerate test")

        if event_handler.type == pygame.KEYUP:

            if event_handler.key == pygame.K_LEFT or event_handler.key == pygame.K_RIGHT:
                    self.delta = 0

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

    def shoot(self):
         for bullet in self.laser.bullets:
             bullet.fire()

#Enemy object
class Enemy(Element):

     shiptype = "Enemy"
     def __init__(self, sprites, scale, screen):
        rand = random.choice(sprites)
        self.sprite = pygame.transform.smoothscale(pygame.image.load(rand), scale).convert_alpha()
        self.sprite = pygame.transform.rotozoom(self.sprite, 180, 1)
        self.scale = scale
        self.screen = screen
        self.state = "spawn"
        self.coords = [random.randint(0, 925), -300]
        self.randY = random.choice(range(0, 351, 10))
        self.gunpos = bullet_map[rand]

     #Displays enemy on screen
     def spawn(self):
        if self.state == "spawn":

            if self.coords[1] < self.randY:
                self.coords[1]+= 10
                self.screen.blit(self.sprite, (self.coords[0], self.coords[1]))
                spawnShield(self, self.screen)
            elif self.coords[1] == self.randY:
                self.state = "display"
                

        elif self.state == "display":
            self.screen.blit(self.sprite, ((self.coords[0], self.coords[1])))
        

    
    
                    
       
        
    
        
        
                 

        

