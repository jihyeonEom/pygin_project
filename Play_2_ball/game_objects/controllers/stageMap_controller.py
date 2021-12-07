from pygame import Vector2, mixer
from pygin.basic_objects.text import Text
from pygin.material import Material
from pygin.color import Color
from pygin.game_object import GameObject
from pygin.basic_objects.basic_rectangle import BasicRectangle
from pygin.basic_objects.button import Button
from pygin import Scene
from .main_menu_controller import MainMenuController
from pygin.sound import Sound

class StageMapController(GameObject) :
  ball_skin = Material(Color.orange, alpha=240)
  def start(self) :
    
    #경로 주의
    font_path = "Play_2_ball/assets/fonts/malgun.ttf"

    #스테이지 이름 텍스트 좌표
    stage_x = 75
    stage_y = 160

    Basic_x = 75
    Basic_y = 240

    tutorial1_x = 450
    tutorial1_y = 75

    tutorial2_x = 450
    tutorial2_y = 150

    tutorial3_x = 450
    tutorial3_y = 225

    level1_x = 450
    level1_y = 300

    level2_x = 450
    level2_y = 375

    title_size = 50
    message_size = 25
    option_size = 15
    
    background_rect1 = BasicRectangle(Vector2(75, 140), Vector2(170, 13), Material((82, 61, 41)))
    background_rect2 = BasicRectangle(Vector2(75, 320), Vector2(170, 13), Material((82, 61, 41)))

    #뒤로가기 버튼
    back_btn = Button(Vector2(10, 10), Vector2(45, 45), Material((82, 61, 41)), func=backMain_btn_onclick)

    #단계선택 버튼
    tuto1_btn = Button(Vector2(tutorial1_x, tutorial1_y), Vector2(350, 50), Material((82, 61, 41)), func=tutorial1_onclick)
    tuto2_btn = Button(Vector2(tutorial2_x, tutorial2_y), Vector2(350, 50), Material((82, 61, 41)), func=tutorial2_onclick)
    tuto3_btn = Button(Vector2(tutorial3_x, tutorial3_y), Vector2(350, 50), Material((82, 61, 41)), func=tutorial3_onclick)
    level1_btn = Button(Vector2(level1_x, level1_y), Vector2(350, 50), Material((82, 61, 41)), func=level1_onclick)
    level2_btn = Button(Vector2(level2_x, level2_y), Vector2(350, 50), Material((82, 61, 41)), func=level2_onclick)

    self.game_object_list = {
      Text(Vector2(20,0), ">", Material(Color.white), 40, font_path),
      Text(Vector2(stage_x, stage_y), "STAGE 1", Material(Color.black), title_size, font_path),
      Text(Vector2(Basic_x, Basic_y), "BASIC", Material(Color.black), title_size, font_path),
      Text(Vector2(tutorial1_x+15, tutorial1_y+4), "TUTORIAL  1", Material(Color.white), message_size, font_path), 
      Text(Vector2(tutorial2_x+15, tutorial2_y+4), "TUTORIAL  2", Material(Color.white), message_size, font_path),
      Text(Vector2(tutorial3_x+15, tutorial3_y+4), "TUTORIAL  3", Material(Color.white), message_size, font_path), 
      Text(Vector2(level1_x+15, level1_y+4), "LEVEL  1", Material(Color.white), message_size, font_path),
      Text(Vector2(level2_x+15, level2_y+4), "LEVEL  2", Material(Color.white), message_size, font_path),
      background_rect1, background_rect2
    }

  def update(self):
     pass

def set_sound(name, loop=-1):
    Sound.music(name,loop)

def backMain_btn_onclick():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(0)
    MainMenuController.donot_play_overlap = False

def tutorial1_onclick():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(2)                                                 

def tutorial2_onclick():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(3) 

def tutorial3_onclick():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(4)

#본 스테이지로 이동하는 버튼 
def level1_onclick():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(5)

def level2_onclick():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(6)