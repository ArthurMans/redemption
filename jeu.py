import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob

class Jeu:

    def __init__(self):
        self.combattant = Combattant()
        self.tout_joueurs = pygame.sprite.Group()
        self.joueur = Combattant(self)
        self.tout_joueurs.add(self.joueur)
        self.tout_monstres = pygame.sprite.Group()
        self.appui = {}
        self.spawn_blob()

    def verif_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_blob(self):
        blob = Blob(self)
        self.tout_monstres.add(blob)