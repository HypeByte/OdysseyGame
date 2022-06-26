import pygame
import bulletsystem
import sys
import os

def bulletCollide(projectile, target):

    if projectile.bulletcoords[0][0] > target.coords[0] and projectile.bulletcoords[0][0] < target.coords[0] + target.scale[0] or projectile.bulletcoords[1][0] > target.coords[0] and projectile.bulletcoords[1][0] < target.coords[0] + target.scale[0]: 
        if projectile.bulletcoords[0][1] > target.coords[1] and projectile.bulletcoords[0][1] < target.coords[1] + target.scale[1] or projectile.bulletcoords[1][1] > target.coords[1] and projectile.bulletcoords[1][1] < target.coords[1] + target.scale[1]:
            return True