import pygame
import sys


class element:

    def __init__(self, sprite, scale, coords, velocity):
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale)
        self.scale = scale
        self.coords = coords
        self.velocity = velocity
        

    def spawn(self, screen):
        screen.blit(self.sprite, self.coords)

    def move(self, direct):
        self.coords[0]+= -(self.velocity) if direct == True else self.velocity
        

