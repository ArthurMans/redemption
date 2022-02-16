import pygame
import sys
from combattants.combattant import Combattant
from combattants.blob import Blob
from combattants.heros import Heros
from definition import *


class Jeu:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.tout_combattants = pygame.sprite.Group()
        self.tout_ennemis = pygame.sprite.Group()
        self.tout_alliés = pygame.sprite.Group()

        self.arriere_plan = pygame.image.load('assets/highnoondarkstar.jpg')
        self.arriere_plan = pygame.transform.scale(self.arriere_plan, (largeur_ecran, hauteur_ecran))

        self.heros = None
        self.spawn_heros()

        self.blob = None
        self.spawn_blob()

        self.attaque_en_cours = False
        self.dx, self.dy = 0, 0

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():  # Si on clique sur la croix pour quitter, on arrete le jeu
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.heros.lancer_projectile()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.attaque_en_cours = True
                self.dx, self.dy = self.heros.vitesse_deplacement(self.blob)
        if self.attaque_en_cours:
            if not self.verif_collision(self.heros, self.tout_ennemis):
                self.heros.rect.x += self.dx
                self.heros.rect.y += self.dy
            else:
                self.blob.damage(20)
                self.attaque_en_cours = False

    def update(self):
        for combattant in self.tout_combattants:
            combattant.update()
        for projectile in self.heros.all_projectiles:
            projectile.move()


    def draw(self):  # Construction graphiques
        self.screen.blit(self.arriere_plan, (0, 0))
        for combattant in self.tout_combattants:
            combattant.draw()
        self.heros.all_projectiles.draw(self.screen)
        pygame.display.flip()

    def verif_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_blob(self):
        self.blob = Blob(self)
        self.tout_ennemis.add(self.blob)
        self.tout_combattants.add(self.blob)

    def spawn_heros(self):
        self.heros = Heros(self)
        self.tout_combattants.add(self.heros)
        self.tout_alliés.add(self.heros)
