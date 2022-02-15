import pygame
from combattants.combattant import Combattant
from definition import *

class Blob(Combattant):

    def __init__(self,jeu):
        super().__init__(jeu)
        self.jeu = jeu
        self.pv = 30
        self.pv_max = 30
        self.nom = 'Blob'
        self.image = pygame.image.load('assets/angry cat.png')
        self.rect = self.image.get_rect()
        self.rect.x = largeur_ecran-600
        self.rect.y = (hauteur_ecran /2)
        self.velocity = 1

    def avance(self):
        if not self.jeu.verif_collision(self, self.jeu.tout_combattants):
            self.rect.x -= self.velocity

