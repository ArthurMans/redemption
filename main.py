import pygame
from combattants.combattant import Combattant
from combattants.blob import Blob

pygame.init()

pygame.display.set_caption("Redemption")
pygame.display.setmode((1080, 720))
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()