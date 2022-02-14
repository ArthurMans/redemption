import pygame
from projectile import Projectile

class Combattant(pygame.sprite.Sprite):

    def __init__(self, pv, nom):
        self.pv = pv
        self.nom = nom
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.all_projectiles = pygame.sprite.Group()
        #self.robustesse
        #self.puissance
        #self.endurance
        #self.perception
        #self.reactivite
        #self.parade

    def lancer_projectile(self):
        self.all_projectiles.add(Projectile())

    def afficher_combattant(self):
        print("nom :",self.nom,"||  pv :",self.pv)
