from game_objects.mesh_objects.laser import Laser
from pygin.components.polygon_collider import PolygonCollider
from pygin.time import Time
from pygin.material import Material

class MoveLaser(Laser):

    def __init__(self, position, dimension, material = Material((255, 0, 0)), layer=0, direction = "right", time = 0):
        super(Laser, self).__init__(position, dimension, material, layer=layer)
        self.dimension = dimension
        self.polygon_collider = PolygonCollider(self)
        self.travel_time = time
        self.set_time = Time.now()
        self.direction = direction

        if direction == "right":
            self.dir_x = 1
            self.dir_y = 0
        elif direction == "left":
            self.dir_x = -1
            self.dir_y = 0
        elif direction == "up":
            self.dir_x = 0
            self.dir_y = -1
        elif direction == "down":
            self.dir_x = 0
            self.dir_y = 1

    def update(self):
        if Time.now() - self.set_time < self.travel_time:
            self.transform.position.x += Time.delta_time()*100*self.dir_x
            self.transform.position.y += Time.delta_time()*100*self.dir_y
        else:
            self.dir_x *= -1
            self.dir_y *= -1
            self.set_time = Time.now()

