import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob
from combattants.heros import Heros
from bouton import Bouton


class Jeu:

    def __init__(self):
        self.tout_combattants = pygame.sprite.Group()
        self.tout_ennemis = pygame.sprite.Group()
        self.tout_alliés = pygame.sprite.Group()

        self.appui = {}
        self.bouton_attaque = Bouton(self)

        self.heros = None
        self.spawn_heros()

        self.blob = None
        self.spawn_blob()

    def verif_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_blob(self):
        self.blob = Blob(self)
        self.tout_ennemis.add(self.blob)
        self.tout_combattants.add(self.blob)

    def spawn_heros(self):
        self.heros = Heros(self)
        self.tout_combattants.add(self.heros)
        self.tout_alliés.add(self.heros)





