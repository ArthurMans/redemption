import pygame
from definition import *


class Projectile():

    def __init__(self, combattant, screen):
        super().__init__()
        self.velocity = 5

        self.image = pygame.image.load('assets/bdf.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen = screen

        # position du projectile par rapport à celui qui le lance
        self.largeur_image_combattant = combattant.image.get_width()
        self.hauteur_image_combattant = combattant.image.get_height()
        if combattant.est_allié:
            self.rect.x = combattant.rect.x + self.largeur_image_combattant
            self.rect.y = combattant.rect.y + (self.hauteur_image_combattant / 3)
        else:
            self.rect.x = combattant.rect.x - self.image.get_width()
            self.rect.y = combattant.rect.y + (self.hauteur_image_combattant / 3)

        self.combattant = combattant

        self.puissance_competence = 10

    def update(self):
        self.move()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def remove(self):
        for i in range(len(self.combattant.all_projectiles)):
            if self.combattant.all_projectiles[i] == self:
                self.combattant.all_projectiles.pop(i)

    def move(self):
        if self.combattant.est_allié:
            self.rect.x += self.velocity

            # verifie si le projectile n'est plus sur l'ecran
            if self.rect.x > largeur_ecran:
                self.remove()
        else:
            self.rect.x -= self.velocity

            # verifie si le projectile n'est plus sur l'ecran
            if self.rect.x < 0:
                self.remove()

        # Vérifie si le projectile touche un ennemi
        for ennemi in self.combattant.jeu.tout_ennemis:
            if ennemi.rect.colliderect(self.combattant.rect):
                # retire le projectile
                self.remove()
                # infliger des degats
                ennemi.damage(self.puissance_competence * self.combattant.puissance)

