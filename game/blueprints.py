import pygame
import sys
import random 


class Element:

    def __init__(self, sprite, scale, coords):
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale).convert_alpha()
        self.scale = scale
        self.coords = coords
        

    def spawn(self, screen):
        screen.blit(self.sprite, (self.coords[0], self.coords[1]))

def spawnShield(target, screen):
    shield = pygame.image.load("./asset/images/spr_shield.png")
    shield = pygame.transform.smoothscale(shield, (150,150))
    screen.blit(shield, (target.coords[0] - 25, target.coords[1] - 25))


class Player(Element):

    def __init__(self, sprite, scale, coords, velocity, delta=0):
        
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale).convert_alpha()
        self.scale = scale
        self.coords = coords
        self.velocity = velocity
        self.delta = delta 

    def input(self, event_handler):
    
        if event_handler.type == pygame.KEYDOWN:

            if event_handler.key == pygame.K_LEFT:
                    #Move left
                    self.delta = -self.velocity

            if event_handler.key == pygame.K_RIGHT:
                    #Move right
                    self.delta = self.velocity
            
        if event_handler.type == pygame.KEYUP:

            if event_handler.key == pygame.K_LEFT or event_handler.key == pygame.K_RIGHT:
                    self.delta = 0

    def move(self):
        self.coords[0]+= self.delta
        
    def getCords(self):
        return (self.coords[0], self.coords[1])

    def spawn(self, screen):

        if self.coords[0] <= 0:
             self.coords[0] = 0

        elif self.coords[0] >= 900:
             self.coords[0] = 900

        screen.blit(self.sprite, self.getCords())

class Enemy(Element):

     def __init__(self, sprites, scale):
        self.sprite = pygame.transform.smoothscale((pygame.image.load(random.choice(sprites))), scale).convert_alpha()
        self.sprite = pygame.transform.rotozoom(self.sprite, 180, 1)
        self.scale = scale
        self.state = "spawn"
        self.coords = [random.randint(0, 925), -300]
        self.randY = random.choice(range(0, 351, 10))

     def spawn(self, screen):
        
        if self.state == "spawn":

            if self.coords[1] < self.randY:
                self.coords[1]+= 10
                screen.blit(self.sprite, (self.coords[0], self.coords[1]))
                spawnShield(self, screen)
            elif self.coords[1] == self.randY:
                self.state = "display"
                

        elif self.state == "display":
            screen.blit(self.sprite, ((self.coords[0], self.coords[1])))
        

    
    
                    
       
        
    
        
        
                 

        

