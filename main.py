import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob
from jeu import Jeu
from definition import *

pygame.init()

pygame.display.set_caption("Redemption")
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
arriere_plan = pygame.image.load('assets/highnoondarkstar.jpg')
joueur = Combattant()
jeu = Jeu()

running = True

while running:

    #appliquer la fenetre du jeu
    ecran.blit(arriere_plan,(0,0))

    #appliquer image combattant
    ecran.blit(jeu.combattant.image,jeu.combattant.rect)

    #recuperer projectile du combattant
    for projectile in jeu.combattant.all_projectiles:
        projectile.move()

    #appliquer l'ensemble des images des projectiles
    jeu.combattant.all_projectiles.draw(ecran)

    #mettre à jour l'ecran
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                jeu.combattant.bouger_a_droite()
            elif event.key == pygame.K_LEFT:
                jeu.combattant.bouger_a_gauche()
            elif event.key == pygame.K_UP:
                jeu.combattant.bouger_en_haut()
            elif event.key == pygame.K_DOWN:
                jeu.combattant.bouger_en_bas()
            if event.key == pygame.K_SPACE:
                jeu.combattant.lancer_projectile()