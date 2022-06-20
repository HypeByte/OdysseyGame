import pygame
import sys


class element:

    def __init__(self, sprite, scale, coords):
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale)
        self.scale = scale
        self.coords = coords
        

    def spawn(self, screen):
        screen.blit(self.sprite, self.coords)



class player(element):

    def __init__(self, sprite, scale, coords, velocity):
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale)
        self.scale = scale
        self.coords = coords
        self.velocity = velocity 

    def xmove(self, event_handler):
        if event_handler.type == pygame.KEYDOWN:

            if event_handler.key == pygame.K_LEFT:
                #Move left
                self.coords[0]+= self.velocity

            if event_handler.key == pygame.K_RIGHT:
                #Move right
                self.coords[0]+= self.velocity
        
        if event_handler.type == pygame.KEYUP:

            if event_handler.key == pygame.K_LEFT or event_handler.key == pygame.K_RIGHT:
                self.coords[0]+= 0
    
        if self.coords[0] <= 0:
             self.coords[0] = 0

        elif self.coords[0] >= 925:
             self.coords[0] = 925
                 

        

