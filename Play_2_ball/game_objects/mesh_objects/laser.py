from pygin.basic_objects.basic_rectangle import BasicRectangle
from pygin.components.polygon_collider import PolygonCollider
from pygin.material import Material


class Laser(BasicRectangle):

    def __init__(self, position, dimension, material = Material((255, 0, 0)), layer=0):
        super(Laser, self).__init__(position, dimension, material, layer=layer)
        self.dimension = dimension
        self.polygon_collider = PolygonCollider(self)