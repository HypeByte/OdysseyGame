import pygame
import sys
import random
from engine import bulletCollide

#A dictionary that maps differet ship file to a transformation tuple, which transforms ship coordinates to get appropriate coordinates of bullets for each different ship
bullet_map = {

    "./asset/images/player1.png" : (10, 70),
    "./asset/images/player2.png" : (20, 60),
    "./asset/images/player3.png" : (22, 56),
    "./asset/images/player4.png" : (10, 70),
    "./asset/images/enemy1.png" : (15, 70),
    "./asset/images/enemy2.png" : (25, 60),
    "./asset/images/enemy3.png" : (27, 58),
    "./asset/images/enemy4.png" : (15, 70)

}

#Iniitializes a pair of lasers/bullets based on the ship you are attaching them on
class BulletSet():

    def __init__(self, ship, screen):
        self.ship = ship
        self.x = ship.coords[0]
        if ship.shiptype == "Player":
             self.sprite = pygame.image.load("./asset/images/greenlaser.png")
             self.sprite = pygame.transform.smoothscale(self.sprite, (20, 30))
             self.bulletcoords = [ [self.x + ship.gunpos[0], 625], [self.x +  ship.gunpos[1], 625] ]
             self.velocity = -36
            
        elif ship.shiptype == "Enemy":
             self.sprite = pygame.image.load("./asset/images/redlaser.png")
             self.sprite = pygame.transform.smoothscale(self.sprite, (20, 30))
             self.bulletcoords = [ [self.x + ship.gunpos[0], ship.randY + 75], [self.x + ship.gunpos[1], ship.randY + 75] ]
             self.velocity = 18
             self.nextfire = False
        self.screen = screen
    
    def fire(self, target): #displays bullet and updates its positions to be displayed next time
        if self.ship.shiptype == "Player":
                self.screen.blit(self.sprite, self.bulletcoords[0])
                self.screen.blit(self.sprite, self.bulletcoords[1])
                self.bulletcoords[0][1]+= self.velocity
                self.bulletcoords[1][1]+= self.velocity
                if self.bulletcoords[0][1] < -30 or self.bulletcoords[1][1] < -30:
                    return True
                else:
                    return False
        
        elif self.ship.shiptype == "Enemy":
                self.screen.blit(self.sprite, self.bulletcoords[0])
                self.screen.blit(self.sprite, self.bulletcoords[1])
                self.bulletcoords[0][1]+= self.velocity
                self.bulletcoords[1][1]+= self.velocity
                if self.bulletcoords[0][1] > 750 or self.bulletcoords[1][1] > 750 or bulletCollide(self, target):
                    self.bulletcoords[1][1] = self.ship.randY + 75
                    self.bulletcoords[0][1] = self.ship.randY + 75
                
            

#Serves as a dynamic list of bullet sets so that you can appropriately spawn in and delete bullet objects
class Bullets(BulletSet):

    def __init__(self, ship):
        self.ship = ship
        self.bullets = []
    
    def last(self):
        return self.bullets[ len(self.bullets) - 1 ]
    
    def newBullet(self):
        self.bullets.append( BulletSet(self.ship, self.ship.screen) )






 #Ignore this code, it is from a previous unaffective bullet system, but some code can still be used for this new verison
    '''
    def __update(self):
        if self.host == Player:
            self.bulletcoords = [ [self.x + self.ship.gunpos[0], 625], [self.x + self.ship.gunpos[1], 625] ]
            self.trigger_state = False
        else:
            self.bulletcoords = [ [self.x + self.ship.gunpos[0], self.ship.randY + 75], [self.x + self.ship.gunpos[1], self.ship.randY + 75] ]
            self.trigget_state = False

    #Looks for if you press the up arrow key, then sets trigger state to true to prepare for the firing of the laser
    def trigger(self, event_handler):
        if event_handler.type == pygame.KEYDOWN:
            if event_handler.key == pygame.K_UP:
                self.trigger_state = True
                self.x = self.ship.coords[0]
                self.bulletcoords = [ [self.x + self.ship.gunpos[0], 625], [self.x +  self.ship.gunpos[1], 625] ]

    #Used to animate laser across screen when trigger has been activated
    def fire(self):
        if self.trigger_state == True:

            if self.host == Player:
                self.screen.blit(self.sprite, self.bulletcoords[0])
                self.screen.blit(self.sprite, self.bulletcoords[1])
                self.bulletcoords[0][1]+= self.velocity
                self.bulletcoords[1][1]+= self.velocity
                
                if self.bulletcoords[0][1] < -30 or self.bulletcoords[1][1] < -30:
                    self.__update()

            elif self.ship.state == "display":
                self.screen.blit(self.sprite, self.bulletcoords[0])
                self.screen.blit(self.sprite, self.bulletcoords[1])
                self.bulletcoords[0][1]+= self.velocity
                self.bulletcoords[1][1]+= self.velocity
                if self.bulletcoords[0][1] > 1000 or self.bulletcoords[1][1] > 1000:
                    self.__update()
'''

