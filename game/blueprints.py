import pygame
import sys
import random 

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


class BulletSet(Element):

    def __init__(self, ship, screen):
        self.ship = ship
        if type(ship) == Player:
             self.host = Player
             self.sprite = pygame.image.load("./asset/images/greenlaser.png")
             self.sprite = pygame.transform.smoothscale(self.sprite, (20, 30))
             self.bulletcoords = [ (ship.coords[0] + ship.gunpos[0], 625), (ship.coords[0] +  ship.gunpos[1], 625) ]
             self.direct = 1
            
        elif type(ship) == Enemy:
             self.host = Enemy
             self.sprite = pygame.image.load("./asset/images/redlaser.png")
             self.sprite = pygame.transform.smoothscale(self.sprite, (20, 30))
             self.bulletcoords = [ (ship.coords[0] + ship.gunpos[0], ship.randY + 75), (ship.coords[0] + ship.gunpos[1], ship.randY + 75) ]
             self.direct = -1
        self.screen = screen

    def display(self):
        self.screen.blit(self.sprite, self.bulletcoords[0])
        self.screen.blit(self.sprite, self.bulletcoords[1])

    def enemydisplay(self):
        if self.ship.state == "display":
            self.screen.blit(self.sprite, self.bulletcoords[0])
            self.screen.blit(self.sprite, self.bulletcoords[1])



class Player(Element):

    def __init__(self, sprite, scale, coords, velocity, delta=0):
        
        self.sprite = pygame.transform.smoothscale((pygame.image.load(sprite)), scale).convert_alpha()
        self.scale = scale
        self.coords = coords
        self.velocity = velocity
        self.delta = delta 
        self.gunpos = bullet_map[sprite]

    def input_movement(self, event_handler):
    
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
        rand = random.choice(sprites)
        self.sprite = pygame.transform.smoothscale(pygame.image.load(rand), scale).convert_alpha()
        self.sprite = pygame.transform.rotozoom(self.sprite, 180, 1)
        self.scale = scale
        self.state = "spawn"
        self.coords = [random.randint(0, 925), -300]
        self.randY = random.choice(range(0, 351, 10))
        self.gunpos = bullet_map[rand]

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
        

    
    
                    
       
        
    
        
        
                 

        

