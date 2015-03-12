import os, sys
import pygame
from pygame.locals import *
import itertools
import random
import time

    
class Player():
    """ This is the player rectangle that moves around the screen and eats food. """
    
    def __init__(self):

        self.x = 50
        self.y = 50

        self.rect = pygame.Rect(50,50,10,10)
        self.color = ((255,255,0))

        #to define directions later on
        #can be 0 (not moving in that direction), -1 (moving in negative direction), or 1 (moving in positive direction)
        self.x_sign = 1
        self.y_sign = 0

        self.is_dead = False

        self.score = 0

        self.speed = .1
        
    def move_always(self):
        """ The function that continuously moves the player throught the game. """
        
        #changes the x and y positions at a certain speed with directionality
        self.x += self.speed*self.x_sign        
        self.y += self.speed*self.y_sign

        #create rectangle at these new points
        self.rect = pygame.Rect(self.x, self.y, 10,10)

        #if the player leaves the screen, the player dies
        if self.x >= 640 or self.x <= 0 or self.y >= 480 or self.y <= 0:
            self.is_dead = True
      
    def change_direction(self, key):
        """ Changes the direction the player is heading based on key presses. """

        #if right arrow key is pressed, will move in positive x direction
        if (key == K_RIGHT):
            self.x_sign = 1
            self.y_sign = 0
        
        #if left arrow key is pressed, will move in negative x direction
        elif (key == K_LEFT):
            self.x_sign = -1
            self.y_sign = 0

        #if up arrow key is pressed, will move in negative y direction
        elif (key == K_UP):
            self.x_sign = 0
            self.y_sign = -1            
            
        #if down arrow key is pressed, will move in positive y direction
        elif (key == K_DOWN):
            self.x_sign = 0
            self.y_sign = 1
           
        
class Food():
    """ Initializes food that the player eats. """

    def __init__(self):

        #generates random coordinates for food
        random_x = random.randint(0,640)
        random_y = random.randint(0,480)

        #creates food rectangle at the random coordinates
        self.rect = pygame.Rect(random_x,random_y,10,10)


class DeathBlock():
    """ Initializes the "death block" obstacles. """

    def __init__(self):

        #generates random coordinates for a death block
        random_x = random.randint(0,640)
        random_y = random.randint(0,480)

        #creates food rectangle at the random coordinates
        self.rect = pygame.Rect(random_x,random_y,20,20)


class Main(object):
    """ The class that runs everything. Contains the main loop and conditions of the game. """
    
    def __init__(self, width=640,height=480):
        """Initialize the main class. """

        pygame.init()

        #initialize the sound
        pygame.mixer.init()

        #set the status of the game
        self.running = True
        
        #set the window size
        self.width = width
        self.height = height
        
        #create the screen
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()

        #create the objects in the main class
        self.player = Player()
        self.food = Food() 
        self.food.rect = self.food.rect

        #create a list to house all of the death block objects
        self.deathblocks = []

    def check_collision(self):
        """ Check for collisions between the player and death blocks and the player and food. """

        #if the player collides with a death block, kills the player
        if self.player.rect.collidelist(self.deathblocks) != -1:
            self.player.is_dead = True
        
        #if the player collides with food, updates the score and increases the speed
        #returns True if a collision occured for use in main loop
        if (self.player.rect.colliderect(self.food)) == True:
            self.player.score += 1
            self.player.speed += .05
            collision = True
        else:
            collision = False
        
        return collision

    def check_collision_pair(self, food, deathblock):
        """ Checks for collisions between the randomly placed food and death blocks. """

        return food.colliderect(deathblock)

    def make_food(self):
        """ Creates food rectangles in the main class. """

        #generates random coordinates for food
        random_x = random.randint(0,630)
        random_y = random.randint(0,470)

        #assigns the random coordinates to the food rectangle
        self.food.rect.x = random_x
        self.food.rect.y = random_y

    def check_food_collision(self):
        """ Makes sure there is no collision between the food and the death blocks. If there
            is a collision, the food block is created at a different location and then checked
            recursively for a collision, until the food is outside the death blocks. """

        for deathblock in self.deathblocks:
            if self.check_collision_pair(self.food.rect, deathblock):
                self.make_food()
                self.check_food_collision()

    def eat_and_grow(self):
        """ Handles the creation of new food when a collision occurs between the player and the
            food. """

        self.make_food()

        #creates 5 death blocks per food eaten
        for x in range(0,5):
            self.deathblocks.append(DeathBlock())

        #checks for collisions between food and death blocks
        self.check_food_collision()

    def display_update(self):
        """ Updates the display to reflect changes in the game. """

        self.screen.fill((0,0,0))

        #draws the rectangle for the player
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(self.player.x, self.player.y, 10,10))

        #draws the rectangles for the death blocks
        for x in range(0,len(self.deathblocks)):
            pygame.draw.rect(self.screen, (255,0,0), self.deathblocks[x].rect) #(255,0,0), self.deathblocks[x].rect)

        #draws the rectangle for food
        pygame.draw.rect(self.screen, (0,255,0), self.food.rect)

        #draws the text
        myfont = pygame.font.SysFont("monospace", 15, True, False)
        directions1 = myfont.render("Eat the green square!", 1, (255,255,0))
        directions2 = myfont.render("Don't leave the screen or touch the red blocks!", 1, (255,255,0))
        label = myfont.render("Score = "+ str(self.player.score), 1, (255,255,0))
        
        self.screen.blit(directions1, (443, 420))
        self.screen.blit(directions2, (210, 440))
        self.screen.blit(label, (550, 460))

        #updates the display with all drawn components
        pygame.display.update()
        pygame.display.flip()

    def MainLoop(self):
        """ This is the main loop of the game """
        
        pygame.draw.rect(self.screen, (255,255,0), self.player.rect)

        #load music
        pygame.mixer.music.load('jaws.mp3')
        
        #game loop: runs while the game is running and player is alive
        while self.running and self.player.is_dead == False:
            
            #plays the music
            pygame.mixer.music.play()
            
            #if a food/player collisions occurs, calls eat_and_grow()
            if self.check_collision() == True:
                self.eat_and_grow()

            for event in pygame.event.get():

                pygame.draw.rect(self.screen, (0,0,0), self.food.rect)

                #if quits, ends game
                if event.type == pygame.QUIT:
                    self.running = False

                #if a key is pressed, calls change_direction and passes the key
                elif event.type == KEYDOWN:

                    if (event.key == K_RIGHT):
                        self.player.change_direction(event.key)

                    elif (event.key == K_LEFT):
                        self.player.change_direction(event.key)

                    elif (event.key == K_UP):
                        self.player.change_direction(event.key)

                    elif (event.key == K_DOWN):
                        self.player.change_direction(event.key)
            
            #moves the player forawrd
            self.player.move_always()
            
            #updates the display
            self.display_update()
            
            time.sleep(0.00001)      

        pygame.quit()


if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.MainLoop()