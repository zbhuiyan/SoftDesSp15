"""  """

import pygame
import random
import time

class DrawableSurface():
    """ A class that wraps a pygame.Surface and a pygame.Rect """
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


class Snake():
    """ represents the state of the player in the game """
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def update(self):
        if direction == 0:
            pos_y += vel
        elif direction == 1:
            pos_x -= vel
        elif direction == 2:
            pos_y -= vel
        elif direction == 3:
            pos_x -= vel
        #self.pos_x += .1
        #self.pos_y += self.vel_y
        #self.vel += .01

    #def change_direction(self):
        #self.vel_y -= 1

    def get_drawables(self):
        w,h = self.image.get_size()
        return [DrawableSurface(self.image, pygame.Rect(self.pos_x,
                                                        self.pos_y,
                                                        w,
                                                        h))]

class Background():
    """  """
    def __init__(self,width,height):
        self.image = pygame.image.load('snake_resources/images/grass.png')
        self.height = height

    def get_drawables(self):
        """ Gets the drawables for the background """
        drawables = []
        for i in range(100):
            drawables.append(DrawableSurface(self.image,
                                             pygame.Rect(i*32,self.height - 32,32,32)))
        return drawables

    def collided_with(self, entity):
        """ Returns True if the input drawable surface (entity) has
            collided with the ground """
        drawables = self.get_drawables()
        rectangles = []
        for d in drawables:
            rectangles.append(d.get_rect())
        return entity.get_rect().collidelist(rectangles) != -1

class GameState():
    """ Represents the game state of Snake """
    def __init__(self, width, height):
        """ Initialize the game state """
        self.width = width
        self.height = height
        self.background = Background(width, height)
        self.snake = Snake(0,200)

    def get_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        return self.snake.get_drawables() + self.background.get_drawables()

    def is_dead(self):
        """ Return True if the player is dead (for instance) the player
            has collided with an obstacle, and false otherwise """
        # TODO: modify this if the player becomes more complicated
        player_rect = self.snake.get_drawables()[0]
        return self.background.collided_with(player_rect)

    def update(self):
        """ Updates the model and its constituent parts """
        self.snake.update()


class SnakeController():
    def __init__(self, model):
        self.model = model
        self.direction = 0

    def process_events(self):
        """  """
        pygame.event.pump()
        
        if pygame.key.get_pressed()[pygame.K_UP] != 0 and direction != 0:
            direction = 2

        if pygame.key.get_pressed()[pygame.K_DOWN] != 0 and direction != 2:
            direction = 0

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and direction != 1:
            direction = 3

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0 and direction != 3:
            direction = 1


class GamePlay():
    """  """

    def __init__(self):
        """  """
        self.model = GameState(640, 480)
        self.controller = SnakeController(self.model)

    def run(self):
        """ the main runloop... loop until death """
        last_update_time = time.time()
        while not(self.model.is_dead()):
            self.view.draw()
            self.controller.process_events()
            self.model.update()
            last_update_time = time.time()

if __name__ == '__main__':
    game = GamePlay()
    game.run()