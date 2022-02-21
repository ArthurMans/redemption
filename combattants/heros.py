import pygame
from combattants.combattant import Combattant
from definition import *


class Heros(Combattant):

    def __init__(self):
        super().__init__()
        self.pv_max = 100
        self.pv = 100
        self.nom = 'Antoine'

        self.est_allié = True

        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()

        self.rect.x = 450
        self.rect.y = 500
        self.velocity = 0.005

        # self.robustesse
        # self.puissance
        # self.endurance
        # self.perception
        self.reactivite = 1
        # self.parade
