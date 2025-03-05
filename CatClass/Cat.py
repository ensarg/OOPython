import simpleaudio as sa
from pydub import AudioSegment
from pydub.playback import play
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_color(self):
        return self.color

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_color(self, color):
        self.color = color

    def meow(self):
        print(f"{self.name} says: Meow!")
        try:
            wave_obj = sa.WaveObject.from_wave_file("/Users/ensar/IdeaProjects/sounds/cat.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()
        except Exception as e:
            print(f"Error playing sound: {e}")
    def meow2(self):
        print(f"{self.name} says: Meow!")
    try:
        sound = AudioSegment.ffmpeg("/Users/ensar/IdeaProjects/sounds/cat-meow.mp3")
        play(sound)
    except Exception as e:
        print(f"Error playing sound: {e}")