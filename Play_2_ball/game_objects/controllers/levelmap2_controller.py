from pygame import Vector2, mixer
from pygin.basic_objects.text import Text
from pygin.material import Material
from pygin.color import Color
from pygin.game_object import GameObject
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

class LevelMap2Controller(GameObject):

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
    samsh3 = Smash(Vector2(400,385), 10) #smash skill
    smash = Smash(Vector2(240,190),10) #smash skill
    smash2 = Smash(Vector2(180,230), 10) #smash skill
    point1 = Star(Vector2(320,280), 10) #point
    point2 = Star(Vector2(650,225), 10) #point
    point3 = Upup(Vector2(710,185), 10) #double jump
    point4 = Star(Vector2(790, 155), 10) #point
    jump = Upup(Vector2(550, 430), 10) #double jump
    jump2 = Upup(Vector2(450, 430), 10) #double jump
    flag = Flag(Vector2(250, 430), 10)

    #맵블럭 

    #큰 네모 
    map_block1 = Rectangle(Vector2(150, 240), Vector2(140,13), Material((82, 61, 41)))
    map_block2 = Rectangle(Vector2(150, 100), Vector2(140,13), Material((82, 61, 41))) #smash 될 부분 (예상)
    map_block3 = Rectangle(Vector2(150, 100), Vector2(13,140), Material((82, 61, 41))) 
    map_block4 = Rectangle(Vector2(290, 100), Vector2(15,153), Material((82, 61, 41)))

    #작은 네모 
    map_block5 = Rectangle(Vector2(185, 200), Vector2(80,13), Material((82, 61, 41)))
    map_block6 = Rectangle(Vector2(185, 140), Vector2(80,13), Material((82, 61, 41))) #smash 될 부분(예상)
    map_block7 = Rectangle(Vector2(185, 140), Vector2(13,73), Material((82, 61, 41)))
    map_block8 = Rectangle(Vector2(255, 140), Vector2(13,73), Material((82, 61, 41)))

    map_block9 = Rectangle(Vector2(160, 330), Vector2(100,13), Material((82, 61, 41)))
    laser_block = Laser(Vector2(260, 330), Vector2(80,13)) #laser
    map_block10 = Rectangle(Vector2(340, 330), Vector2(80,13), Material((82, 61, 41)))

    map_block11 = Rectangle(Vector2(460, 300), Vector2(50,13), Material((82, 61, 41)))
    map_block12 = Rectangle(Vector2(530, 270), Vector2(50,13), Material((82, 61, 41)))
    map_block13 = Rectangle(Vector2(600, 240), Vector2(50,13), Material((82, 61, 41)))

    map_block14 = Rectangle(Vector2(770, 170), Vector2(50,13), Material((82, 61, 41))) #움직이는 블록으로 하고 싶었는데 아직 구현 못했습니다..ㅠ
    map_block15 = Rectangle(Vector2(710, 380), Vector2(100,13), Material((82, 61, 41))) 
    map_block16 = Rectangle(Vector2(810, 320), Vector2(13,73), Material((82, 61, 41)))
    map_block17 = Rectangle(Vector2(600, 400), Vector2(80,13), Material((82, 61, 41))) #움직이는 블록으로 하고 싶었는데 아직 구현 못했습니다..ㅠ
    
    laser_block2 = Laser(Vector2(420, 330), Vector2(80,13)) #laser
    laser_block3 = Laser(Vector2(680, 240), Vector2(100,13)) #laser
    map_block18 = Rectangle(Vector2(600, 400), Vector2(80,13), Material((82, 61, 41)))
    map_block19 = Rectangle(Vector2(230, 450), Vector2(100,13), Material((82, 61, 41)))
    map_block20 = Rectangle(Vector2(230, 370), Vector2(100,13), Material((82, 61, 41)))
    map_block21 = Rectangle(Vector2(330, 370), Vector2(13,93), Material((82, 61, 41)))

    self.game_object_list = {
      Text(Vector2(20,0), ">", Material(Color.white), 40, font_path),
      back_btn,point1, point2, point3, point4, 
      smash, smash2, samsh3, jump, jump2, flag,
      map_block1, map_block2, map_block3, map_block4, map_block5, map_block6, map_block7, map_block8, map_block9, map_block10, 
      map_block11, map_block12, map_block13, map_block14, map_block15, map_block16, map_block17, map_block18, map_block19,
      laser_block, laser_block2, laser_block3
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
      self.player_controller = PlayerController(Vector2(210,210)) #최초 생성 위치를 인자로 가진다.
 
def set_sound(name, loop=-1):
    Sound.music(name,loop)

def backStageMap_btn_onclick():
    #스테이지맵으로 복귀
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(1)

    
