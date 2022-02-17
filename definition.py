import pygame


largeur_ecran = 1920
hauteur_ecran = 1080
FPS = 60

attaque_en_cours = False

click = False



def afficher_image(screen, image, x=0, y=0):
    picture = pygame.image.load(image).convert_alpha()
    screen.blit(picture, (x, y))

def cliquer(bouton):
    if bouton.collidepoint((mx,my)):
        pygame.draw.rect(ecran, (255,255,255), ())
