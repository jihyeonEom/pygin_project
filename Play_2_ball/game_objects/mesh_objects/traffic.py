from pygin.basic_objects.basic_rectangle import BasicRectangle
from pygin.components.polygon_collider import PolygonCollider
from pygin.material import Material
from pygin.time import Time


class Traffic(BasicRectangle):

    def __init__(self, position, dimension, layer=0, green = 1, red = 1):
        super(Traffic, self).__init__(position, dimension, material = Material((0,255,0)), layer=layer)
        self.dimension = dimension
        self.polygon_collider = PolygonCollider(self)
        self.green = green
        self.red = red
        self.set_time = Time.now()
        self.mode = False   #false가 green, true가 red

    def update(self):
        if self.mode == False and Time.now() - self.set_time > self.green:
            self.mode = True
            self.material = Material((255,0,0))
            self.set_time = Time.now()
        elif self.mode == True and Time.now() - self.set_time > self.red:
            self.mode = False
            self.material = Material((0,255,0))
            self.set_time = Time.now()
