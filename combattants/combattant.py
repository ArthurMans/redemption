import pygame
from projectile import Projectile


class Combattant(pygame.sprite.Sprite):

    def __init__(self, jeu, est_allié=True):
        super().__init__()
        self.jeu = jeu
        self.screen = self.jeu.screen
        self.pv_max = 100
        self.pv = 100
        self.nom = ''

        # allié à gauche, ennemmi à droite
        self.est_allié = est_allié
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.all_projectiles = pygame.sprite.Group()
        self.rect.x = 450
        self.rect.y = 200
        self.velocity = 0.005

        self.robustesse = 0.98
        self.puissance = 1
        # self.endurance
        # self.perception
        # self.reactivite
        # self.parade

        if self.est_allié:
            self.groupe_allié = self.jeu.tout_alliés
            self.groupe_ennemi = self.jeu.tout_ennemis
        else:
            self.groupe_allié = self.jeu.tout_ennemis
            self.groupe_ennemi = self.jeu.tout_alliés

        self.attaque_en_cours = False

    def update(self):
        return False

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.barre_de_vie(self.screen)

    def vitesse_deplacement(self, combattant):
        dx = (combattant.rect.x - self.rect.x) * self.velocity
        dy = (combattant.rect.y - self.rect.y) * self.velocity
        return dx, dy


    # def attaque_basique(self, combattant):
    #     while


    def damage(self, montant):
        # infliger les degats
        self.pv -= montant * self.robustesse

        # vérifier si pv <=0
        if self.pv <= 0:
            # Supprimer combattant
            self.kill()


    def barre_de_vie(self, surface):
        longueur_barre_de_vie = 200
        bon_placement_barre_hp = [self.rect.x, self.rect.y - 10, longueur_barre_de_vie, 5]
        bon_placement_barre_hp_coloré = [self.rect.x, self.rect.y - 10, (self.pv * longueur_barre_de_vie) / self.pv_max, 5]
        pygame.draw.rect(surface, (81, 71, 71), bon_placement_barre_hp)
        if self.pv >= 0.75 * self.pv_max:
            # afficher barre de hp verte quand t'es quasi full life
            pygame.draw.rect(surface, (44, 205, 44), bon_placement_barre_hp_coloré)
        elif self.pv >= 0.50 * self.pv_max:
            # afficher barre de hp jaune quand t'es mid life
            pygame.draw.rect(surface, (255, 236, 0), bon_placement_barre_hp_coloré)
        elif self.pv >= 0.25 * self.pv_max:
            # afficher barre de hp orange quand t'es mal
            pygame.draw.rect(surface, (255, 128, 0), bon_placement_barre_hp_coloré)
        elif self.pv > 0:
            # afficher barre de hp rouge quand t'es dans la barba-sauce
            pygame.draw.rect(surface, (236, 15, 15), bon_placement_barre_hp_coloré)

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

