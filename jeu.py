import pygame
import sys
from combattants.combattant import Combattant
from combattants.blob import Blob
from combattants.heros import Heros
from definition import *
from bouton import Bouton
from combat import Combat


class Jeu:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.arriere_plan = pygame.image.load('assets/highnoondarkstar.jpg')
        self.arriere_plan = pygame.transform.scale(self.arriere_plan, (largeur_ecran, hauteur_ecran))

        self.toutes_entités = []

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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #lancement d'un combat
                self.liste_combattants = [Blob(largeur_ecran-600, hauteur_ecran/3, 2), Heros(), Blob(largeur_ecran-600, hauteur_ecran/2, 3)]
                self.combat = Combat(self.screen, self.clock, self.liste_combattants)
                self.combat.run()

    def update(self):
        return

    def draw(self):  # Construction graphiques
        self.screen.blit(self.arriere_plan, (0, 0))
        pygame.display.flip()
