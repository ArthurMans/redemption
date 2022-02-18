import pygame
from definition import *

class Bouton():

    def __init__(self, jeu):
        self.jeu = jeu
        self.nom = ''
        self.image = pygame.image.load('assets/attaque.jpg')
        self.rect = self.image.get_rect()

    def events(self):
        if not combattant_select:
            if jeu.blob.rect.collidepoint((mx, my)) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                bouton1 = pygame.Rect(850, 1000, 200, 50)
                arriere_plan.blit(jeu.bouton_attaque.image, (850, 1000))
                combattant_select = True
        if combattant_select:
            if bouton1.collidepoint((mx, my)):
                pygame.draw.rect(arriere_plan, (255, 255, 255), (850, 1000, 200, 50), 3)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    attaque_en_cours = True
                    dx, dy = jeu.heros.vitesse_deplacement(jeu.blob)
                    combattant_select = False
                    arriere_plan.blit(jeu.bouton_attaque.image, (850, 1000))
            else:
                arriere_plan.blit(jeu.bouton_attaque.image, (850, 1000))


    #def update(self):


    #def draw(self):

