class Animal:
    def __init__(self, skin_color, voice, legs):
        self.skin_color = skin_color
        self.voice = voice
        self.legs = legs

    def show_voice(self):
        print("Here my voice: ", self.voice)

    def show_color(self):
        print("Here my color: ", self.skin_color)

    def show_legs_num(self):
        print("Here my legs number: ", self.legs)


class Cat(Animal):
    def __init__(self, skin_color, voice, legs):
        super().__init__(skin_color, voice, legs)
        self.voice = "Cats_voice"


class Dog(Animal):
    def __init__(self, skin_color, voice, legs):
        super().__init__(skin_color, voice, legs)
        self.voice = "Dogs_voice"


class Lion(Cat):
    def __init__(self, skin_color, voice, legs):
        super().__init__(skin_color, voice, legs)
        self.voice = "Lions_voice"


class Werewolf(Dog):
    def __init__(self, skin_color, voice, legs, transform=True):
        super().__init__(skin_color, voice, legs)
        self.transformed = transform
        self.transformation()

    def transformation(self):
        if self.transformed:
            self.voice = "Werewolf_voice"
            self.legs = 4
        else:
            self.voice = "Hi"
            self.legs = 2


ver = Werewolf("Black", "Grr", 4, False)
ver.show_voice()
ver.show_legs_num()
