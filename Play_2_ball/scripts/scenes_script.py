from pygin import Scene
from scenes.main_menu import MainMenu
from scenes.option import Option
from scenes.stageMap import StageMap
from scenes.tutorialmap1 import TutorialMap1
from scenes.tutorialmap2 import TutorialMap2
from scenes.tutorialmap3 import TutorialMap3
from scenes.levelmap1 import LevelMap1
from scenes.levelmap2 import LevelMap2

class ScenesScript:

    @classmethod
    def get_scenes(cls):
        """
        :return: the scene list with the references to the scenes classes
        """
        return [MainMenu, StageMap, TutorialMap1, TutorialMap2, TutorialMap3, LevelMap1, LevelMap2, Option]
