import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, combattant):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('assets/bdf.png')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.largeur_image = self.image.get_width()
        self.hauteur_image = self.image.get_height()
        if combattant.est_allié:
            self.rect.x = combattant.rect.x 
            self.rect.y = combattant.rect.y
        else:
            self.rect.x = combattant.rect.x
            self.rect.y = combattant.rect.y