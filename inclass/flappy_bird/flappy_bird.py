""" A Collaboratively-Coded Clone of Flappy Bird """

import pygame
import random
import time

class FlappyModel():
    """ Represents the game state of our Flappy bird clone """
    def __init__(self, width, height):
        """ Initialize the flappy model """
        self.width = width
        self.height = height
        self.bird = Bird(0, height/2.0)
        self.background = Background(width, height)
        self.obstacles = []
        for i in range(100):
            self.obstacles.append(PipeObstacle((i+1)*500, height))

    def get_drawables(self):
        """ Return a list of DrawableSurfaces for the model """
        drawables = self.background.get_drawables()+self.bird.get_drawables()
        for obstacle in self.obstacles:
            drawables += obstacle.get_drawables()
        return drawables

    def get_player(self):
        """ return the player """
        return self.bird

    def is_dead(self):
        """ Return True if the player is dead (for instance) the player
            has collided with an obstacle, and false otherwise """
        # TODO: modify this if the player becomes more complicated
        player_rect = self.get_player().get_drawables()[0]
        if self.background.collided_with(player_rect):
            return True
        for obstacle in self.obstacles:
            if obstacle.collided_with(player_rect):
                return True
        return False

    def update(self, delta_t):
        """ Updates the model and its constituent parts """
        self.bird.update(delta_t)

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

class Background():
    """ Represents the contents of the background """
    def __init__(self, screen_width, screen_height):
        """ initialize the background for Flappy Bird.  The variables
            screen_width and screen_height are the size of the
            screen in pixels """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tile = pygame.image.load('images/plant_tile.png')
        self.tile.set_colorkey((255,255,255))
        self.star = pygame.image.load('images/largeyellowstar.jpg')
        w,h = self.star.get_size()
        self.star = pygame.transform.scale(self.star, (int(0.1*w), int(0.1*h)))
        self.star.set_colorkey((255,255,255))

        self.star_x = []
        self.star_y = []
        for i in range(1000):
            self.star_x.append(random.randint(0,25000))
            self.star_y.append(random.randint(0,screen_height-100))

    def get_drawables(self):
        """ Get the drawables for the background """
        drawables = []
        for i in range(len(self.star_x)):
            r = pygame.Rect(self.star_x[i],
                            self.star_y[i],
                            self.star_x[i] + self.star.get_rect().width,
                            self.star_y[i] + self.star.get_rect().height)
            drawables.append(DrawableSurface(self.star, r))
        return drawables + self.get_ground_drawables()

    def get_ground_drawables(self):
        """ Get just the drawables that are part of the ground.  These
            have been separated out since death will only occur if there
            is a collision with the ground (rather than other background
            drawables) """
        drawables = []
        r = pygame.Rect(0,
                        self.screen_height-self.tile.get_rect().height,
                        self.tile.get_rect().width,
                        self.tile.get_rect().height)

        for i in range(1000):
            drawables.append(DrawableSurface(self.tile,r))
            r = r.move(self.tile.get_rect().width,0)
        return drawables

    def collided_with(self, entity):
        """ Returns True iff the input drawable surface (entity) has
            collided with the ground """
        drawables = self.get_ground_drawables()
        rectangles = []
        for d in drawables:
            rectangles.append(d.get_rect())
        return entity.get_rect().collidelist(rectangles) != -1

class Bird():
    """ Represents the player in the game (the Flappy Bird) """
    def __init__(self,pos_x,pos_y):
        """ Initialize a Flappy bird at the specified position
            pos_x, pos_y """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = 50
        self.v_y = 0
        # TODO: don't depend on relative path
        self.image = pygame.image.load('images/olin_o.png')
        self.image.set_colorkey((255,255,255))

    def get_drawables(self):
        """ get the drawables that makeup the Flappy Bird Player """
        return [DrawableSurface(self.image, self.image.get_rect().move(self.pos_x, self.pos_y))]

    def update(self, delta_t):
        """ update the flappy bird's position """
        self.pos_x += self.v_x*delta_t
        self.pos_y += self.v_y*delta_t
        self.v_y += delta_t*100 # this is gravity in pixels / s^2

    def flap(self):
        """ cause the bird to accelerate upwards (negative y direction) """
        self.v_y -= 100

