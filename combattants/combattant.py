import pygame

class Combattant(pygame.sprite.Sprite):

    def __init__(self, pv=100, nom='Antoine'):
        self.pv = pv
        self.nom = nom
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 200
        self.velocity = 20
        #self.robustesse
        #self.puissance
        #self.endurance
        #self.perception
        #self.reactivite
        #self.parade

    def afficher_combattant(self):
        print("nom :",self.nom,"||  pv :",self.pv)

    def bouger_a_droite(self):
        self.rect.x += self.velocity

    def bouger_a_gauche(self):
        self.rect.x -= self.velocity

    def bouger_en_haut(self):
        self.rect.y -= self.velocity

    def bouger_en_bas(self):
        self.rect.y += self.velocity
