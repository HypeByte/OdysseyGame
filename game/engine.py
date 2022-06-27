import pygame
import bulletsystem
import globaldata
import sys
import os

def bulletCollide(projectile, target):

    if projectile.bulletcoords[0][0] > target.coords[0] and projectile.bulletcoords[0][0] < target.coords[0] + target.scale[0] or projectile.bulletcoords[1][0] > target.coords[0] and projectile.bulletcoords[1][0] < target.coords[0] + target.scale[0]: 
        if projectile.bulletcoords[0][1] > target.coords[1] and projectile.bulletcoords[0][1] < target.coords[1] + target.scale[1] or projectile.bulletcoords[1][1] > target.coords[1] and projectile.bulletcoords[1][1] < target.coords[1] + target.scale[1]:
            return True

def mouseCollide(x, y, button):

    if x > button.coords[0] and x < button.coords[0] + button.scale[0] and y > button.coords[1] and y < button.coords[1] + button.scale[1]:
        return True

def displayText(text, font, screen, x, y, color):
    display = font.render(text, True, color)
    screen.blit(display, (x, y))
