# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import math





class Joueur:
    
    def __init__(self,argentDepart,nomJoueur):
        self.argent=argentDepart
        self.argentMise=0
        self.nom=nomJoueur
        self.cartes=[]
        self.estCouche=True

    def getArgent(self):
        print(self.argent)
        
    def mise(self):
        self.argentMise=math.floor(self.argent*0.1)
        self.argent-=self.argentMise
        return self.argentMise



class MaitreDuJeu:
    
    def __init__(self,listeJoueurInitiale):
        self.listeJoueurs=listeJoueurInitiale
        self.paquetDeCarte=[]
        self.tapis=[]
        self.couleurs=["coeur","carreau","trefle","pique"]
        self.valeurs=["2","3","4","5","6","7","8","9","10","valet","dame","roi","1"]
        
    def lancePartie(self):
        #initialisaer la partie
        #Tant que > 1 joueur : faire partie
        #annoncer vaincueur
        
    def initPaquet():
        
        for c in range(len(self.couleurs)):
            for v in range(len(self.valeurs)):
                self.paquetDeCarte.append((v,c))
        
    def distribueJoueur():
        for joueur in self.listeJoueurs:
            


        
joueur1=Joueur(100,"Jojo")
joueur2=Joueur(50,"Juju")

maitre=MaitreDuJeu([joueur1,joueur2])