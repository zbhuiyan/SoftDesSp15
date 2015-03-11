import os, sys
import pygame
from pygame.locals import *
from helpers import *
import itertools
import random
import time
    
class Snake(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.rect = pygame.Rect(50,50,10,10)
    
        """Set the number of Pixels to move each time"""
        self.x_dist = 1
        self.y_dist = 1

        self.xMove = 0
        self.yMove = 0
        self.direction = 0
        self.name = "fred"

        
    def move_always(self, direction):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        speed = .2 
        
        if direction == 0:
            xMove = 0
            yMove = -self.y_dist * speed
        if direction == 1:
            yMove = 0
            xMove = self.x_dist * speed
        if direction == 2:
            xMove = 0
            yMove = self.y_dist * speed
        if direction == 3:
            yMove = 0
            xMove = -self.x_dist * speed
    
        self.rect = self.rect.move(self.xMove,self.yMove)
        self.rect.move(self.xMove,self.yMove)


    def move_key_down(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        speed = 5
    
        if (key == K_RIGHT):
            #if direction !=3 or direction !=2 or direction !=0:
            self.yMove = 0
            self.xMove = self.x_dist * speed
            self.direction = 1


        elif (key == K_LEFT):
            #if direction !=1 or direction !=0 or direction !=2:
            self.yMove = 0
            self.xMove = -self.x_dist * speed
            self.direction = 3
        
        elif (key == K_UP):
            #if direction != 0 or direction !=1 or direction !=3:
            self.xMove = 0
            self.yMove = -self.y_dist * speed
            self.direction = 2
            
        elif (key == K_DOWN):
            #if direction !=1 or direction !=2 or direction !=3:
            self.xMove = 0
            self.yMove = self.y_dist *+ speed
            self.direction = 0

        self.rect = self.rect.move(self.xMove,self.yMove)
        self.rect.move(self.xMove,self.yMove)
        
        
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(75,80,10,10)
        



    def randomize(self):
        
        qty = 1  # or however many points you want
# Generate a set of all points within 200 of the origin, to be used as offsets later
# There's probably a more efficient way to do this.
        random_x = random.randint(0,640)
        random_y = random.randint(0,480)

    
        return [random_x, random_y]
        

#             x = random.randrange(*rangeX)
#             y = random.randrange(*rangeY)
#             if (x,y) in excluded: continue
#             randPoints.append((x,y))
#             i += 1
#             excluded.update((x+dx, y+dy) for (dx,dy) in deltas)
#         print randPoints

class Main():
    """"""
    
    def __init__(self, width=640,height=480):
        """Initialize"""
        
        #Initialize PyGame
        pygame.init()
        self.running = True
        
        #Set the window size
        self.width = width
        self.height = height
        
        #Create the screen
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
    

    def LoadSprites(self):
        """Load the sprites that we need"""
        
        self.snake = Snake()
        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
        self.food = Food()
        self.food_sprites = pygame.sprite.RenderPlain((self.food))                 


    # def setup_background(self):
    #     self.screen.fill((0,0,0))
    #     self.screen.blit(self.background,(0,0))
    #     background_width, background_height = self.background.get_width(), self.background.get_height()
    #     for x,y in itertools.product(range(0,self.width,background_width),
    #                                  range(0,self.height,background_height)):
    #         self.screen.blit(self.background, (x, y))
    #     pygame.display.flip()

    # def death(self):

    def check_collision(self, snake, food):
        """Check for collisions"""


        collision = pygame.sprite.collide_rect(self.snake,self.food)
        return collision




    def MainLoop(self):
        """This is the Main Loop of the Game"""

        direction = 0
        #Load all sprites
        self.LoadSprites()

        #Create the background
        self.background = pygame.image.load("snake_resources/images/grass3.jpg").convert()
        # self.screen.blit(self.background, (0,0))
        #self.setup_background()
        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
        

        counter = 0
        running = True
        while running:
            #counter = counter + 1
         
            for event in pygame.event.get():
                pygame.draw.rect(self.screen, (0,0,0), self.food.rect)
                if event.type == pygame.QUIT:
                    running = False
                elif self.check_collision(self.snake,self.food) == True:
                    running = False
                elif event.type == KEYDOWN:
                    if (event.key == K_RIGHT):
                        self.snake.move_key_down(event.key)
                        self.setup_background()
                        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
                    elif (event.key == K_LEFT):
                        self.snake.move_key_down(event.key)
                        self.setup_background()
                        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
                    elif (event.key == K_UP):
                        self.snake.move_key_down(event.key)
                        self.setup_background()
                        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
                    elif (event.key == K_DOWN):
                        self.snake.move_key_down(event.key)
                        self.setup_background()
                        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)


                self.snake.move_always(self.snake.direction)

                self.setup_background()
                pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
                pygame.draw.rect(self.screen, (0,0,0), self.food.rect)
        # """Check for collision"""
            #lstCols = pygame.sprite.spritecollide(self.snake
                                                 #, self.pellet_sprites
                                                 #, True)

            # pygame.draw.rect(self.screen, (0,0,255), self.snake.rect)
                self.screen.blit(self.background, [0,0])

                # pygame.display.update(self.snake.rect)
                # pygame.display.update(self.food.rect)
                time.sleep(0.0001)      

            pygame.quit()
            # pygame.display.flip() 

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.MainLoop()