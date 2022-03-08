from theme import Meteo
from theme import Traduction
from theme import Crypto
from theme import Blague
from theme import PierrePapierCiseau

from gestion import rechercheTheme
from erreur import erreur

class GestionTheme:
    def __init__(self):

        self.theme = {"meteo": Meteo.Meteo(),
                      "traduction": Traduction.Traduction(),
                      "crypto":Crypto.Crypto(),
                      "blague":Blague.Blague(),
                      "pierrePapierCiseau":PierrePapierCiseau.PierrePapierCiseau()}

        self.themesTrouves = []

    def themesTrouvesAction(self):
        if len(self.themesTrouves) > 1:
            raise erreur.ToManyThemeFind(self.themesTrouves)
        else:
            self.themesTrouves[0]["theme"].action()

    def themesTrouvesSetElement(self):
        for theme in self.themesTrouves:
            theme["theme"].setElement(theme["element"])

    def verifierTheme(self, texte: str):
        """
            Entree: texte (str)
            Sortie: list
            Fonction: retourne la liste des themes possible present dans un texte
        """
        self.themesTrouves = rechercheTheme.RechercheTheme(self,texte).get()
        return self.themesTrouves

    def getAllReconnaisseur(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne la liste de tous les mot reconnaisseur des theme de facon unique
        """
        listeReconnaisseur = []
        for theme in self.theme.values():
            for mot in theme.getReconnaisseur():
                if mot not in listeReconnaisseur:
                    listeReconnaisseur.append(mot)
        return listeReconnaisseur

    def getAllConnecteur(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne la liste de tous les mot connecteur des theme de facon unique
        """
        listeConnecteur = []
        for theme in self.theme.values():
            for mot in theme.getConnecteur():
                if mot not in listeConnecteur:
                    listeConnecteur.append(mot)
        return listeConnecteur

    def getAllUrl(self):
        """
            Entree:
            Sortie: list
            Fonction: retourne la liste de tous les url des theme de facon unique
        """
        listeUrl = []
        for theme in self.theme.values():
            listeUrl.append(theme.api.URL)
        return listeUrl
