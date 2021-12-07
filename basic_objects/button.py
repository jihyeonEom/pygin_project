from pygin.input import Input
from pygin.basic_objects.basic_rectangle import BasicRectangle
from pygin.material import Material
from pygame.math import Vector2

class Button(BasicRectangle):
    
    def __init__(self, position=Vector2(0, 0), dimension=Vector2(10, 10), material=Material(), layer=0, scale=Vector2(1, 1), func = None):
        super(Button,self).__init__(position, dimension, material, layer, scale)
        self.func = func

    def protected_update(self):
        super(Button,self).protected_update()
        if Input.press_mouse_left:
            before_x, after_x = self.transform.position.x, self.transform.position.x + self.dimension.x
            before_y, after_y = self.transform.position.y, self.transform.position.y + self.dimension.y
            if before_x <= Input.mouse_x <= after_x and before_y <= Input.mouse_y <= after_y:
                if self.func is not None:
                    self.func()