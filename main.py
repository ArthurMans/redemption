import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob
from combattants.heros import Heros
from jeu import Jeu
from definition import *


pygame.init()

timer = pygame.time.Clock()

pygame.display.set_caption("Redemption")
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
arriere_plan = pygame.image.load('assets/highnoondarkstar.jpg')
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_ecran, hauteur_ecran))

jeu = Jeu()

combattant_select = False
running = True

while running:

    # appliquer la fenetre du jeu
    ecran.blit(arriere_plan, (0, 0))

    if attaque_en_cours:
        if not jeu.verif_collision(jeu.heros, jeu.tout_ennemis):
            jeu.heros.rect.x += dx
            jeu.heros.rect.y += dy
        else:
            jeu.blob.damage(20)
            attaque_en_cours = False
    # appliquer image heros
    ecran.blit(jeu.heros.image, jeu.heros.rect)

    # appliquer images ennemis
    jeu.tout_ennemis.draw(ecran)

    # actualisère barre de PV
    for element in jeu.tout_combattants:
        element.update_barre_de_vie(ecran)

    # recuperer projectile du heros
    for projectile in jeu.heros.all_projectiles:
        projectile.move()

    # appliquer l'ensemble des images des projectiles
    jeu.heros.all_projectiles.draw(ecran)

    # mis à jour
    pygame.display.flip()

    for event in pygame.event.get():
        (mx, my) = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()
        if not attaque_en_cours:
            if event.type == pygame.KEYDOWN:
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
        if not combattant_select:
            if jeu.blob.rect.collidepoint((mx, my)) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                bouton1 = pygame.Rect(850, 1000, 200, 50)
                arriere_plan.blit(jeu.bouton_attaque.image, (850, 1000))
                combattant_select = True
        if combattant_select:
            if bouton1.collidepoint((mx, my)):
                pygame.draw.rect(arriere_plan, (255, 255, 255), (850, 1000, 200, 50), 2)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    attaque_en_cours = True
                    dx, dy = jeu.heros.vitesse_deplacement(jeu.blob)
                    combattant_select = False

    timer.tick(FPS)

