#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:21:11 2020

@author: brice
"""

import time
import tkinter as tk

fenetre = tk.Tk()   #défini une fenetre graphique
fenetre.title("Jeu du Minotaure")   #défini le titre de la fenetre
fenetre.geometry("700x700+100+100") #défini les dimension de la fenetre
graph = tk.Canvas(fenetre,width=500,height=500,bg='grey')   #défini un espace de dessin
graph.pack()    

class Cellule:  #défini un objet Cellule
    def __init__(self,x,y): #défini la méthode initialisation
        self.coordonnee = [x*20,y*20]   #défini l'attribut coordonnée
        self.couleur = ["green"]    #défini l'attribut couleur
            
    def affichage(self):    #défini la méthode affichage
        graph.create_rectangle(self.coordonnee[0],self.coordonnee[1],self.coordonnee[0]+2,self.coordonnee[1]+2,outline=self.couleur[0],width=12)
        #défini l'affichage de l'objet

labyrinthe = [[]] #défini une matrice labyrinthe vide
minotaure = '00'


import csv

with open('laby_exemple.csv', newline='') as csvfile:   #ouvre le fichier
    spamreader = csv.reader(csvfile)    #récupère une ligne du fichier
    for row in spamreader:              #pour chaque ligne du fichier
        labyrinthe.append(row)          #ajoute la ligne à la matrice labyrinthe
csvfile.close()                         #ferme le fichier

def affichage(matrice,n,m): #permet d'afficher le labyrinthe
    for i in range(2,n+2):  #pour chaque ligne de la matrice
        for j in range(m):      #pour chaque case d'une ligne de la matrice
            case = Cellule(j+5,i+5) #défini une case aux coordonnée j,i
            if matrice[i][j]=='99': #si la case de la matrice est libre alors:
                case.couleur[0] = "green"   #la case prend la couleur verte
            else:                   #sinon
                if matrice[i][j]=='-1':     #si la case est un mur alors:
                    case.couleur[0] = "black"   #la case prend la couler noir
                else:                       #sinon
                    case.couleur[0] = "yellow" #la case prednd la couleur jaune
            case.affichage()    #dessine la case
affichage(labyrinthe,15,11) #affiche le labyrinthe de 15 lignes et 11 colonnes

def test(labyrinthe,chaine,x,y): #permet de tester dans quelle direction le minotaure peut se déplacer
    if labyrinthe[x][y-1] == '99':  #si la case de gauche est libre alors:
        labyrinthe[x][y-1] = "0G"       #alors j'avance sur cette case
        y = y - 1                       #je déplace mon curseur sur la gauche
        chaine = chaine + "G"           #je récupère la direction
        return chaine,x,y               #retourne les coordonnées et la direction prise
    else:                           #sinon:
        if labyrinthe[x-1][y] == '99':  #si la case de devant est libre alors:
            labyrinthe[x-1][y] = "0H"       #alors j'avance sur cette case
            x = x - 1                       #je déplace mon curseur devant
            chaine = chaine + "H"           #je récupère la direction
            return chaine,x,y               #retourne les coordonnées et la direction prise
        else:                           #sinon:
            if labyrinthe[x][y+1] == '99':  #si la case de droite est libre alors:
                labyrinthe[x][y+1] = "0D"       #alors j'avance sur cette case
                y = y + 1                       #je déplace mon curseur sur la droite
                chaine = chaine + "D"           #je récupère la direction
                return chaine,x,y               #retourne les coordonnées et la direction prise
            else:                           #sinon:
                if labyrinthe[x+1][y] == '99':  #si la case arrière est libre alors:
                    labyrinthe[x+1][y] = "0B"       #alors j'avance sur cette case
                    x = x + 1                       #je déplace mon curseur en arrière
                    chaine = chaine + "B"           #je récupère la direction
                    return chaine,x,y               #retourne les coordonnées et la direction prise
                else:                           #sinon:
                    print("erreur")                 #écrit une erreur
                    return chaine,x,y               #retourne les coordonnées et la direction prise
                
def conv_dir(chaine): #permet de convertir la chaine sous le format: se déplace toujours ver l'avant et tourne sur lui-même
    chaine2 = "" #définit une chaine vide
    for i in range(len(chaine)):    #pour i parcourant la chaine
        if i > 0:                       #si i est supérieur à 0 alors:
            if chaine[i] != chaine[i-1]:    #si le caractére actuel est différent du caractère précédent alors:
                chaine2 = chaine2 + chaine[i] + 'A'     #j'ajoute le caractere actuel + le carcatère A dans la chaine2
            else:                           #sinon
                chaine2 = chaine2 + 'A'         #j'ajoute le caractere A dans chaine2
        else:                           #sinon
            chaine2 = 'A'                   #la chaine vaut A
    return chaine2                  #retourne la chaine2

def direction(x,y,sense):  #permet de récupérer les coordonnées du déplacement à effectuer 
    if sense == 'D':    #si il est tourné vers la droite alors:
        y = y + 1           #avance d'une colonne
    if sense == 'B':    #si il est tourné vers le bas alors:
        x = x + 1           #avance d'une ligne
    if sense == 'G':    #si il est tourné vers la gauche alors:
        y = y - 1           #recule d'une colonne
    if sense == 'H':    #si il est tourné vers le haut alors:
        x = x - 1           #recule d'une ligne
    return x,y          #retourne les coordonnées x et y

def rotation(i,a):  #permet d'effectuer une rotation
    if i == 'D':    #si le caractere est D alors:
        a = 0           #tourne vers la droite
    if i == 'B':    #si le caractère est B alors:
        a = 1           #tourne vers le bas
    if i == 'G':    #si le caractere est G alors:
        a = 2           #tourne vers la gauche
    if i == 'H':    #si le caractere est H alors:
        a = 3           #tourne vers le haut
    if a > 3:       #si il dépasse la liste alors:
        a = a - 4       #il reprend du début de la liste alors:
    return a        #retourne l'indice de la rotation

def lecture(matrice, chaine,x,y):   #permet de lire la chaine de direction
    orientation = ['D','B','G','H'] #défini une liste avec toutes les directions possibles
    a = 0   #on suppose qu'au début il est tourné vers la droite
    sense = orientation[a]  #récupère la direction
    for i in chaine:    #pour i parcourant la chaine faire:
        if i == 'A':        #si le caractere est A alors:
            x,y = direction(x,y,sense)  #récupère les coordonnée de la direction
            matrice[x][y] = '0A'        #avance
        else:               #sinon
            a = rotation(i,a)       #effectue une rotation
            sense = orientation[a]  #récupère la nouvelle direction
            
                       
n = 15  #nombre de lignes
m = 11  #nombre de colonnes
x = 3   #coordonnée x (3 correspond à 1 du labyrinthe)
y = 1   #coordonnée y
labyrinthe[x][y] = minotaure #place le minotaure sur la case de départ
affichage(labyrinthe,n,m)   #afiiche le labyrinthe
chaine = ""                 #définit une chaine vide

while((x!=(n)) or (y!=(m-2))): #tant que le minotaure n'atteint pas la sortie faire:
    chaine,x,y = test(labyrinthe,chaine,x,y)    #récupère les coordonnées et la direction résultante du test
    time.sleep(0.5)   #attend 1 seconde
    affichage(labyrinthe,n,m)   #affiche le labyrinthe
    fenetre.update()            #met à jour la fenetre

print(conv_dir(chaine))     #affiche la chaine des directions convertit pour la lecture du minotaure
labyrinthe2 = [[]] #défini une matrice labyrinthe2 vide

with open('laby_exemple.csv', newline='') as csvfile:   #ouvre le fichier
    spamreader = csv.reader(csvfile)    #récupère une ligne du fichier
    for row in spamreader:              #pour chaque ligne du fichier
        labyrinthe2.append(row)         #ajoute la ligne à la matrice labyrinthe2
csvfile.close()                         #ferme le fichier

x = 3   #coordonnée x (3 correspond à 1 du labyrinthe)
y = 1   #coordonnée y

labyrinthe2[x][y] = minotaure #place le minotaure sur la case de départ
affichage(labyrinthe2,n,m)      #affiche le labyrinthe

lecture(labyrinthe2,conv_dir(chaine),x,y)   
affichage(labyrinthe2,15,11)            #affiche le labyrinthe fini
fenetre.mainloop()                      #lance la fenetre