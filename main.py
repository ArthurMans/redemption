import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob
from combattants.heros import Heros
from jeu import Jeu
from definition import *



pygame.init()

timer = pygame.time.Clock()

pygame.display.set_caption("Redemption")
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
jeu = Jeu(screen, timer)

running = True


while running:

    jeu.run()

