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

        self.tout_combattants = []
        self.tout_ennemis = []
        self.tout_alliés = []

        self.arriere_plan = pygame.image.load('assets/highnoondarkstar.jpg')
        self.arriere_plan = pygame.transform.scale(self.arriere_plan, (largeur_ecran, hauteur_ecran))

        self.heros = None
        self.spawn_heros()

        self.blob = None
        self.spawn_blob(largeur_ecran-600, hauteur_ecran/2)

        self.spawn_blob(largeur_ecran-600, hauteur_ecran/3)

        self.attaque_en_cours = False
        self.dx, self.dy = 0, 0

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            print(len(self.heros.all_projectiles))
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
            for ennemi in self.tout_ennemis:
                if not self.heros.rect.colliderect(ennemi.rect):
                    self.heros.rect.x += self.dx
                    self.heros.rect.y += self.dy
                else:
                    ennemi.damage(20)
                    self.attaque_en_cours = False

    def update(self):
        for combattant in self.tout_combattants:
            combattant.update()

    def draw(self):  # Construction graphiques
        self.screen.blit(self.arriere_plan, (0, 0))
        for combattant in self.tout_combattants:
            combattant.draw()
        pygame.display.flip()

    def spawn_blob(self, x, y):
        self.blob = Blob(self, x, y)
        self.tout_ennemis.append(self.blob)
        self.tout_combattants.append(self.blob)

    def spawn_heros(self):
        self.heros = Heros(self)
        self.tout_combattants.append(self.heros)
        self.tout_alliés.append(self.heros)
