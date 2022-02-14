import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob
from jeu import Jeu

pygame.init()

pygame.display.set_caption("Redemption")
ecran = pygame.display.set_mode((1080, 720))
arriere_plan = pygame.image.load('assets/highnoondarkstar.jpg')
joueur = Combattant()
jeu = Jeu()

running = True

while running:

    ecran.blit(arriere_plan,(0,0))
    ecran.blit(jeu.joueur.image,jeu.joueur.rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                jeu.joueur.bouger_a_droite()
            elif event.key == pygame.K_LEFT:
                jeu.joueur.bouger_a_gauche()
            elif event.key == pygame.K_UP:
                jeu.joueur.bouger_en_haut()
            elif event.key == pygame.K_DOWN:
                jeu.joueur.bouger_en_bas()