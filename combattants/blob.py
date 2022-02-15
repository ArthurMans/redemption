import pygame
from combattants.combattant import Combattant

class Blob(Combattant):

    def __init__(self, jeu):
        super().__init__(jeu)
        self.jeu = jeu
        self.pv_max = 30
        self.pv = self.pv_max
        self.nom = 'Blob'
        self.image = pygame.image.load('assets/angry cat.png')
        self.rect = self.image.get_rect()
        self.rect.x = 830
        self.rect.y = 475
        self.velocity = 1

