from definition import *

class Combat():


    def __init__(self, clock):
        self.clock = clock

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        return False

    def update(self):
        return False

    def draw(self):
        return False