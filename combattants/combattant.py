import pygame
from projectile import Projectile


class Combattant(pygame.sprite.Sprite):

    def __init__(self, jeu, est_allié=True):
        super().__init__()
        self.jeu = jeu
        self.pv = 50
        self.nom = ''
        self.est_allié = est_allié
        # allié à gauche, ennemmi à droite
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

    def lancer_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def afficher_combattant(self):
        print("nom :", self.nom, "||  pv :", self.pv)

    def bouger_a_droite(self):
        if not self.jeu.verif_collision(self, self.jeu.tout_ennemis):
            self.rect.x += self.velocity

    def bouger_a_gauche(self):
        self.rect.x -= self.velocity

    def bouger_en_haut(self):
        if not self.jeu.verif_collision(self, self.jeu.tout_ennemis):
            self.rect.y -= self.velocity

    def bouger_en_bas(self):
        if not self.jeu.verif_collision(self, self.jeu.tout_ennemis):
            self.rect.y += self.velocity
