import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob
from combattants.heros import Heros


class Jeu:

    def __init__(self):
        self.combattant = Heros(self)
        self.tout_combattants = pygame.sprite.Group()
        self.tout_combattants.add(self.combattant)
        self.tout_ennemis = pygame.sprite.Group()
        self.tout_alliés = pygame.sprite.Group()
        self.tout_alliés.add(self.combattant)
        self.appui = {}
        self.spawn_blob()

    def verif_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_blob(self):
        blob = Blob(self)
        self.tout_ennemis.add(blob)
        self.tout_combattants.add(blob)
