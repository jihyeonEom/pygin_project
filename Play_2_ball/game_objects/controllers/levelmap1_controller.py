from pygame import Vector2, mixer
from pygin.basic_objects.basic_rectangle import BasicRectangle
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
from game_objects.controllers.player_controller import PlayerController
from game_objects.mesh_objects.laser import Laser
from game_objects.mesh_objects.flag import Flag
from game_objects.mesh_objects.smash import Smash
from game_objects.mesh_objects.star import Star
from game_objects.mesh_objects.upup import Upup

class LevelMapController(GameObject) :
  
  def start(self):
    self.setup_initializer()
    
    #경로 주의
    font_path = "Play_2_ball/assets/fonts/malgun.ttf"

    guide_x = 380
    guide_y = 50

    title_size = 50
    message_size = 25
    guide_size = 19
    option_size = 15

    #뒤로가기 버튼
    back_btn = Button(Vector2(10, 10), Vector2(45, 45), Material((82, 61, 41)), func=backStageMap_btn_onclick)

    #포인트 
    point = Flag(Vector2(360,390), 10, Material(Color.blue_0)) #목적지  
    point2 = Upup(Vector2(430,210), 10) #double jump
    point3 = Upup(Vector2(585,370), 10) #double jump2
    point4 = Upup(Vector2(460,370), 10) #double jump3
    point5 = Star(Vector2(765,190), 10) #point

    #test
    smash = Smash(Vector2(680,150),10) #smash skill
    map_block5 = Rectangle(Vector2(785,100), Vector2(13,100), Material((82,61,41)))
    map_block9 = Rectangle(Vector2(745,200), Vector2(53,13), Material((82,61,41)))

    #맵블럭 
    map_block1 = Rectangle(Vector2(100, 255), Vector2(150,13), Material((82, 61, 41)))
    map_block2 = Rectangle(Vector2(300, 220), Vector2(50,13), Material((82, 61, 41))) 
    map_block3 = Rectangle(Vector2(530, 200), Vector2(170,13), Material((82, 61, 41)))
    map_block4 = Rectangle(Vector2(650, 163), Vector2(60,13), Material((82, 61, 41)))
    map_block6 = Rectangle(Vector2(830, 350), Vector2(70,13), Material((82, 61, 41)))
    map_block7 = Rectangle(Vector2(710, 380), Vector2(70,13), Material((82, 61, 41)))
    map_block8 = Rectangle(Vector2(350, 400), Vector2(50,13), Material((82, 61, 41)))
    laser_block = Laser(Vector2(220, 300), Vector2(550,13))
 
    
    self.game_object_list = {
      Text(Vector2(20,0), ">", Material(Color.white), 40, font_path),
      map_block1, map_block2, map_block3, map_block4, map_block5, map_block6, map_block7, map_block8, map_block9, point, point2, point3, point4, point5, smash, laser_block, back_btn
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
      self.player_controller = PlayerController(Vector2(175,230)) #최초 생성 위치를 인자로 가진다.

def set_sound(name, loop=-1):
    Sound.music(name,loop)

def backStageMap_btn_onclick():
    #스테이지맵으로 복귀
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(1)

  
