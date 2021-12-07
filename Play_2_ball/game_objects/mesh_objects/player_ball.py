from pygame import mixer
from pygin.basic_objects.basic_circle import BasicCircle
from pygin.components.circle_collider import CircleCollider
from pygin.components.physics import Physics
from pygin.color import Color
from pygame.math import Vector2
from game_objects.mesh_objects.rectangle import Rectangle
from game_objects.mesh_objects.laser import Laser
from game_objects.mesh_objects.traffic import Traffic
from game_objects.mesh_objects.flag import Flag
from game_objects.mesh_objects.star import Star
from game_objects.mesh_objects.upup import Upup
from game_objects.mesh_objects.smash import Smash
from game_objects.mesh_objects.die_effect import DieEffect
from pygin.time import Time
from pygin.sound import Sound
from pygin.material import Material
from game_objects.mesh_objects.item_graves import ItemGraves
from pygin.basic_objects.text import Text

class PlayerBall(BasicCircle) :

  def __init__(self, position, radius, material):
    super(PlayerBall, self).__init__(position, radius, material, layer=-2)
    self.circle_collider = CircleCollider(self)
    self.is_dying = False #ball이 죽었는지 표시하는 변수
    self.itemgraves = ItemGraves()    #아이템 무덤입니다.
    self.ini_material = material
    self.can_clear = False
    self.can_upup = False
    self.can_smash = False
    self.is_smash = False

  def start(self):
    #클리어 메세지
    font_path = "Play_2_ball/assets/fonts/malgun.ttf"
    self.clear1 = Text(Vector2(450, 100), "Clear", Material(Color.black, 0), 50, font_path)
    self.clear2 = Text(Vector2(440, 175), "press space bar", Material(Color.black, 0), 20, font_path)

    self.physics = Physics(self, None, 50) #물리학 적용, 중력 50, 중력으로 ball 낙하 속도를 조절 가능
    self.death_sound = Sound('Play_2_ball/assets/soundtrack/ball_death_01.ogg') #경로 주의
    self.death_sound.sound.set_volume(0.2) #볼륨 줄이기

  def update(self):
    #화면 아래로 추락하면 die
    if self.transform.position.y > 500:
      self.die()
    
    self.check_collision()

  def check_collision(self):
    (collided, game_obj) = self.circle_collider.on_collision()

    if collided:
      #ball이 Rectangle과 충돌 했을 때
      if issubclass(type(game_obj), Rectangle) and not self.is_smash and game_obj.collidable:
        #ball이 Rectangle의 위에서 충돌시 튀어오름
        #ball이 Rectangle의 옆에서 충돌시 바깥으로 밀려남
        #ball이 Rectangle의 아래에서 충돌시 아래로 튕겨남
        if game_obj.transform.position.x < self.transform.position.x and self.transform.position.x < game_obj.transform.position.x + game_obj.dimension.x :
          if self.transform.position.y > game_obj.transform.position.y + game_obj.dimension.y:
            self.physics.velocity = Vector2(0, 10)
          else:
            self.physics.velocity = Vector2(0, -200)
        elif self.transform.position.x < game_obj.transform.position.x:
          self.transform.position.x -= Time.delta_time()*150
        else:
          self.transform.position.x += Time.delta_time()*150
      #볼이 traffic을 통과할 때 red일 경우 입니다.
      elif issubclass(type(game_obj), Traffic) and game_obj.collidable and game_obj.mode == True:
        self.die()
      #ball이 Laser과 충돌했을 때입니다
      elif issubclass(type(game_obj), Laser) and game_obj.collidable:
        self.die()
      #볼이 Flag에 충돌했을 때입니다.
      elif issubclass(type(game_obj), Flag) and game_obj.collidable:
        #flag도착 효과음
        flag_sound = mixer.Sound("Play_2_ball/assets/soundtrack/stageClear.mp3")
        mixer.Sound.play(flag_sound)
        self.itemgraves.item_in(game_obj)
        self.material = game_obj.material
        self.can_clear = True
        self.clear1.material = Material(Color.black)
        self.clear2.material = Material(Color.black)
        game_obj.die()
      #볼이 Star에 충돌했을 때입니다.
      elif issubclass(type(game_obj), Star) and game_obj.collidable:
        #포인트획득 효과음
        point_sound = mixer.Sound("Play_2_ball/assets/soundtrack/getPoint.wav")
        point_sound.set_volume(0.5)
        mixer.Sound.play(point_sound)
        self.itemgraves.item_in(game_obj)
        game_obj.die()
      #볼이 Upup에 충돌했을 때입니다. -300속도로 올라갑니다
      elif issubclass(type(game_obj), Upup) and game_obj.collidable:
        self.itemgraves.item_in(game_obj)
        self.material = game_obj.material
        self.can_upup = True
        game_obj.die()
      #볼이 smash에 충돌했을 때
      elif issubclass(type(game_obj), Smash) and game_obj.collidable:
        self.itemgraves.item_in(game_obj)
        self.material = game_obj.material
        self.can_smash = True
        game_obj.die()
      elif issubclass(type(game_obj), Rectangle) and self.is_smash and game_obj.collidable:
        self.material = self.ini_material
        self.itemgraves.item_in(game_obj)
        game_obj.destroy_me()
        self.is_smash = False


  def die(self):
    if not self.is_dying:
      self.is_dying = True
      self.death_sound.play()
      self.material = self.ini_material
      self.can_clear = False
      self.can_upup = False
      self.can_smash = False
      self.clear1.material = Material(Color.black, 0)
      self.clear2.material = Material(Color.black, 0)
      r = self.circle_mesh.get_radius()
      self.itemgraves.item_out()              #죽으면 아이템 무덤에서 아이템을 뱉습니다.
      self.physics.velocity = Vector2(0,0)
      #추락사와 장애물에 충돌해서 죽은 것 구별
      if self.transform.position.y > 500:
        for i in range(7):
          DieEffect(Vector2(self.transform.position.x, 495), Material(Color.red), 1 + r*i/6, Vector2(0,0))  
      else:
        for i in range(7):
          DieEffect(Vector2(self.transform.position.x, self.transform.position.y), Material(Color.red), 1 + r*i/6, Vector2(0,0))  #시체 위에 터지도록 수정하였습니다
    
def set_sound(name, loop=-1):
    Sound.music(name,loop)         