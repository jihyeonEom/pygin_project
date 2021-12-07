from pygin.scene import Scene
from game_objects.controllers.option_controller import OptinoController


class Option(Scene):

    def __init__(self):
        """
        Create the list of mesh_objects and call the superclass constructor passing the list
        """
        self.init_game_objects_controllers_reference_list = [OptinoController]
        super(Option, self).__init__(self.init_game_objects_controllers_reference_list)
