from pygame import Vector2, mixer
from pygin import sound
from pygin.basic_objects.text import Text
from pygin.material import Material
from pygin.color import Color
from pygin.game_object import GameObject
from pygin.basic_objects.basic_rectangle import BasicRectangle
from pygin.sound import Sound
from pygin import Scene
from pygin.basic_objects.button import Button
from game_objects.controllers.main_menu_controller import MainMenuController
from game_objects.controllers.player_controller import PlayerController

class OptinoController(GameObject):
    #다른 씬에서 메인씬으로 넘어올때 음악이 중복으로 재생되는 현상 방지
    #스테이지맵에서 메인화면으로 돌아올 때 False
    donot_play_music_repeate = True
    mysound = MainMenuController.back_sound
    now_vol = 10
    #경로 주의
    font_path = "Play_2_ball/assets/fonts/malgun.ttf"
    sound_path = "Play_2_ball/assets/soundtrack/Invade.wav"

    v_up_clicked = False
    v_down_clicked = False

    def start(self):
        """
        This method will be called when this object is created
        """
        
        title_x = 352
        title_y = 75

        title_size = 50
        message_size = 30
        option_size = 15

        #title 위 아래에 있는 갈색 네모
        background_rect1 = BasicRectangle(Vector2(275, 65), Vector2(90, 13), Material((82, 61, 41)))
        background_rect2 = BasicRectangle(Vector2(625, 148), Vector2(90, 13), Material((82, 61, 41)))
        
        #뒤로가기 버튼
        back_btn = Button(Vector2(10, 10), Vector2(45, 45), Material((82, 61, 41)), func=backMain_btn_onclick)

        #볼륨 조절 버튼
        down_btn = Button(Vector2(450, 210), Vector2(45, 45), Material((82, 61, 47)), func=v_down)
        up_btn = Button(Vector2(650, 210), Vector2(45, 45), Material((82, 61, 47)), func=v_up)

        #공 색깔 선택 버튼
        orange_ball = Button(Vector2(450, 310), Vector2(45, 45), Material(Color.orange), func=c_ball_orange)
        blue_ball = Button(Vector2(550, 310), Vector2(45, 45), Material(Color.blue), func=c_ball_blue)
        gray_ball = Button(Vector2(650, 310), Vector2(45, 45), Material(Color.gray), func=c_ball_gray)

        self.game_object_list = [
            Text(Vector2(20,0), ">", Material(Color.white), 40, self.font_path),
            Text(Vector2(464,200), "-", Material(Color.white), 40, self.font_path),
            Text(Vector2(658,200), "+", Material(Color.white), 40, self.font_path),
            Text(Vector2(title_x + 70, title_y), "Option", Material(Color.black), title_size, self.font_path),
            Text(Vector2(300, 210), "Volume", Material(Color.black), message_size, self.font_path),
            Text(Vector2(550, 210), str(self.now_vol), Material(Color.black), message_size, self.font_path),
            Text(Vector2(270, 310), "Ball Color", Material(Color.black), message_size, self.font_path),
            background_rect1, background_rect2, back_btn, down_btn, up_btn,
            orange_ball, blue_ball, gray_ball
        ]
        
    def update(self):
        """
        This method will be called every frame
        """
        if((self.v_up_clicked or self.v_down_clicked) and (self.now_vol >= 0 and self.now_vol < 11)):
            self.game_object_list[5].text_mesh.message = str(self.now_vol)

def set_sound(name,loop=-1):
    Sound.music(name,loop)

def backMain_btn_onclick():
    #튜토리얼 스테이지 맵으로 이동
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(0)
    MainMenuController.donot_play_overlap = False

def v_down():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    OptinoController.mysound.volume_down()
    if(OptinoController.now_vol > 0):
        OptinoController.now_vol -= 1
    OptinoController.v_down_clicked = True
    OptinoController.v_up_clicked = False

def v_up():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    OptinoController.mysound.volume_up()
    if(OptinoController.now_vol < 10):
        OptinoController.now_vol += 1
    OptinoController.v_down_clicked = False
    OptinoController.v_up_clicked = True

def c_ball_orange():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    PlayerController.ball_skin = Material(Color.orange, alpha=240)

def c_ball_blue():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    PlayerController.ball_skin = Material(Color.blue, alpha=240)

def c_ball_gray():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    PlayerController.ball_skin = Material(Color.gray, alpha=240)
