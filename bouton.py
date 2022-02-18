import pygame
from definition import *
from combattants.combattant import Combattant

class Bouton(): #class Objet_cliquable(self):

    def __init__(self, jeu, x, y, image, screen):
        self.entité_select = False
        self.jeu = jeu
        self.screen = screen
        self.nom = ''
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def events(self):
        mx, my = pygame.mouse.get_pos()
        if not self.entité_select:
            if self.rect.collidepoint((mx, my)) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                bouton1 = pygame.Rect(850, 1000, 200, 50)
                arriere_plan.blit(jeu.bouton_attaque.image, (850, 1000))
                self.entité_select = True
        if self.entité_select:
            if bouton1.collidepoint((mx, my)):
                pygame.draw.rect(arriere_plan, (255, 255, 255), (850, 1000, 200, 50), 3)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    attaque_en_cours = True
                    dx, dy = jeu.heros.vitesse_deplacement(jeu.blob)
                    self.entité_select = False
                    arriere_plan.blit(jeu.bouton_attaque.image, (850, 1000))
            else:
                arriere_plan.blit(jeu.bouton_attaque.image, (850, 1000))


    def update(self):
        return False


    def draw(self):
        return False

