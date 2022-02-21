import pygame
from definition import*
pygame.init()

timer = pygame.time.Clock()

pygame.display.set_caption("Redemption")
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

surface = pygame.image.load('assets/highnoondarkstar.jpg')
sprite_sheet = pygame.image.load("assets\Warrior\SpriteSheet\Warrior_SheetnoEffect.png")

surface.blit(sprite_sheet, (50, 100), (0, 0, 20, 20))
surface.blit(sprite_sheet, (70, 100), (20, 0, 20, 20))

