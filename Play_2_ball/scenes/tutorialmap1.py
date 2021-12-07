from pygin.scene import Scene
from game_objects.controllers.tutorialmap1_controller import TutorialMap1Controller

class TutorialMap1(Scene) :
  def __init__(self):
    
    self.init_game_objects_controllers_reference_list = [TutorialMap1Controller]
    super(TutorialMap1, self).__init__(self.init_game_objects_controllers_reference_list)