class PipeObstacle():
    """ A class that represents a double pipe obstacle """
    def __init__(self, pos_x, screen_height):
        """ Initialize a pip obstacle at the specified x coordinate pos_x """
        self.pos_x = pos_x
        self.pos_y_bottom = random.randint(100,screen_height-100)
        self.pos_y_top = self.pos_y_bottom - 200
        self.screen_height = screen_height
        self.pipe_top = pygame.image.load('images/pipe_top.png')
        self.pipe_body = pygame.image.load('images/pipe_body.png')
        w,h = self.pipe_top.get_size()
        self.pipe_top = pygame.transform.scale(self.pipe_top, (int(w*0.5),int(h*0.5)))
        w,h = self.pipe_body.get_size()
        self.pipe_body = pygame.transform.scale(self.pipe_body, (int(w*0.5),int(h*0.5)))
        self.pipe_top_flipped = pygame.transform.flip(self.pipe_top, False, True)

    def get_drawables(self):
        """ Get the drawables that constitute a pipe obstacle """
        # the pipe pointing up
        drawables = []
        r = pygame.Rect(self.pos_x,
                        self.pos_y_bottom,
                        self.pipe_top.get_rect().width,
                        self.pipe_top.get_rect().height)

        drawables.append(DrawableSurface(self.pipe_top,r))
        r = r.move(0,self.pipe_top.get_rect().height)
        while r.top <= self.screen_height:
            drawables.append(DrawableSurface(self.pipe_body,r))
            r = r.move(0,self.pipe_body.get_rect().height)
        # the pipe pointing down
        r = pygame.Rect(self.pos_x,
                        self.pos_y_top,
                        self.pipe_top_flipped.get_rect().width,
                        self.pipe_top_flipped.get_rect().height)
        drawables.append(DrawableSurface(self.pipe_top_flipped,r))

        while r.top > -self.pipe_body.get_rect().height:
            r = r.move(0,-self.pipe_body.get_rect().height)
            drawables.append(DrawableSurface(self.pipe_body,r))
        return drawables

    def collided_with(self, entity):
        drawables = self.get_drawables()
        rectangles = []
        for d in drawables:
            rectangles.append(d.get_rect())
        return entity.get_rect().collidelist(rectangles) != -1

class FlappyView():
    def __init__(self, model, width, height):
        """ Initialize the view for Flappy Bird.  The input model
            is necessary to find the position of relevant objects
            to draw. """
        pygame.init()
        # to retrieve width and height use screen.get_size()
        self.screen = pygame.display.set_mode((width, height))
        self.screen_boundaries = pygame.Rect(0 ,0, width, height)
        # this is used for figuring out where to draw stuff
        self.model = model

    def draw(self):
        """ Redraw the full game window """
        self.screen.fill((0,51,102))
        # get the new drawables
        self.drawables = self.model.get_drawables()
        player_pos_x = self.model.get_player().pos_x
        screen_position = self.screen_boundaries.move(player_pos_x,0)
        for d in self.drawables:
            rect = d.get_rect()
            rect = rect.move(-screen_position.x, -screen_position.y)
            surf = d.get_surface()
            self.screen.blit(surf, rect)
        pygame.display.update()

class PygameKeyboardController():
    """ Controls flappy bird by mapping spacebar to upward acceleration """
    def __init__(self, model):
        """ initialize the keyboard controller.  The specified model
            will be manipulated in response to user key presses """
        self.model = model
        self.space_pressed = False

    def process_events(self):
        """ process keyboard events.  This must be called periodically
            in order for the controller to have any effect on the game """
        pygame.event.pump()
        if not(pygame.key.get_pressed()[pygame.K_SPACE]):
            self.space_pressed = False
        elif not(self.space_pressed):
            self.space_pressed = True
            self.model.bird.flap()

class FlappyBird():
    """ The main Flappy Bird class """

    def __init__(self):
        """ Initialize the flappy bird game.  Use FlappyBird.run to
            start the game """
        self.model = FlappyModel(640, 480)
        self.view = FlappyView(self.model, 640, 480)
        self.controller = PygameKeyboardController(self.model)

    def run(self):
        """ the main runloop... loop until death """
        frame_count = 0
        last_update_time = time.time()
        while not(self.model.is_dead()):
            self.view.draw()
            self.controller.process_events()
            delta_t = time.time() - last_update_time
            self.model.update(delta_t)
            print delta_t
            last_update_time = time.time()

if __name__ == '__main__':
    flappy = FlappyBird()
    flappy.run()