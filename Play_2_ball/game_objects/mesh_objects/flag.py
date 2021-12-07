from pygin.basic_objects.basic_circle import BasicCircle
from pygin.components.circle_collider import CircleCollider
from pygin.material import Material
from pygin.color import Color


class Flag(BasicCircle):

    def __init__(self, position, radius, material = Material(Color.blue_0)):
        super(Flag, self).__init__(position, radius, material, layer=-1)
        self.circle_collider = CircleCollider(self)

    def die(self):
        self.destroy_me()