import math

class WaterAnimal(object):
    def __init__(self, name, velocity, age):
        self.name = name
        self.noise = noise
        self.vel = velocity
        self.pos = [0, 0] # x,y
    
    def __str__( # fill this in)
    """ also fill this in """
    
    def swim(self, strokes, direction):
        rad_dir = math.radians(direction)
        self.pos[0] = self.pos[0] + (self.vel * strokes * math.cos(rad_dir))
        self.pos[1] = self.pos[1] + (self.vel * strokes * math.sin(rad_dir))

    def talk(self, times):
        return self.noise * times


""" Create a child class Duck that inherits from WaterAnimal. 
implement a new method 
override a method
add an attribute
set one attribute to be a specific value for Duck objects
"""


def main():
    """create an instance of both the parent and child class
    with the child, call one of the child's methods   and one of it's parent's methods
    change an attribute for each the parent and the child instance
    print each instance (you need to fill in the string method)
    """
    

if __name__ == "__main__":
    main()
