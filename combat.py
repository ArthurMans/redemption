from definition import *
from random import randrange

class Combat():


    def __init__(self, screen,  clock, liste_combattants):
        self.screen = screen
        self.clock = clock

        self.liste_combattants = liste_combattants

        self.nouveau_tour = True
        self.tour = 0
        self.priorité = []

        self.arriere_plan = pygame.image.load('assets/highnoondarkstar.jpg')
        self.arriere_plan = pygame.transform.scale(self.arriere_plan, (largeur_ecran, hauteur_ecran))

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():  # Si on clique sur la croix pour quitter, on arrete le jeu
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update(self):
        if self.nouveau_tour:
            self.creation_priorité()
            print(self.liste_combattants)
            self.nouveau_tour = False


    def draw(self):
        self.screen.blit(self.arriere_plan, (0, 0))
        for combattant in self.liste_combattants:
            self.screen.blit(combattant.image, combattant.rect)
        # for bouton in self.liste_boutons:
        #     self.screen.blit(bouton.image, bouton.rect)
        # A implementer
        pygame.display.flip()


    def creation_priorité(self):
        for i in range(0, len(self.liste_combattants) - 1):
            liste_ex_aequo = []
            nb_ex_aequo = 0
            pos_max = i
            for j in range(i + 1, len(self.liste_combattants)):
                if self.liste_combattants[j].reactivite > self.liste_combattants[pos_max].reactivite:
                    if nb_ex_aequo != 0:
                        liste_ex_aequo = []
                        nb_ex_aequo = 0
                    pos_max = j
                elif self.liste_combattants[j].reactivite == self.liste_combattants[pos_max].reactivite:
                    if nb_ex_aequo == 0:
                        nb_ex_aequo = 2
                        liste_ex_aequo.append(self.liste_combattants[pos_max])
                    elif nb_ex_aequo >= 2:
                        nb_ex_aequo += 1
                    liste_ex_aequo.append(self.liste_combattants[j])
            if (pos_max != i):
                if nb_ex_aequo != 0:
                    pos_combattant = randrange(0, len(liste_ex_aequo))
                    self.liste_combattants[i], self.liste_combattants[pos_combattant] = self.liste_combattants[pos_combattant], self.liste_combattants[i]
                else:
                    tmp = self.liste_combattants[i]
                    self.liste_combattants[i] = self.liste_combattants[pos_max]
                    self.liste_combattants[pos_max] = tmp