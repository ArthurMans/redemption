import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob
from combattants.heros import Heros
from jeu import Jeu
from definition import *

pygame.init()

pygame.display.set_caption("Redemption")
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
arriere_plan = pygame.image.load('assets/highnoondarkstar.jpg')
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_ecran, hauteur_ecran))
jeu = Jeu()


running = True

while running:

    # appliquer la fenetre du jeu
    ecran.blit(arriere_plan, (0, 0))

    # appliquer image heros
    ecran.blit(jeu.heros.image, jeu.heros.rect)

    # appliquer images ennemis
    jeu.tout_ennemis.draw(ecran)

    # actualisère barre de PV
    for element in jeu.tout_combattants:
        element.update_barre_de_vie(ecran)

    #recuperer projectile du heros
    for projectile in jeu.heros.all_projectiles:
        projectile.move()

    # appliquer l'ensemble des images des projectiles
    jeu.heros.all_projectiles.draw(ecran)




    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            if event.key == pygame.K_RIGHT and jeu.heros.rect.x + jeu.heros.rect.width < ecran.get_width():
                jeu.heros.bouger_a_droite()
            elif event.key == pygame.K_LEFT and jeu.heros.rect.x > 0:
                jeu.heros.bouger_a_gauche()
            elif event.key == pygame.K_UP and jeu.heros.rect.y > 0:
                jeu.heros.bouger_en_haut()
            elif event.key == pygame.K_DOWN and jeu.heros.rect.y + jeu.heros.rect.height < ecran.get_height():
                jeu.heros.bouger_en_bas()
            if event.key == pygame.K_SPACE:
                jeu.heros.lancer_projectile()
