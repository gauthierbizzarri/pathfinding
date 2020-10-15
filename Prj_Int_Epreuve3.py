#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:19:09 2020

@author: brice
"""

import time
import tkinter as tk

#//////////////////////////////// Fenetre /////////////////////////////////////

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
        graph.create_rectangle(self.coordonnee[0],self.coordonnee[1],self.coordonnee[0]+2,self.coordonnee[1]+2,outline=self.couleur[0],width=18)
        #défini l'affichage de l'objet

labyrinthe = [[]] #défini une matrice labyrinthe vide
minotaure = '1'

#//////////////////////////////////////////////////////////////////////////////

import csv

with open('../Laby_Eval.csv', newline='') as csvfile:   #ouvre le fichier
    spamreader = csv.reader(csvfile)    #récupère une ligne du fichier
    for row in spamreader:              #pour chaque ligne du fichier
        labyrinthe.append(row)          #ajoute la ligne à la matrice labyrinthe
csvfile.close()                         #ferme le fichier

#/////////////////////////////// Fonctions ////////////////////////////////////

def affichage(matrice,n,m): #permet d'afficher le labyrinthe
    #case2 = Cellule(1+5,3+5)
    for i in range(2,n+2):  #pour chaque ligne de la matrice
        for j in range(m):      #pour chaque case d'une ligne de la matrice
            case = Cellule(j+1,i+1) #défini une case aux coordonnée j,i
            if matrice[i][j]=='99': #si la case de la matrice est libre alors:
                case.couleur[0] = "green"   #la case prend la couleur verte
                case.affichage()   #dessine la case
            else:                   #sinon
                if matrice[i][j]=='-1':     #si la case est un mur alors:
                    case.couleur[0] = "black"   #la case prend la couler noir
                    case.affichage()   #dessine la case
                else:                      #sinon
                    if matrice[i][j]=='100':    #si la case contient la valeur 100 alors:
                        case.couleur[0]="red"       #la case prend la couleur rouge
                        case.affichage()            #dessine la case
                    else:                       #sinon
                        #case2.couleur[0] = "green"
                        #case2.affichage()
                        case.couleur[0] = "yellow" #la case prednd la couleur jaune
                        case.affichage()            #dessine las case
                        #case2 = case
            
affichage(labyrinthe,15,11) #affiche le labyrinthe de 15 lignes et 11 colonnes

"""
def murGauche(matrice,chaine,x,y,a,sense,cpt): #permet d'effectuer le chmein le plus court
    orientation=['D','H','G','B']   #liste contenant toutes les directions
    sense = orientation[a]          #récupère la direction dans laquelle le minotaure regarde     
    c,d = x,y                       #conserve les coordonnée du minotaure
    x,y=direction(x,y,sense)        #calcule les coordonnée de la prochaine case
    if matrice[x][y] != '-1':       #si la nouvelle case n'est pas un mur alors:
        if int(matrice[x][y]) < cpt:    #si sa valeur et plus faible que mon compteur alors:
            cpt = int(matrice[x][y])        #cpt prend la valeur de la case
            matrice[c][d]='0'
            sense = orientation[a]
            x,y=direction(x,y,sense)
        else:
            a = a +1
            if a==4:
                a=0
            sense = orientation[a]
            x,y=c,d
    else:
        a = a +1
        if a==4:
            a=0
        x,y=c,d
    return x,y,a,cpt,sense
