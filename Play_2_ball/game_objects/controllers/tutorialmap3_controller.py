from pygame import Vector2, mixer
from pygin.basic_objects.text import Text
from pygin.material import Material
from pygin.color import Color
from pygin.game_object import GameObject
from pygin.basic_objects.basic_circle import BasicCircle
from pygin.basic_objects.button import Button
from pygin import Scene
from pygin.sound import Sound

from pygin.time import Time
from game_objects.mesh_objects.rectangle import Rectangle
from game_objects.mesh_objects.flag import Flag
from game_objects.controllers.player_controller import PlayerController
from pygin.game_object import GameObject

from game_objects.mesh_objects.smash import Smash

class TutorialMap3Controller(GameObject) :
  
  def start(self) :
    self.setup_initializer()
    
    #경로 주의
    font_path = "Play_2_ball/assets/fonts/malgun.ttf"

    guide_x = 50
    guide_y = 10

    guide_skill_x = 345
    guide_skill_y = 30
    guide_flag_x = 680
    guide_flag_y = 75

    title_size = 50
    message_size = 25
    guide_size = 19
    option_size = 15

    #뒤로가기 버튼
    back_btn = Button(Vector2(10, 10), Vector2(45, 45), Material((82, 61, 41)), func=backStageMap_btn_onclick)

    #포인트 
    point = Flag(Vector2(730,355), 10, Material(Color.blue_0))

    #test
    test = Smash(Vector2(490,335), 10) #스킬(스매쉬)
    map_block4 = Rectangle(Vector2(580, 220), Vector2(13, 150), Material((82, 61, 41)))

    #맵 블럭
    map_block1 = Rectangle(Vector2(250, 370), Vector2(50, 13), Material((82, 61, 41)))
    map_block2 = Rectangle(Vector2(350, 370), Vector2(50, 13), Material((82, 61, 41)))
    map_block3 = Rectangle(Vector2(450, 370), Vector2(80, 13), Material((82, 61, 41)))
    map_block4 = Rectangle(Vector2(630, 370), Vector2(150, 13), Material((82, 61, 41)))

    guide_skill = BasicCircle(Vector2(guide_skill_x, guide_skill_y), 10, Material(Color.white))
    guide_flag = BasicCircle(Vector2(guide_flag_x, guide_flag_y), 10, Material(Color.blue_0))

    self.game_object_list = {
        Text(Vector2(20,0), ">", Material(Color.white), 40, font_path),
        Text(Vector2(guide_x+40, guide_y), "get the WHITE BALL       then you can use SMASH by pressing space bar", Material(Color.black), message_size, font_path),
        Text(Vector2(guide_x+330, guide_y + 50), "break the wall and get your flag       ", Material(Color.black), guide_size, font_path),
        point, map_block1, map_block2, map_block3, map_block4, guide_skill, guide_flag
    }

  def update(self):
    pass
    self.initialize_scene()

  def setup_initializer(self):
    self.initial_time = Time.now()
    self.should_initialize = True

  def initialize_scene(self):
    if Time.now() - self.initial_time > 0.45 and self.should_initialize:
      self.should_initialize = False
      self.player_controller = PlayerController(Vector2(275, 330)) #최초 생성 위치를 인자로 가진다.

def set_sound(name, loop=-1):
    Sound.music(name,loop)

def backStageMap_btn_onclick():
    #스테이지맵으로 복귀
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(1)