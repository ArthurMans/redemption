import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob
from jeu import Jeu

pygame.init()

pygame.display.set_caption("Redemption")
ecran = pygame.display.set_mode((1080, 720))
arriere_plan = pygame.image.load('assets/highnoondarkstar.jpg')
jeu = Jeu()


running = True

while running:

    ecran.blit(arriere_plan,(0,0))
    jeu.combattant.all_projectiles.draw(ecran)

    ecran.blit(jeu.joueur.image,jeu.joueur.rect)

    for blob in jeu.tout_monstres:
         blob.avance()

    jeu.tout_monstres.draw(ecran)

    if jeu.appui.get(pygame.K_RIGHT) and jeu.joueur.rect.x + jeu.joueur.rect.width < ecran.get_width():
        jeu.joueur.bouger_a_droite()
    elif jeu.appui.get(pygame.K_LEFT) and jeu.joueur.rect.x > 0:
        jeu.joueur.bouger_a_gauche()
    elif jeu.appui.get(pygame.K_UP) and jeu.joueur.rect.y > 0:
        jeu.joueur.bouger_en_haut()
    elif jeu.appui.get(pygame.K_DOWN) and jeu.joueur.rect.y + jeu.joueur.rect.height < ecran.get_height():
        jeu.joueur.bouger_en_bas()

    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            jeu.appui[event.key] = True
        elif event.type == pygame.KEYUP:
            jeu.appui[event.key] = False
