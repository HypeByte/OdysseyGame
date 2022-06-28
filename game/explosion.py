import pygame
import os
import sys
from pygame import mixer



#Loading in all the sprites of the explosion for our animation frames
explosion1 = pygame.image.load("./asset/images/explosion/explosion1.png")
explosion2 = pygame.image.load("./asset/images/explosion/explosion2.png")                               
explosion3 = pygame.image.load("./asset/images/explosion/explosion3.png")                             
explosion4 = pygame.image.load("./asset/images/explosion/explosion4.png")                              
explosion5 = pygame.image.load("./asset/images/explosion/explosion5.png")                              
explosion6 = pygame.image.load("./asset/images/explosion/explosion6.png")                             
explosion7 = pygame.image.load("./asset/images/explosion/explosion7.png")                              
explosion8 = pygame.image.load("./asset/images/explosion/explosion8.png")                              
explosion9 = pygame.image.load("./asset/images/explosion/explosion9.png")                             
explosion10 = pygame.image.load("./asset/images/explosion/explosion10.png")                              

#Object used to initialize and target explosions
class Explosion:

    def __init__(self, screen, coords, size):
        self.screen = screen
        self.coords = coords
        self.size = size
        self.animation = [explosion1,
                          explosion2,
                          explosion3,
                          explosion4,
                          explosion5,
                          explosion6,
                          explosion7,
                          explosion8,
                          explosion9,
                          explosion10]
        for i in range(len(self.animation)):
            self.animation[i] = pygame.transform.smoothscale(self.animation[i], self.size)
        self.frame = 0
        self.image = self.animation[int(self.frame)]
        self.state = True

    #Updates to the next animation frame, animation frame swith to frame ratio: 1 : 2
    def update(self, speed=.5):
        if int(self.frame + speed) < len(self.animation) and self.state == True:
            self.frame+=speed
            self.image = self.animation[int(self.frame)]
        
        else:
            self.state = False

    #Displays a frame of the explosion
    def explode(self):
        if self.state == True:
            self.screen.blit(self.image, self.coords)
        
