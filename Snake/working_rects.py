import os, sys
import pygame
from pygame.locals import *
import itertools
import random
import time
    
class Snake():
    """This is our snake that will move around the screen"""
    
    def __init__(self):
        self.x = 50
        self.y = 50

        self.rect = pygame.Rect(50,50,10,10)
        self.color = ((255,255,0))

        self.x_sign = 1
        self.y_sign = 0
        
    def move_always(self):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        speed = .1
        
        
        self.x += speed*self.x_sign        
        self.y += speed*self.y_sign

        self.rect = pygame.Rect(self.x, self.y, 10,10)
      

    def change_direction(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        speed = 5

    
        if (key == K_RIGHT):
            self.x_sign = 1
            self.y_sign = 0
            print "moving right"

        elif (key == K_LEFT):
            self.x_sign = -1
            self.y_sign = 0
            
        elif (key == K_UP):
            self.x_sign = 0
            self.y_sign = -1            
            
        elif (key == K_DOWN):
            self.x_sign = 0
            self.y_sign = 1
           
        
class Food():
    def __init__(self):
        self.rect = pygame.Rect(75,80,10,10)
      
    def randomize(self):

        random_x = random.randint(0,640)
        random_y = random.randint(0,480)

        return [random_x, random_y]


class Main():
    """"""
    
    def __init__(self, width=640,height=480):
        """Initialize"""
        
        pygame.init()

        #Initialize PyGame
        self.running = True
        
        #Set the window size
        self.width = width
        self.height = height
        
        #Create the screen
        self.screen = pygame.display.set_mode((self.width,self.height))

        self.snake = Snake()
        self.food = Food()    


    def check_collision(self):
        """Check for collisions"""

        collision = self.snake.rect.colliderect(self.food)
        return collision


    def display_update(self):
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(self.snake.x, self.snake.y, 10,10))#self.snake.rect)
        pygame.draw.rect(self.screen, (0,255,0), self.food.rect)
        pygame.display.update()
        pygame.display.flip()


    def MainLoop(self):
        """This is the Main Loop of the Game"""
        
        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
        

        while self.running:
            if self.check_collision() == True:
                self.running = False
            for event in pygame.event.get():
                pygame.draw.rect(self.screen, (0,0,0), self.food.rect)
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if (event.key == K_RIGHT):
                        self.snake.change_direction(event.key)
                    elif (event.key == K_LEFT):
                        self.snake.change_direction(event.key)
                    elif (event.key == K_UP):
                        self.snake.change_direction(event.key)
                    elif (event.key == K_DOWN):
                        self.snake.change_direction(event.key)
            
            self.snake.move_always()
            self.display_update()
   
            time.sleep(0.0001)      

        pygame.quit()
            # pygame.display.flip() 

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.MainLoop()