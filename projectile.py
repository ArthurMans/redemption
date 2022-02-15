import pygame
from definition import *

class Projectile(pygame.sprite.Sprite):

    def __init__(self, combattant):
        super().__init__()
        self.velocity = 5


        self.image = pygame.image.load('assets/bdf.png')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()

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

    def remove(self):
        self.combattant.all_projectiles.remove(self)

    def move(self):
        if self.combattant.est_allié:
            self.rect.x += self.velocity

            #verifie si le projectile n'est plus sur l'ecran
            if self.rect.x > largeur_ecran:
                self.remove()
        else:
            self.rect.x -= self.velocity

            # verifie si le projectile n'est plus sur l'ecran
            if self.rect.x < 0:
                self.remove()