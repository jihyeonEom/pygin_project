from pygame import mixer

class Sound :
    
    def __init__(self, name, volume=1.0):
        mixer.init()
        self.name = name
        self.sound = mixer.Sound(self.name)
        self.volume = volume

    def play(self) :
        self.sound.play()

    @classmethod
    def music(cls, name, loop = -1) :
        mixer.music.load(name)
        mixer.music.play(loop)

    def volume_down(self):
        self.volume -= 0.1
        mixer.music.set_volume(self.volume)
        print("v dowm")

    def volume_up(self):
        self.volume += 0.1
        mixer.music.set_volume(self.volume)
        print("v up")