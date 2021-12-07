from pygin.scene import Scene
from game_objects.controllers.stageMap_controller import StageMapController

class StageMap(Scene) :
  def __init__(self):
    
    self.init_game_objects_controllers_reference_list = [StageMapController]
    super(StageMap, self).__init__(self.init_game_objects_controllers_reference_list)