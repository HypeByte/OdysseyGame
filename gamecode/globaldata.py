import pygame
import json

game = pygame.display.set_mode((1000,800))

enemy_sprites = ["./asset/images/enemy1.png",
                 "./asset/images/enemy2.png",
                 "./asset/images/enemy3.png",
                 "./asset/images/enemy4.png"]

player_sprites = ["./asset/images/player1.png",
                  "./asset/images/player2.png",
                  "./asset/images/player3.png",
                  "./asset/images/player4.png" ]

Screen_size = (1000, 800)
origin = (0, 0)

user_data = {
    "highscore" : '0'
}  


