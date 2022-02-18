import pygame

class Bouton():

    def __init__(self, jeu):
        self.jeu = jeu
        self.nom = ''
        self.image = pygame.image.load('assets/attaque.jpg')
        self.rect = self.image.get_rect()

    #def events(self):


    #def update(self):


    #def draw(self):
