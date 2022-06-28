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

try:
    with open("./asset/userdata.txt") as data:
        user_data = json.load(data)
except:
    with open("./asset/userdata.txt", 'w') as data:
        json.dump(user_data, data)

def menugui():
 
    menu = pygame.display.set_mode(Screen_size)
    pygame.display.set_caption("Odyssy Menu")
    menu_background = Element("./asset/images/menu.png", Screen_size, origin)
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
                    charactergui("menu")
                    runmenu = False
                
                if mouseCollide(mouseX, mouseY, controls_button):
                    guidegui()
                    runmenu = False
                
                if mouseCollide(mouseX, mouseY, profile_button):
                    profilegui()
                    runmenu = False

        play_button.spawn(menu)
        controls_button.spawn(menu)
        profile_button.spawn(menu)
        pygame.display.update()

def guidegui():
    guidescreen = pygame.display.set_mode(Screen_size)
    pygame.display.set_caption("How to play")
    guidebackground = Element("./asset/images/guidescreen.jpg", (1000, 800), (0, 0))
    backbutton = Element("./asset/images/backbutton.png", (100, 100), (0,0))
    runguide = True

    while runguide:
        guidebackground.spawn(guidescreen)
        mouseX, mouseY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Exit window of x button is pressed
                runguide = False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseCollide(mouseX, mouseY, backbutton):
                    menugui()
                    runguide = False

        backbutton.spawn(guidescreen)
        pygame.display.update()

def profilegui():
    profilescreen = pygame.display.set_mode(Screen_size)
    pygame.display.set_caption("Your Profile")
    profilebackground = Element("./asset/images/profilescreen.png", (1000, 800), origin)
    backbutton = Element("./asset/images/backbutton.png", (100, 100), (0,0))
    font = pygame.font.Font("./asset/fonts/Transformers.ttf", 72)
    runprofile = True

    while runprofile:
        profilebackground.spawn(profilescreen)
        mouseX, mouseY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Exit window of x button is pressed
                runprofile = False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseCollide(mouseX, mouseY, backbutton):
                    menugui()
                    runcharscreen = False
                        
        displayText("Highest Score: " + str(user_data["highscore"]), font, profilescreen, 200, 250, (255,255,255))               
        backbutton.spawn(profilescreen)
        pygame.display.update()







def charactergui(previous):
    characterscreen = pygame.display.set_mode(Screen_size)
    pygame.display.set_caption("Characters Screen")
    characterscreen_background = Element("./asset/images/characterscreen.jpg", Screen_size, origin)
    opt1 = Element("./asset/images/player1.png", (150, 150), (50, 400))
    opt2 = Element("./asset/images/player2.png", (150, 150), (295, 400))
    opt3 = Element("./asset/images/player3.png", (150, 150), (535, 400))
    opt4 = Element("./asset/images/player4.png", (150, 150), (790, 400))
    backbutton = Element("./asset/images/backbutton.png", (100, 100), (0,0))
    runcharscreen = True

    while runcharscreen:
        characterscreen_background.spawn(characterscreen)
        mouseX, mouseY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Exit window of x button is pressed
                runcharscreen = False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if mouseCollide(mouseX, mouseY, backbutton):
                    runcharscreen = False
                    if previous == "menu":
                        menugui()
                    elif previous == "loss":
                        losegui()
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

        backbutton.spawn(characterscreen)
        opt1.spawn(characterscreen)
        opt2.spawn(characterscreen)
        opt3.spawn(characterscreen)
        opt4.spawn(characterscreen)
        pygame.display.update()

def highscoregui():
    highscorescreen = pygame.display.set_mode(Screen_size)
    pygame.display.set_caption("Highscore!")
    highscorebackground = Element("./asset/images/highscore.jpg", Screen_size, origin)
    menubutton = Element("./asset/images/menubutton.png", (185, 185), (125, 600))
    screenshotbutton = Element("./asset/images/screenshot.png", (185, 185), (375, 600))
    redobutton = Element("./asset/images/redobutton.png", (185, 185), (625, 600))

def losegui(score):
    losingscreen = pygame.display.set_mode(Screen_size)
    pygame.display.set_caption("You Lost!")
    losingbackground = Element("./asset/images/losingscreen.jpg", Screen_size, origin)
    runlose = True
    font = pygame.font.Font("./asset/fonts/Transformers.ttf", 100)
    menubutton = Element("./asset/images/menubutton.png", (185, 185), (300, 500))
    redobutton = Element("./asset/images/redobutton.png", (185, 185), (515, 500))

    while runlose:
        losingbackground.spawn(losingscreen)
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Exit window of x button is pressed
                runlose = False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseCollide(mouseX, mouseY, menubutton):
                    menugui()
                    runlose = False
                
                elif mouseCollide(mouseX, mouseY, redobutton):
                    charactergui("loss")
                    runlose = False
            
        menubutton.spawn(losingscreen)   
        redobutton.spawn(losingscreen)
        displayText("Your Score: " + str(score), font, losingscreen, 200, 300, (224, 63, 74))
        displayText("High Score: " + str(user_data["highscore"]), font, losingscreen, 200, 425, (227, 190, 57))
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
    base_explosions = [Explosion(game, (15, 650), (100, 100)),
                       Explosion(game, (115, 650), (100, 100)),
                       Explosion(game, (225, 650), (100, 100)),
                       Explosion(game, (335, 650), (100, 100)),
                       Explosion(game, (445, 650), (100, 100)),
                       Explosion(game, (555, 650), (100, 100)),
                       Explosion(game, (655, 650), (100, 100)),
                       Explosion(game, (755, 650), (100, 100)),
                       Explosion(game, (855, 650), (100, 100)),
                       Explosion(game, (955, 650), (100, 100)),
                                                             ]

    #Make game background
    background = Element("./asset/images/background.jpg", Screen_size, (0,0))
    bomb = Explosion(game, (450, 400), (300, 300))

    #Initialize player
    player_sprites = ["./asset/images/player1.png",
                    "./asset/images/player2.png",
                    "./asset/images/player3.png",
                    "./asset/images/player4.png" ]


    #Initialize aliens or the enemy ships
    alien = Enemy((100, 100), 10, 12)
    alien2 = Enemy((100, 100), 10, 12)
    alien3 = Enemy((100, 100), 10, 12)
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
                if player.score > user_data["highscore"]:
                    user_data["highscore"] = player.score
                    with open("./asset/userdata.txt", 'w') as data:
                        json.dump(user_data, data)
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

        if player.health == 0:
            while base_explosions[len(base_explosions) - 1].state:
                for explosion in base_explosions:
                    explosion.explode()
                    explosion.update(speed=.1)
                    pygame.display.update()
            if player.score > user_data["highscore"]:
                    user_data["highscore"] = player.score
                    with open("./asset/userdata.txt", 'w') as data:
                        json.dump(user_data, data)
            losegui(player.score)
            rungame = False

        pygame.display.update()

menugui()
   
