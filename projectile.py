import pygame

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