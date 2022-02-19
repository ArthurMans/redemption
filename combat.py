from definition import *
from random import randint

class Combat():


    def __init__(self, screen,  clock, liste_combattants):
        self.screen = screen
        self.clock = clock

        self.liste_combattants = liste_combattants

        self.tour = 0
        self.priorité = []

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        if tour == 0:
            self.creation_priorité()
        return False

    def update(self):
        return False

    def draw(self):
        return False

    def creation_priorité(self):
        for i in range(0, len(self.liste_combattants) - 1):
            liste_ex_aequo = []
            min = i
            for j in range(i + 1, len(self.liste_combattants)):
                if self.liste_combattants[j].reactivite < self.liste_combattants[min].reactivite:
                    min = j
                elif self.liste_combattants[j].reactivite == self.liste_combattants[min].reactivite:
                    liste_ex_aequo.append(self.liste_combattants[j])

            if (min != i):
                tmp = self.liste_combattants[i]
                self.liste_combattants[i] = self.liste_combattants[min]
                self.liste_combattants[min] = tmp

