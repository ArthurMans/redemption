import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob

pygame.init()

pygame.display.set_caption("Redemption")
pygame.display.set_mode((1080, 720))
running = True

while running:

    jeu.combattant.all_projectiles.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jeu.combattant.lancer_projectile()