"""
def lepluscourt(matrice,a,liste,cpt):   #modifie la matrice pour avoir le chmein le plus court
    orientation = ['D','H','G','B']     #liste contenant toutes les directions
    liste3 = []                         #liste vide
    affichage(matrice,19,14)            #affiche le labyrinthe
    time.sleep(0.2)             #attend 200 miliseconde
    fenetre.update()
    if liste == []:                     #si ma liste est vide alors:
        return 'none'                       #retourne rien
    else:                               #sinon:
        for i in range(len(liste)):         #pour i de 0 à la longueur de la liste faire:
            for j in range(4):                  #pour j de 0 à 4 (4 directions) faire:
                a = a+1                             #j'incrémente a de 1
                if a==4:                            #si a dépasse 3
                    a= 0                                #il revient à 0
                sense = orientation[a]              #je récupère la nouvelle direction
                liste2 = [0,0]                      #j'initialise une liste à 0
                liste2[0],liste2[1] = direction(liste[i][0],liste[i][1],sense)#je récupère les coordonnée de la case voisine dans cette liste
                if matrice[liste2[0]][liste2[1]]=='99': #si la case est libre alors:
                    matrice[liste2[0]][liste2[1]]= str(cpt) #je place la valeur de mon compteur
                    liste3.append(liste2)                   #j'ajoute mes nouveaux coordonnées dans ma liste3
        return lepluscourt(matrice,a,liste3,cpt+1)  #retourne ma fonction avec ma nouvelle liste et j'incrémente mon compteur de 1
    
    
def test(labyrinthe,chaine,x,y,cpt): #permet de tester dans quelle direction le minotaure peut se déplacer
    if (labyrinthe[x][y-1] != '-1')and(int(labyrinthe[x][y-1]) < cpt):  #si la case de gauche est libre et que sa valeur est plus petite que mon compteur alors:
        cpt = int(labyrinthe[x][y-1])   #je récupère la valeur de la case dans mon compteur
        labyrinthe[x][y-1] = "100"      #alors j'avance sur cette case
        y = y - 1                       #je déplace mon curseur sur la gauche
        chaine = chaine + "G"           #je rempli ma chaine avec la direction
    else:                           #sinon:
        if (labyrinthe[x-1][y] != '-1')and(int(labyrinthe[x-1][y]) < cpt):  #si la case de devant est libre et que sa valeur est plus petite que mon compteur alors:
            cpt = int(labyrinthe[x-1][y])   #je récupère la valeur de la case dans mon compteur
            labyrinthe[x-1][y] = "100"      #alors j'avance sur cette case
            x = x - 1                       #je déplace mon curseur devant
            chaine = chaine + "H"           #je rempli ma chaine avec la direction
        else:                           #sinon:
            if (labyrinthe[x][y+1] != '-1')and(int(labyrinthe[x][y+1]) < cpt):  #si la case de droite est libre et que sa valeur est plus petite que mon compteur alors:
                cpt = int(labyrinthe[x][y+1])   #je récupère la valeur de la case dans mon compteur 
                labyrinthe[x][y+1] = "100"      #alors j'avance sur cette case
                y = y + 1                       #je déplace mon curseur sur la droite
                chaine = chaine + "D"           #je rempli ma chaine avec la direction
            else:                           #sinon:
                if (labyrinthe[x+1][y] != '-1')and(int(labyrinthe[x+1][y]) < cpt):  #si la case arrière est libre et que sa valeur est plus petite que mon compteur alors:
                    cpt = int(labyrinthe[x+1][y])   #je récupère la valeur de la case dans mon compteur
                    labyrinthe[x+1][y] = "100"      #alors j'avance sur cette case
                    x = x + 1                       #je déplace mon curseur en arrière
                    chaine = chaine + "B"           #je rempli ma chaine avec la direction
    return chaine,x,y,cpt               #retourne les coordonnées, le compteur et la chaine de directions
                
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
        return x,y          #retourne les coordonnées x et y
    if sense == 'B':    #si il est tourné vers le bas alors:
        x = x + 1           #avance d'une ligne
        return x,y          #retourne les coordonnées x et y
    if sense == 'G':    #si il est tourné vers la gauche alors:
        y = y - 1           #recule d'une colonne
        return x,y          #retourne les coordonnées x et y
    if sense == 'H':    #si il est tourné vers le haut alors:
        x = x - 1           #recule d'une ligne
    return x,y         #retourne les coordonnées x et y

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

def lecture(matrice,chaine,sense,x,y):   #permet de lire la chaine de direction
    orientation = ['D','B','G','H'] #défini une liste avec toutes les directions possibles
    for i in range(len(orientation)):   #pour i de 0 à la longueur de la liste faire:
        if sense == orientation[i]:         #si le sens et égal à la valeur de la liste alors:
            a = i                               #récupère l'indice de la liste
    for i in chaine:    #pour i parcourant la chaine faire:
        if i == 'A':        #si le caractere est A alors:
            x,y = direction(x,y,sense)  #récupère les coordonnée de la direction
            matrice[x][y] = '0A'        #avance
        else:               #sinon
            a = rotation(i,a)       #effectue une rotation
            sense = orientation[a]  #récupère la nouvelle direction
            
#/////////////////////////// Initialisation ///////////////////////////////////                      
n = 19  #nombre de lignes
m = 14  #nombre de colonnes
x = 3   #coordonnée x (3 correspond à 1 du labyrinthe)
y = 1   #coordonnée y
cpt = 1 #initialise le compteur à 1
affichage(labyrinthe,n,m)   #affiche le labyrinthe
chaine = ""                 #définit une chaine vide
a = 0   #on suppose qu'au début il est tourné vers la droite
liste = [[n,m-2]]

#/////////////////////// Programme Principal //////////////////////////////////

lepluscourt(labyrinthe,a,liste,cpt)    #modifie la matrice pour effectuer le chemin le plus court
sense = 'D'                             #initialise le sens de départ
cpt = 100                               #initilialise le compteur à 100
while((x!=(n)) or (y!=(m-3))):          #tant que le minotaure n'as pas atteint la sortie faire:
    chaine,x,y,cpt = test(labyrinthe,chaine,x,y,cpt)    #effectue le chemin le plus court et retourne les coordonnée de chaque case
    time.sleep(0.2)             #attend 200 miliseconde
    affichage(labyrinthe,n,m)   #affiche le labyrinthe
    fenetre.update()            #met à jour la fenetre
print(chaine)
sense = chaine[0]  
print(conv_dir(chaine))     #affiche la chaine des directions convertit pour la lecture du minotaure

labyrinthe2 = [[]] #défini une matrice labyrinthe2 vide

with open('../Laby_Eval.csv', newline='') as csvfile:   #ouvre le fichier
    spamreader = csv.reader(csvfile)    #récupère une ligne du fichier
    for row in spamreader:              #pour chaque ligne du fichier
        labyrinthe2.append(row)         #ajoute la ligne à la matrice labyrinthe2
csvfile.close()                         #ferme le fichier

x = 3   #coordonnée x (3 correspond à 1 du labyrinthe)
y = 1   #coordonnée y

labyrinthe2[x][y] = minotaure #place le minotaure sur la case de départ
affichage(labyrinthe2,n,m)      #affiche le labyrinthe

lecture(labyrinthe2,conv_dir(chaine),sense,x,y)   #suit les instructions de la chaine pour sortir du labyrinthe
affichage(labyrinthe2,n,m,)            #affiche le labyrinthe fini
fenetre.update()            #met à jour la fenetre