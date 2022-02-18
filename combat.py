from definition import *
from jeu import Jeu

class Combat():


    def __init__(self, clock):
        self.clock = clock
        self.toutes_entités = toutes_entités

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self): # on parcourt la liste de toutes les entités
        for entités_cliquables in self.toutes_entités:
            entités_cliquables.events()
        return False

    def update(self):
        return False

    def draw(self):
        return False