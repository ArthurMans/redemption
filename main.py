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
bouton_attaque = pygame.image.load('assets/attaque.jpg')
arriere_plan = pygame.image.load('assets/highnoondarkstar.jpg')
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_ecran, hauteur_ecran))
jeu = Jeu()


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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                xmin = jeu.blob.rect.x
                xmax = jeu.blob.rect.x + jeu.blob.rect.width
                ymin = jeu.blob.rect.y
                ymax = jeu.blob.rect.y + jeu.blob.rect.height
                if xmin <= pygame.mouse.get_pos()[0] <= xmax and ymin <= pygame.mouse.get_pos()[1] <= ymax:
                    arriere_plan.blit(bouton_attaque, (850,1000))
                    pos_bouton_attaque = bouton_attaque.get_rect(topleft=(850,1000))
                if pos_bouton_attaque[0] <= pygame.mouse.get_pos()[0] <= pos_bouton_attaque[0]+pos_bouton_attaque[2] and pos_bouton_attaque[1] <= pygame.mouse.get_pos()[1] <= pos_bouton_attaque[1]+pos_bouton_attaque[3]:
                    arriere_plan.blit(bouton_attaque, (0,0))
                    attaque_en_cours = True
                    dx, dy = jeu.heros.vitesse_deplacement(jeu.blob)

    timer.tick(FPS)

