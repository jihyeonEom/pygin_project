from pygame import Vector2
from pygin.basic_objects.text import Text
from pygin.material import Material
from pygin.color import Color
from pygin.game_object import GameObject
from pygin.basic_objects.basic_rectangle import BasicRectangle
from pygin.sound import Sound
from pygin import Scene
from pygin.basic_objects.button import Button
from pygin.engine import Engine
from pygame import mixer

class MainMenuController(GameObject):
    #다른 씬에서 메인씬으로 넘어올때 음악이 중복으로 재생되는 현상 방지
    #스테이지맵에서 메인화면으로 돌아올 때 False
    donot_play_overlap = True
    sound_path = "Play_2_ball/assets/soundtrack/Invade.wav"
    back_sound = Sound("Play_2_ball/assets/soundtrack/Invade.wav")

    def start(self):
        """
        This method will be called when this object is created
        """
        
        #경로 주의
        font_path = "Play_2_ball/assets/fonts/malgun.ttf"

        title_x = 352
        title_y = 75

        start_x = 460
        start_y = 220

        exit_x = 467
        exit_y = 300

        option_x = 900
        option_y = 420

        title_size = 50
        message_size = 30
        option_size = 15

        #title 위 아래에 있는 갈색 네모
        background_rect1 = BasicRectangle(Vector2(275, 65), Vector2(90, 13), Material((82, 61, 41)))
        background_rect2 = BasicRectangle(Vector2(625, 148), Vector2(90, 13), Material((82, 61, 41)))
        #start, exit버튼, option버튼
        start_btn = Button(Vector2(start_x-3, start_y), Vector2(70, 45), Material((82, 61, 41)), func=start_btn_onclick)
        exit_btn = Button(Vector2(start_x-3, exit_y), Vector2(70, 45), Material((82, 61, 41)), func=exit_btn_onclick)
        option_btn = Button(Vector2(890, 410), Vector2(70, 45), Material((82, 61, 41), 200), func=option_btn_onclick)

        self.game_object_list = [
            Text(Vector2(title_x, title_y), "PLAY 2 BALL", Material(Color.black), title_size, font_path),
            Text(Vector2(start_x, start_y), "Start", Material(Color.white), message_size, font_path),
            Text(Vector2(exit_x, exit_y), "Exit", Material(Color.white), message_size, font_path),
            Text(Vector2(option_x, option_y), "Option", Material(Color.white), option_size, font_path),
            background_rect1, background_rect2, start_btn, exit_btn, option_btn
        ]

        if(self.donot_play_overlap):
            set_sound(self.sound_path)

    def update(self):
        """
        This method will be called every frame
        """

def set_sound(name,loop=-1):
    Sound.music(name,loop)

def start_btn_onclick():
    #튜토리얼 스테이지 맵으로 이동
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    #set_sound(, 0)
    Scene.change_scene(1)

def exit_btn_onclick():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Engine.end_game()

def option_btn_onclick():
    click_sound = mixer.Sound("Play_2_ball/assets/soundtrack/clickBtn.mp3")
    mixer.Sound.play(click_sound)
    Scene.change_scene(7)

