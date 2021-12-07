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
from game_objects.mesh_objects.laser import Laser
from game_objects.mesh_objects.rectangle import Rectangle
from game_objects.mesh_objects.flag import Flag
from game_objects.mesh_objects.star import Star
from game_objects.mesh_objects.upup import Upup
from game_objects.controllers.player_controller import PlayerController
from pygin.game_object import GameObject


class TutorialMap2Controller(GameObject) :
  
  def start(self) :
    self.setup_initializer()
    
    #경로 주의
    font_path = "Play_2_ball/assets/fonts/malgun.ttf"

    guide_x = 50
    guide_y = 10

    guide_skill_x = 310
    guide_skill_y = 30
    guide_star_x = 360
    guide_star_y = 75
    guide_laserBlock_x = 810
    guide_laserBlock_y = 65

    title_size = 50
    message_size = 25
    guide_size = 19
    option_size = 15

    #뒤로가기 버튼
    back_btn = Button(Vector2(10, 10), Vector2(45, 45), Material((82, 61, 41)), func=backStageMap_btn_onclick)

    #포인트 
    point = Flag(Vector2(730,355), 10) #목적지
    poin2 = Star(Vector2(650,315), 10) #포인트
    poin3 = Upup(Vector2(570,335), 10) #스킬(더블점프)

    #맵 블럭
    map_block1 = Rectangle(Vector2(180, 220), Vector2(50, 13), Material((82, 61, 41)))
    map_block2 = Rectangle(Vector2(280, 280), Vector2(50, 13), Material((82, 61, 41)))
    map_block3 = Rectangle(Vector2(380, 340), Vector2(80, 13), Material((82, 61, 41)))
    map_block4 = Rectangle(Vector2(650, 370), Vector2(120, 13), Material((82, 61, 41)))
    laser_block1 = Laser(Vector2(510, 370), Vector2(100, 13))

    guide_star = BasicCircle(Vector2(guide_star_x, guide_star_y), 10, Material(Color.star_yellow))
    guide_skill = BasicCircle(Vector2(guide_skill_x, guide_skill_y), 10, Material(Color.green))
    guide_laserBlock = BasicRectangle(Vector2(guide_laserBlock_x, guide_laserBlock_y), Vector2(50, 13), Material(Color.red))

    self.game_object_list = {
        Text(Vector2(20,0), ">", Material(Color.white), 40, font_path),
        Text(Vector2(guide_x, guide_y), "get the GREEN BALL       then you can use DOUBLE-JUMP by pressing space bar", Material(Color.black), message_size, font_path),
        Text(Vector2(guide_x+150, guide_y + 50), "get your POINT        and Be careful not to touch the LASER BLOCK        ", Material(Color.black), guide_size, font_path),
        point, poin2, poin3, map_block1, map_block2, map_block3, map_block4, laser_block1,
        guide_star, guide_skill, guide_laserBlock
    }
    
  def update(self):
    self.initialize_scene()

  def setup_initializer(self):
    self.initial_time = Time.now()
    self.should_initialize = True

  def initialize_scene(self):
    if Time.now() - self.initial_time > 0.45 and self.should_initialize:
      self.should_initialize = False
      self.player_controller = PlayerController(Vector2(200, 200)) #최초 생성 위치를 인자로 가진다.

def set_sound(name, loop=-1):
    Sound.music(name,loop)

def backStageMap_btn_onclick():
    #스테이지맵으로 복귀
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(1)