from pygin.scene import Scene
from game_objects.controllers.tutorialmap3_controller import TutorialMap3Controller

class TutorialMap3(Scene) :
  def __init__(self):
    
    self.init_game_objects_controllers_reference_list = [TutorialMap3Controller]
    super(TutorialMap3, self).__init__(self.init_game_objects_controllers_reference_list)