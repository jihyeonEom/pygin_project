from pygin.scene import Scene
from game_objects.controllers.tutorialmap2_controller import TutorialMap2Controller

class TutorialMap2(Scene) :
  def __init__(self):
    
    self.init_game_objects_controllers_reference_list = [TutorialMap2Controller]
    super(TutorialMap2, self).__init__(self.init_game_objects_controllers_reference_list)