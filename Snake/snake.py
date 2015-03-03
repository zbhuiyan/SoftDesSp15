import pygame
import random
import time


class DrawableSurface():
    def __init__(self, surface, rect):
        """ Initialize the drawable surface """
        self.surface = surface
        self.rect = rect

    def get_surface(self):
        """ Get the surface """
        return self.surface

    def get_rect(self):
        """ Get the rect """
        return self.rect


class Background():

    def __init__(self,width,height):
        self.image = pygame.image.load('snake_resources/images/grass.png')
        self.height = 
        self.width = 


class Snake():
    def __init__(self, pos_x, pos_y):

        self.image= pygame.draw.rect(surface, blue, (200,150,100,50))
        self.pos_x = pos_x
        self.pos_y = pos_y
