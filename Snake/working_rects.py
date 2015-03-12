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

        self.is_dead = False

        self.score = 0

        self.speed = .1
        

    def move_always(self):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        
        self.x += self.speed*self.x_sign        
        self.y += self.speed*self.y_sign

        self.rect = pygame.Rect(self.x, self.y, 10,10)


        if self.x >= 640 or self.x <= 0 or self.y >= 480 or self.y <= 0:
            self.is_dead = True
      

    def change_direction(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        speed = 5

    
        if (key == K_RIGHT):
            self.x_sign = 1
            self.y_sign = 0
            

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

        random_x = random.randint(0,640)
        random_y = random.randint(0,480)

        self.rect = pygame.Rect(random_x,random_y,10,10)

class DeathBlock():

    def __init__(self):

        random_x = random.randint(0,640)
        random_y = random.randint(0,480)
        self.rect = pygame.Rect(random_x,random_y,20,20)







class Main(object):
    """"""
    
    def __init__(self, width=640,height=480):
        """Initialize"""
        
        #pygame.mixer.pre_init(44100, -16, 2, 2048)

        pygame.init()

        pygame.mixer.init()

        #Initialize PyGame
        self.running = True
        
        #Set the window size
        self.width = width
        self.height = height
        
        #Create the screen
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.snake = Snake()
        self.food = Food() 
        self.food.rect = self.food.rect
        self.deathblocks = []



    def check_collision(self):
        """Check for collisions"""
        if self.snake.rect.collidelist(self.deathblocks) != -1:
            self.snake.is_dead = True
        
        if (self.snake.rect.colliderect(self.food)) == True:
            self.snake.score += 1
            self.snake.speed += .05
            print self.snake.score
            collision = True
        else:
            collision = False
        
        return collision

    def check_collision_pair(self, food, deathblock):
        return food.colliderect(deathblock)

    def make_food(self):
        random_x = random.randint(0,630)
        random_y = random.randint(0,470)

        self.food.rect.x = random_x
        self.food.rect.y = random_y

    def check_food_collision(self):
        for deathblock in self.deathblocks:
            if self.check_collision_pair(self.food.rect, deathblock):
                self.make_food()
                self.check_food_collision()
        # return


    def eat_and_grow(self):
        

        self.make_food()
        # self.food.rect.x = random_x
        # self.food.rect.y = random_y

        for x in range(0,5):
            self.deathblocks.append(DeathBlock())


        self.check_food_collision()


        if self.food.rect in self.deathblocks:
            print "you are successful"
            random_x = random.randint(0,640)
            random_y = random.randint(0,480)

            self.food.rect.x = random_x
            self.food.rect.y = random_y
        







    def display_update(self):
        self.screen.fill((0,0,0))
        # self.background.fill((0,0,0))
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(self.snake.x, self.snake.y, 10,10))

        for x in range(0,len(self.deathblocks)):
            pygame.draw.rect(self.screen, (255,0,0), self.deathblocks[x].rect) #(255,0,0), self.deathblocks[x].rect)

        # pygame.draw.rect(self.screen, (0,255,0), self.food.rect)
        pygame.draw.rect(self.screen, (0,255,0), self.food.rect)



        # font = pygame.font.SysFont('Sans', 50)
        # text = font.render('This is a text', True, (255, 0, 0))

        myfont = pygame.font.SysFont("monospace", 15, True, False)
        directions = myfont.render("Don't touch the red blocks!", 1, (255,255,0))
        label = myfont.render("Score = "+ str(self.snake.score), 1, (255,255,0))
        # print label
        self.screen.blit(label, (550, 460))
        self.screen.blit(directions, (390, 440))
        pygame.display.update()
        pygame.display.flip()


    def MainLoop(self):
        """This is the Main Loop of the Game"""
        
        pygame.draw.rect(self.screen, (255,255,0), self.snake.rect)
        pygame.mixer.music.load('jaws.mp3')#load music
        # print music
        # pygame.draw.rect(self.screen,(0,0,0),self.food.rect)
        

        while self.running and self.snake.is_dead == False:
            
            pygame.mixer.music.play()
            #pygame.mixer.Sound('jaws_theme.mp3')
            if self.check_collision() == True:
                self.eat_and_grow()
   
                # self.running = False
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
            #pygame.Rect.clamp_ip(self.snake.rect)
            self.display_update()
            
            time.sleep(0.00001)      

        pygame.quit()
            # pygame.display.flip() 

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.MainLoop()