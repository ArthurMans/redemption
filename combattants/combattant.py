import pygame

class Combattant(pygame.sprite.Sprite):

    def __init__(self, pv, nom):
        self.pv = pv
        self.nom = nom
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        #self.robustesse
        #self.puissance
        #self.endurance
        #self.perception
        #self.reactivite
        #self.parade

    def afficher_combattant(self):
        print("nom :",self.nom,"||  pv :",self.pv)
