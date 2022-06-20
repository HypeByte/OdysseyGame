import this
import pygame
import sys


class element:

    def __init__(self, sprite, scale, coords, velocity):
        self.sprite = pygame.image.load(sprite)
        self.scale = scale
        self.coords = coords
        self.velocity = velocity
    
    def spawn(self, screen):
        screen.blit(self.sprite, self.coords)
        

