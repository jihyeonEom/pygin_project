from pygin.scene import Scene
from game_objects.controllers.levelmap2_controller import LevelMap2Controller

class LevelMap2(Scene):
  def __init__(self):

    self.init_game_objects_controllers_reference_list = [LevelMap2Controller]
    super(LevelMap2, self).__init__(self.init_game_objects_controllers_reference_list)
