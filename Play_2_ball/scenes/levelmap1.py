from pygin.scene import Scene
from game_objects.controllers.levelmap1_controller import LevelMapController

class LevelMap1(Scene):
  def __init__(self):

    self.init_game_objects_controllers_reference_list = [LevelMapController]
    super(LevelMap1, self).__init__(self.init_game_objects_controllers_reference_list)
