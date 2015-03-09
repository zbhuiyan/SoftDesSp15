import os, sys
import pygame
from pygame.locals import *
from helpers import *
import itertools
import random

    
class Snake(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.rect = pygame.Rect(50,50,10,10)
    
        """Set the number of Pixels to move each time"""
        self.x_dist = 5
        self.y_dist = 5 
        
    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        xMove = 0
        yMove = 0
        speed = 10
        direction = 1

 #Sorry, it's not working, I couldn't get it figured out... Ive added velocity. While loops kept going to infinity  and never stopped running 
 #so i got rid of them. 

        if (key == K_RIGHT) or direction == 1:
            if direction !=3 or direction !=2 or direction !=0:
                xMove = self.x_dist + speed
        
        elif (key == K_LEFT) or direction == 3:
            if direction !=1 or direction !=0 or direction !=2:
                xMove = -self.x_dist - speed
        
        elif (key == K_UP) or direction == 2:
            if direction != 0 or direction !=1 or direction !=3:
                yMove = -self.y_dist + speed

            
        elif (key == K_DOWN) or direction ==0:
            if direction !=1 or direction !=2 or direction !=3:
                yMove = self.y_dist - speed
        

                # self.rect = self.rect.move(xMove,yMove)
        self.rect = self.rect.move(xMove,yMove)
        # print "!!!", self.rect
        # self.rect.move(xMove,yMove)
        # self.rect.move_ip(xMove,yMove)
        
# class Food(pygame.sprite.Sprite):
#     def __init__(self):
#         self.rect = pygame.Rect(75,80,10,10)
        # self.x_pos = x_pos
        # self.y_pos = y_pos


#     def randomize(self):
        
#         qty = 1  # or however many points you want
# # Generate a set of all points within 200 of the origin, to be used as offsets later
# # There's probably a more efficient way to do this.
#         random_x = random.randint(0,640)
#         random_y = random.randint(0,480)

    
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
        # self.food = Food()
        # self.food_sprites = pygame.sprite.RenderPlain((self.food))                 


    def setup_background(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.background,(0,0))
        background_width, background_height = self.background.get_width(), self.background.get_height()
        for x,y in itertools.product(range(0,self.width,background_width),
                                     range(0,self.height,background_height)):
            self.screen.blit(self.background, (x, y))
        pygame.display.flip()

    # def death(self):












    def MainLoop(self):
        """This is the Main Loop of the Game"""

        self.snake = Snake()
        
        direction = 0
        # snake.rect = pygame.Rect(50,50,10,10)
        # pygame.draw(self.snake.rect)

        #Load all sprites
        self.LoadSprites();

        #tell pygame to keep sending up keystrokes when they are held down
        pygame.key.set_repeat(500, 30)

        #Create the background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = pygame.image.load("snake_resources/images/grass3.jpg")
        self.background = self.background.convert()
        # self.screen.blit(self.background, (0,0))
        self.setup_background()
        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)


        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if (event.key == K_RIGHT) and direction != 3:
                        direction = 1
                        self.snake.move(event.key)
                        self.setup_background()
                        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
                    elif (event.key == K_LEFT) and direction !=1:
                        direction = 3
                        self.snake.move(event.key)
                        self.setup_background()
                        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
                    elif (event.key == K_UP) and direction != 0:
                        direction = 2
                        self.snake.move(event.key)
                        self.setup_background()
                        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
                    elif (event.key == K_DOWN) and direction != 2:
                        direction = 0
                        self.snake.move(event.key)
                        self.setup_background()
                        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
                
         

                        # pygame.draw.rect(self.screen, (0,0,255),snake.rect)


            """Check for collision"""
            #lstCols = pygame.sprite.spritecollide(self.snake
                                                 #, self.pellet_sprites
                                                 #, True)

            # pygame.draw.rect(self.screen, (0,0,255), self.snake.rect)
            # print "AAAAA: ", self.snake.rect
            pygame.display.update(self.snake.rect)
            # pygame.display.flip() 

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.MainLoop()