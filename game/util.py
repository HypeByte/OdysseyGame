import pygame
import sys
import random 


class Element:

    def __init__(self, sprite, scale, coords):
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale)
        self.scale = scale
        self.coords = coords
        

    def spawn(self, screen):
        screen.blit(self.sprite, (self.coords[0], self.coords[1]))



class Player(Element):

 
    def __init__(self, sprite, scale, coords, velocity, delta=0):
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale)
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
        self.sprite = pygame.transform.smoothscale((pygame.image.load(random.choice(sprites))), scale)
        self.scale = scale

     def spawn(self, screen):
        screen.blit(self.sprite, (random.randint(0, 925), random.randint(0, 350)))

    
    
                    
       
        
    
        
        
                 

        

