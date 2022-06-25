from asyncio.windows_events import NULL
import pygame
import sys
import random 

'''
 A dictionary used to match different player and enemy ships
 to the appropriate transformation tuple, which is added to the laser
 coordinates so that the laser is positioned perfectly
'''
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

#Iniitializes a pair of lasers/bullets based on the ship you are attaching them on
class BulletSet(Element):

    def __init__(self, ship, screen):
        self.ship = ship
        self.x = ship.coords[0]
        if type(ship) == Player:
             self.host = Player
             self.sprite = pygame.image.load("./asset/images/greenlaser.png")
             self.sprite = pygame.transform.smoothscale(self.sprite, (20, 30))
             self.bulletcoords = [ [self.x + ship.gunpos[0], 625], [self.x +  ship.gunpos[1], 625] ]
             self.velocity = -9
            
        elif type(ship) == Enemy:
             self.host = Enemy
             self.sprite = pygame.image.load("./asset/images/redlaser.png")
             self.sprite = pygame.transform.smoothscale(self.sprite, (20, 30))
             self.bulletcoords = [ [self.x + ship.gunpos[0], ship.randY + 75], [self.x + ship.gunpos[1], ship.randY + 75] ]
             self.velocity = 9
        self.screen = screen

 
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

#Serves as a dynamic list of bullet sets so that you can appropriately spawn in and delete bullet objects
class Bullets:

    def __init__(self, ship):
        self.ship = ship
        self.bullets = []
    
    def last(self):
        return self.bullets[ len(self.bullets) - 1 ]
    
    def newBullet(self):
        self.bullets.append( BulletSet(self.ship, self.ship.screen) )

    def shoot(self):
        for bullet in self.bullets:
             self.screen.blit(self.sprite, self.bulletcoords[0])
             self.screen.blit(self.sprite, self.bulletcoords[1])
             self.bulletcoords[0][1]+= self.velocity
             self.bulletcoords[1][1]+= self.velocity
    



    

    

                    
#Player object
class Player(Element):

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
                if len(self.laser) == 0:
                    self.laser.newBullet()
                    self.firerate = pygame.time.get_ticks()
                
                elif pygame.time.get_ticks() - self.firerate > 1000:
                    self.laser.newBullet()

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

#Enemy object
class Enemy(Element):

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
        

    
    
                    
       
        
    
        
        
                 

        

