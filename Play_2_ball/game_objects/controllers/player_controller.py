from pygame import mixer
from pygin import Scene
from pygin.input import Input
from pygin.time import Time
from game_objects.mesh_objects.player_ball import PlayerBall
from pygame.math import Vector2
from pygin.material import Material
from pygin.game_object import GameObject
from pygin.color import Color
from pygin.sound import Sound

class PlayerController(GameObject) :
  ball_skin = Material(Color.orange, alpha=240)

  def __init__(self, position, rotation=0, scale=..., layer=0):
      super().__init__(position=position, rotation=rotation, scale=scale, layer=layer)
      self.position = position
      self.ini_x = position.x #ball 초기 생성 x 좌표
      self.ini_y = position.y #ball 초기 생성 y 좌표
      self.ini_material = PlayerController.ball_skin
  
  def start(self) :
      self.game_object = PlayerBall(self.position, 10, self.ini_material) #ball 생성
       
  def update(self):
    #공이 살아 있으면 이동, 죽어 있다면 재생성 후 상태 변경
    if not self.game_object.is_dying:
      if Input.is_pressing_left:
        self.move_left()
      if Input.is_pressing_right:
        self.move_right()
      if Input.press_space_down:
        if(self.game_object.can_clear): 
          self.clear() #클리어 가능 상태라면 stageMap으로 Scene 변경
        if(self.game_object.can_upup): self.use_upup() #스킬 사용 가능 상태라면 더블 점프
        if(self.game_object.can_smash): self.use_smash()    
    else:
        self.game_object.transform.translate(Vector2(self.ini_x, self.ini_y))
        self.game_object.is_dying = False

  def move_right(self):
    self.game_object.transform.position.x += Time.delta_time()*150
    self.update_circles()

  def move_left(self):
    self.game_object.transform.position.x -= Time.delta_time()*150
    self.update_circles()

  def use_upup(self):
    #점프 효과음
    jump_sound = mixer.Sound("Play_2_ball/assets/soundtrack/jumping.mp3")
    mixer.Sound.play(jump_sound)
    self.game_object.physics.velocity = Vector2(0, -200)
    self.game_object.material = Material(Color.orange, alpha=240)
    self.game_object.can_upup = False
    
  def use_smash(self):
    #smash 효과음
    smash_sound = mixer.Sound("Play_2_ball/assets/soundtrack/smash.mp3")
    mixer.Sound.play(smash_sound)
    self.game_object.material = Material(Color.red, alpha=240)
    self.game_object.can_smash = False
    self.game_object.is_smash = True

  def clear(self):
    Scene.change_scene(1)

  def update_circles(self):
    self.game_object.transform.translate(Vector2(self.game_object.transform.position.x , self.game_object.transform.position.y))

def set_sound(name, loop=-1):
    Sound.music(name,loop)   