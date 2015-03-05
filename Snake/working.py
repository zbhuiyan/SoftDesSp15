import os, sys
import pygame
from pygame.locals import *
from helpers import *

    
class Snake(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.rect = pygame.Rect(50,50,10,10)
        self.pellets = 0
        """Set the number of Pixels to move each time"""
        self.x_dist = 5
        self.y_dist = 5 
        
    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        xMove = 0
        yMove = 0
        
        if (key == K_RIGHT):
            xMove = self.x_dist
        elif (key == K_LEFT):
            xMove = -self.x_dist
        elif (key == K_UP):
            yMove = -self.y_dist
        elif (key == K_DOWN):
            yMove = self.y_dist
        # self.rect = self.rect.move(xMove,yMove)
        self.rect = self.rect.move(xMove,yMove)
        print "!!!", self.rect
        # self.rect.move(xMove,yMove)
        # self.rect.move_ip(xMove,yMove)
        

class Main():
    """"""
    
    def __init__(self, width=640,height=480):
        """Initialize"""
        
        #Initialize PyGame
        pygame.init()
        
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

    # def update_screen(self):


    def MainLoop(self):
        """This is the Main Loop of the Game"""
        
        self.snake = Snake()
        # snake.rect = pygame.Rect(50,50,10,10)
        pygame.draw.rect(self.screen, (0,0,255), self.snake.rect)
        # pygame.draw(self.snake.rect)

        #Load all sprites
        self.LoadSprites();

        #tell pygame to keep sending up keystrokes when they are held down
        pygame.key.set_repeat(500, 30)
        
        #Create the background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.snake.move(event.key)
                        # self.background.fill((0,0,0))
                        self.screen.fill((0,0,0))
                        pygame.draw.rect(self.screen, (0,0,255), self.snake.rect)

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