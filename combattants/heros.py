import pygame
from combattants.combattant import Combattant
from definition import *


class Heros(Combattant):

    def __init__(self, jeu, est_allié=True):
        super().__init__(jeu)
        self.jeu = jeu
        self.pv_max = 100
        self.pv = 100
        self.nom = 'Antoine'
        self.est_allié = est_allié
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.all_projectiles = pygame.sprite.Group()
        self.rect.x = 450
        self.rect.y = 200
        self.velocity = 30
        # self.robustesse
        # self.puissance
        # self.endurance
        # self.perception
        # self.reactivite
        # self.parade
