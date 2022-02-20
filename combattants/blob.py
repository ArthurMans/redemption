import pygame
from combattants.combattant import Combattant
from definition import *

class Blob(Combattant):

    def __init__(self, x, y):
        super().__init__()
        self.pv_max = 30
        self.pv = 30
        self.nom = 'Blob'

        self.image = pygame.image.load('assets/angry cat.png')
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.velocity = 1

