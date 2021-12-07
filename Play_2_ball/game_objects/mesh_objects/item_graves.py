from pygame import Vector2
from pygin.material import Material
from game_objects.mesh_objects.flag import Flag
from game_objects.mesh_objects.star import Star
from game_objects.mesh_objects.upup import Upup
from game_objects.mesh_objects.smash import Smash
from game_objects.mesh_objects.rectangle import Rectangle

class ItemGraves():

    def __init__(self):
        self.member = []

    def item_in(self, obj):
        if(obj.__class__.__name__ == 'Rectangle'):
            self.member.append((obj.__class__.__name__,obj.transform.position.x,obj.transform.position.y, obj.dimension)) 
        else: 
            self.member.append((obj.__class__.__name__, obj.transform.position.x, obj.transform.position.y, obj.radius))

    def item_out(self):
        for ghost in self.member:
            if ghost[0] == 'Star':
                Star(Vector2(ghost[1],ghost[2]), ghost[3])
            elif ghost[0] == 'Upup':
                Upup(Vector2(ghost[1],ghost[2]), ghost[3])
            elif ghost[0] == 'Flag':
                Flag(Vector2(ghost[1],ghost[2]), ghost[3])
            elif ghost[0] == 'Smash':
                Smash(Vector2(ghost[1],ghost[2]), ghost[3])
            elif ghost[0] == 'Rectangle':
                Rectangle(Vector2(ghost[1],ghost[2]), Vector2(ghost[3]), Material((82, 61, 41)))
        print(self.member)
        self.member = []