class Combattant:

    def __init__(self, pv, nom):
        self.pv = pv
        self.nom = nom
        #self.robustesse
        #self.puissance
        #self.endurance
        #self.perception
        #self.reactivite
        #self.parade

    def afficher_combattant(self):
        print("nom :",self.nom,"||  pv :",self.pv)
