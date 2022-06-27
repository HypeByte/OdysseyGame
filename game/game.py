import pygame 
import random 
import sys
from explosion import Explosion
from blueprints import Element
from blueprints import Enemy
from blueprints import Player
from blueprints import engine
from engine import mouseCollide
from engine import displayText
import bulletsystem
import globaldata
from globaldata import *



#Start game
pygame.init() 
clock = pygame.time.Clock()

def menugui():
    menu = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Odyssy Menu")
    menu_background = Element("./asset/images/menu.png", (1000, 800), (0, 0))
    play_button = Element("./asset/images/playbutton.png", (185, 185), (125, 475))
    controls_button = Element("./asset/images/controls.png", (185, 185), (375, 475))
    profile_button = Element("./asset/images/profile.png", (185, 185), (625, 475))
    runmenu = True

    while runmenu:
        menu_background.spawn(menu)
        mouseX, mouseY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Exit window of x button is pressed
                runmenu = False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseCollide(mouseX, mouseY, play_button):
                    charactergui()
                    runmenu = False

        play_button.spawn(menu)
        controls_button.spawn(menu)
        profile_button.spawn(menu)
        pygame.display.update()


def charactergui():
    characterscreen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Characters Screen")
    characterscreen_background = Element("./asset/images/characterscreen.jpg", (1000, 800), (0, 0))
    opt1 = Element("./asset/images/player1.png", (150, 150), (50, 400))
    opt2 = Element("./asset/images/player2.png", (150, 150), (295, 400))
    opt3 = Element("./asset/images/player3.png", (150, 150), (535, 400))
    opt4 = Element("./asset/images/player4.png", (150, 150), (790, 400))
    runcharscreen = True

    while runcharscreen:
        characterscreen_background.spawn(characterscreen)
        mouseX, mouseY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Exit window of x button is pressed
                runcharscreen = False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if mouseCollide(mouseX, mouseY, opt1):
                    runcharscreen = False
                    gamegui(0)
                elif mouseCollide(mouseX, mouseY, opt2):
                    runcharscreen = False
                    gamegui(1)
                elif mouseCollide(mouseX, mouseY, opt3):
                    runcharscreen = False
                    gamegui(2)
                elif mouseCollide(mouseX, mouseY, opt4):
                    runcharscreen = False
                    gamegui(3)


        opt1.spawn(characterscreen)
        opt2.spawn(characterscreen)
        opt3.spawn(characterscreen)
        opt4.spawn(characterscreen)
        pygame.display.update()
    


def gamegui(option):
    #Make game window called game
    game = pygame.display.set_mode((1000,800))
    pygame.display.set_caption("Odyssey")
    icon = pygame.image.load("./asset/images/gameicon.png")
    pygame.display.set_icon(icon)
    rungame = True

    #Making the space border
    border = Element("./asset/images/border.png", (1150, 150), (-50, 650))
    font = pygame.font.Font("./asset/fonts/Transformers.ttf", 32)

    #Make game background
    background = Element("./asset/images/background.jpg", (1000, 800), (0,0))
    bomb = Explosion(game, (450, 400), (300, 300))

    #Initialize player
    player_sprites = ["./asset/images/player1.png",
                    "./asset/images/player2.png",
                    "./asset/images/player3.png",
                    "./asset/images/player4.png" ]


    #Initialize aliens or the enemy ships
    alien = Enemy((100, 100))
    alien2 = Enemy((100, 100))
    alien3 = Enemy((100, 100))
    enemies = [alien, alien2, alien3]
    player = Player(player_sprites[option], (100, 100), [450, 625], 70, game, enemies)
    alien.target = player
    alien2.target = player
    alien3.target = player
    #game loop
    while rungame:
        clock.tick(20) #Caps the fps to 30 so that there is no fps lag or display lag
        background.spawn(game)

        #Input scan loop   
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Exit window of x button is pressed
                rungame = False
                sys.exit()
        
            #Our input scan functions that take in event as the event_handler       
            player.input(event)
            
        bomb.explode()   
        border.spawn(game)
        player.move()
        player.spawn()
        player.shoot()
        for enemy in player.target:
            enemy.spawn()
            enemy.autoshoot(player)

        displayText("Score: " + str(player.score), font, game, 30, 760, (126, 187, 222))
        displayText("Health: " + str(player.health), font, game, 300, 760, (245, 76, 79))
        pygame.display.update()

menugui()
    
   
