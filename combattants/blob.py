from combattant import Combattant

class Blob(Combattant):

    def __init__(self):
        self.pv = 30
        self.nom = 'Blob'

    def afficher_combattant(self,nom):
        self.nom = nom
        print("nom :",self.nom)

