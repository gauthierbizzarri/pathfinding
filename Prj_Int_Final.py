#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:35:31 2020

@author: brice
"""

import time
import tkinter as tk
import random as randint
import missile

#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////// FENETRE /////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////

fenetre = tk.Tk()                                           #défini une fenetre graphique
fenetre.title("Jeu du Minotaure")                           #défini le titre de la fenetre
fenetre.geometry("700x700+100+100")                         #défini les dimension de la fenetre
graph = tk.Canvas(fenetre,width=500,height=500,bg='grey')   #défini un espace de dessin
graph.pack()    

pos=[-1,-1]

def afficher_laser_game():
    print("laser")

def afficher_mortier():
    print("mortier")
    
class Labyrinthe:   #permet de définir un objet labyrinthe existant
    def __init__(self,n,m,matrice): #initialise un labyrinthe non découvert
        self.couleur = ["black"]             #initialise la couleur en noir
        self.taille = [n,m]                  #initialise la taille
        for i in range(2,self.taille[0]+2):  #pour chaque ligne de la matrice
            for j in range(self.taille[1]):      #pour chaque case d'une ligne de la matrice
                case = Cellule(j+1,i+1)             #défini une case aux coordonnée j,i
                case.couleur[0] = self.couleur[0]   #définit la couleur de la case
                case.affichage()                    #dessine la case
        
    def affichage(self,matrice,n,m):
        for i in range(2,n+2):      #pour chaque ligne de la matrice
            for j in range(m):          #pour chaque case d'une ligne de la matrice
                case = Cellule(j+1,i+1)     #défini une case aux coordonnée j,i
                if matrice[i][j]=='99':     #si la case de la matrice est libre alors:
                    case.couleur[0] = "green"   #la case prend la couleur verte
                    case.affichage()            #dessine la case
                else:                       #sinon
                    if matrice[i][j]=='-1':     #si la case est un mur alors:
                        case.couleur[0] = "black"   #la case prend la couler noir
                        case.affichage()            #dessine la case
                    else:                       #sinon
                        if matrice[i][j]=='100':    #si la case contient la valeur 100 alors:
                            case.couleur[0]="red"       #la case prend la couleur rouge
                            case.affichage()            #dessine la case
                        else:                       #sinon
                            case.couleur[0] = "yellow"  #la case prend la couleur jaune
                            case.affichage()            #dessine las case

        
class Cellule:  #défini un objet Cellule
    def __init__(self,x,y):             #défini la méthode initialisation
        self.coordonnee = [x*20,y*20]       #défini l'attribut coordonnée
        self.couleur = ["green"]            #défini l'attribut couleur
            
    def affichage(self):    #défini la méthode affichage
        graph.create_rectangle(self.coordonnee[0],self.coordonnee[1],self.coordonnee[0]+2,self.coordonnee[1]+2,outline=self.couleur[0],width=18)
                                #défini l'affichage de l'objet

labyrinthe = [[]] #défini une matrice labyrinthe vide
minotaure = '1'
#//////////////////////////////////////////////////////////////////////////////

import csv

with open('../Laby_Eval.csv', newline='') as csvfile:   #ouvre le fichier
    spamreader = csv.reader(csvfile)                        #récupère une ligne du fichier
    for row in spamreader:                                  #pour chaque ligne du fichier
        labyrinthe.append(row)                                  #ajoute la ligne à la matrice labyrinthe
        
csvfile.close()                        #ferme le fichier
matrice = Labyrinthe(19,14,labyrinthe) #initialise l'objet Labyrinthe
fenetre.update()                       #rafraichi la fenetre
time.sleep(1.0)                        #attend 1 secondes

#//////////////////////////////////////////////////////////////////////////////
#/////////////////////////////// FONCTIONS ////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////

#////////////////////////// ENTREE UTILISATEUR ////////////////////////////////


def keyH(event): #détecte l'appuie sur la touche haut
    global Haut  #défini la variable global Haut
    Haut = True  #Haut prend la valeur True

def keyB(event): #détecte l'appuie sur la touche bas
    global Bas   #défini la variable global Bas
    Bas = True   #Bas prend la valeur True

def keyD(event): #détecte l'appuie sur la touche droite
    global Droite #défini la variable global Droite
    Droite = True #Droite prend la valeur True

def keyG(event): #détecte l'appuie sur la touche gauche
    global Gauche #défini la variable global Gauche
    Gauche = True #Gauche prend la valeur True


def Entrer(x,y,matrice,Haut,Bas,Gauche,Droite): #test la case en fonction des touches directionnelles
    c,d = x,y           #conserve les coordonnées du minotaure
    if Haut == True:    #si j'appuie sur Haut alors:

        x = x - 1           #je regarde la case du haut
        if matrice[x][y] != '-1':#si la case est libre alors:
            indication["text"] = "" #je n'affiche rien
            return x,y,True         #je retourne les coordonnées de la case
        else:                   #sinon:
            indication["text"] = "Mur"  #j'affiche "Mur"
            return c,d,False            #je retourne les coordonnées du minotaure
    else:               #sinon
        if Bas == True:     #si j'appuie sur Bas alors:
            x = x + 1           #je regarde la case du bas
            if matrice[x][y] != '-1':#si la case est libre alors:
                indication["text"] = "" #je n'affiche rien
                return x,y,True         #je retourne les coordonnées de la case
            else:                   #sinon:
                indication["text"] = "Mur"  #j'affiche "Mur"
                return c,d,False            #je retourne les coordonnées du minotaure
        else:               #sinon:
            if Droite == True:  #si j'appuie sur Droite alors:
                y = y + 1           #je regarde la case de droite
                if matrice[x][y] != '-1':#si la case est libre alors:
                    indication["text"] = "" #je n'affiche rien
                    return x,y,True         #je retourne les coordonnées de la case
                else:                   #sinon:
                    indication["text"] = "Mur"  #j'affiche "Mur"
                    return c,d,False            #je retourne les coordonnées du minotaure
            else:               #sinon:
                if Gauche == True:  #si j'appuie sur Gauche alors:
                    y = y -1            #je regarde la case de droite
                    if matrice[x][y] != '-1':#si la case est libre alors:
                        indication["text"] = "" #je n'affiche rien
                        return x,y,True         #je retourne les coordonnées de la case
                    else:                   #sinon:
                        indication["text"] = "Mur"  #j'affiche "Mur"
                        return c,d,False            #je retourne les coordonnées du minotaure
                else:               #sinon:
                    return c,d,False    #je retourne les coordonnées du minotaure
    
fenetre.bind("<Up>",keyH)       #établit le lien entre la touche directionnelle haut et la fonction keyH
fenetre.bind("<Down>",keyB)     #établit le lien entre la touche directionnelle bas et la fonction keyB
fenetre.bind("<Left>",keyG)     #établit le lien entre la touche directionnelle gauche et la fonction keyG
fenetre.bind("<Right>",keyD)    #établit le lien entre la touche directionnelle droite et la fonction keyD
aficher_laser_gameBTN = tk.Button(fenetre, text = 'Ouvrir laser game', command=afficher_laser_game())
aficher_laser_gameBTN.place(x = 100, y = 510)
aficher_mortierBTN = tk.Button(fenetre, text = 'Ouvrir mortier', command=afficher_mortier())
aficher_mortierBTN.place(x = 100, y = 550)

#//////////////////////////////////////////////////////////////////////////////

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
                        case.couleur[0]="yellow"       #la case prend la couleur rouge
                        case.affichage()            #dessine la case
                    else:                       #sinon
                        #case2.couleur[0] = "green"
                        #case2.affichage()
                        case.couleur[0] = "yellow" #la case prednd la couleur jaune
                        case.affichage()            #dessine las case
                        #case2 = case
                        
def creation(matrice,n,m,x,y):      #permet de générer un labyrinthe aléatoire
    orientation = ['D','H','G','B']     #liste de toutes les directions
    matrice[x][y] = '99'                #la case prend la valeur '99'
    sense = orientation[randint.randint(0,3)]   #récupère une direction aléatoire
    x,y = direction(x,y,sense,n,m)      #récupère les nouvelles coordonnées
    if (x == n) and (y == m-2):         #si j'atteint la case de sortie alors:
        matrice[x][y] = '99'                #la case prend la valeur '99'
        return matrice                      #retourne le matrice
    else:                               #sinon:
        return creation(matrice,n,m,x,y)    #retourne elle-même
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
def lepluscourt(matrice,a,liste,cpt,n,m):   #modifie la matrice pour avoir le chmein le plus court
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
                liste2[0],liste2[1] = direction(liste[i][0],liste[i][1],sense,n,m)#je récupère les coordonnée de la case voisine dans cette liste
                if matrice[liste2[0]][liste2[1]]=='99': #si la case est libre alors:
                    matrice[liste2[0]][liste2[1]]= str(cpt) #je place la valeur de mon compteur
                    liste3.append(liste2)                   #j'ajoute mes nouveaux coordonnées dans ma liste3
        return lepluscourt(matrice,a,liste3,cpt+1,n,m)  #retourne ma fonction avec ma nouvelle liste et j'incrémente mon compteur de 1
    
    
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

def direction(x,y,sense,n,m):  #permet de récupérer les coordonnées du déplacement à effectuer 
    if (sense == 'D') and (y!=m-2):    #si il est tourné vers la droite alors:
        y = y + 1           #avance d'une colonne
        return x,y          #retourne les coordonnées x et y
    if (sense == 'B') and (x!=n):    #si il est tourné vers le bas alors:
        x = x + 1           #avance d'une ligne
        return x,y          #retourne les coordonnées x et y
    if (sense == 'G') and (y!=1):    #si il est tourné vers la gauche alors:
        y = y - 1           #recule d'une colonne
        return x,y          #retourne les coordonnées x et y
    if (sense == 'H') and (x!=3):    #si il est tourné vers le haut alors:
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

def Jeu(laby,n,m,pos): #permet de parcourir un labyrinthe
    x = 3   #coordonnée x (3 correspond à 1 du labyrinthe)
    y = 1   #coordonnée y
    global Haut  #définit les variables des touches directionnelles 
    global Bas
    global Droite
    global Gauche
    while((x!=(n)) or (y!=(m-2))):  #tant je ne suis pas sortie du labyrinthe
        time.sleep(0.1)     #attend 100 milisecondes
        x,y,etat = Entrer(x,y,laby,Haut,Bas,Gauche,Droite) #récupère les coordonnées
        Haut = False        #initilise les touches sur false à chaque tour
        Bas = False
        Droite = False
        Gauche = False
        laby[x][y] = '100' #mes la valeur 100 dans la nouvelle case
        case = Cellule(y+1,x+1)     
        case.couleur[0] = "red" #change la couleur de la case
        case2 = Cellule(pos[0], pos[1])
        case2.couleur[0] = "yellow"
        case2.affichage()
        pos = [y+1,x+1]
        case.affichage()            #dessine la case
        fenetre.update()            #rafraichie la fenetre
    return laby             #retourne le labyrinthe


#//////////////////////////////////////////////////////////////////////////////
#/////////////////////// PROGRAMME PRINCIPAL //////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////
    
#/////////////////////////// INITIALISATION ///////////////////////////////////                      
n = 19  #nombre de lignes
m = 14  #nombre de colonnes4
x = 3   #coordonnée x (3 correspond à 1 du labyrinthe)
y = 1   #coordonnée y
cpt = 1 #initialise le compteur à 1
Haut = False  #initialise les touches directionnelles à false
Bas = False
Droite = False
Gauche = False

chaine = ""                 #définit une chaine vide
a = 0   #on suppose qu'au début il est tourné vers la droite
liste = [[n,m-2]]
indication = tk.Label(fenetre, text = '',font='arial 26')   #créer un label indiquant si l'on touche un mur
indication.place(x = 400, y = 200)                          #définit la position du label

#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////// PROGRAMME ///////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////

Jeu(labyrinthe,n,m,pos)         #lance le premier labyrinthe
affichage(labyrinthe,n,m)   #dessine le labyrinthe terminé
fenetre.update()          #rafraichie la fenetre
time.sleep(3)
graph.destroy()             #attend 3 secondes
graph = tk.Canvas(fenetre,width=500,height=500,bg='grey')   #défini un espace de dessin
graph.pack()
missile.Mortier(graph,fenetre) 
#courbe = tk.PhotoImage(file='unnamed.png')
#graph.create_image(300, 300, image = courbe)
#graph.image = courbe
fenetre.update()
time.sleep(3) 
graph.destroy()             #attend 3 secondes
graph = tk.Canvas(fenetre,width=500,height=500,bg='grey')   #défini un espace de dessin
graph.pack() 
x = 3   #coordonnée x (3 correspond à 1 du labyrinthe)
y = 1   #coordonnée y
labyrinthe = [['-1' for i in range(m)] for j in range(n+2)] #initialise une matrice

for i in range(2,n+2):                              #pour i de 2 à n+2 faire:
    for j in range(m):                                  #pour j de 0 à m faire:
        if (i==2) or (i==n) or (j==0) or (j==m-2):          #si je suis sur un bord de la matrice alors:
            labyrinthe[i][j] = '-1'                             #la case prend la valeur '-1'
            
labyrinthe = creation(labyrinthe,n,m,x,y)   #crée un labyrinthe aléatoire
matrice2 = Labyrinthe(n,m,labyrinthe)       #initialise l'objet Labyrinthe
fenetre.update()                            #rafraichie la fenetre
Jeu(labyrinthe,n,m,pos)                         #lance le second labyrinthe
affichage(labyrinthe,n,m)                   #affiche le labyrinthe terminé
fenetre.update()                            #rafraichie la fenetre
time.sleep(3)                               #attend 3 seconde
lepluscourt(labyrinthe,a,liste,cpt,n,m)     #modifie la matrice pour effectuer le chemin le plus court
sense = 'D'                                 #initialise le sens de départ
cpt = 100                                   #initilialise le compteur à 100

while((x!=(n)) or (y!=(m-3))):     #tant que le minotaure n'as pas atteint la sortie faire:
    chaine,x,y,cpt = test(labyrinthe,chaine,x,y,cpt)    #effectue le chemin le plus court et retourne les coordonnée de chaque case
    time.sleep(0.2)                                     #attend 200 miliseconde
    affichage(labyrinthe,n,m)                           #affiche le labyrinthe
    fenetre.update()                                    #met à jour la fenetre
    
print(chaine)               #écrit la chaine
sense = chaine[0]           #récupère la première direction
print(conv_dir(chaine))     #affiche la chaine des directions convertit pour la lecture du minotaure
"""
labyrinthe2 = [[]] #défini une matrice labyrinthe2 vide

#Affichage labyrinth
    
with open('Laby_Eval2.csv', newline='') as csvfile:   #ouvre le fichier
    spamreader = csv.reader(csvfile)    #récupère une ligne du fichier
    for row in spamreader:              #pour chaque ligne du fichier
        labyrinthe2.append(row)         #ajoute la ligne à la matrice labyrinthe2
csvfile.close()                         #ferme le fichier

x = 3   #coordonnée x (3 correspond à 1 du labyrinthe)
y = 1   #coordonnée y

labyrinthe3[x][y] = minotaure #place le minotaure sur la case de départ
affichage(labyrinthe2,n,m)      #affiche le labyrinthe

lecture(labyrinthe2,conv_dir(chaine),sense,x,y)   #suit les instructions de la chaine pour sortir du labyrinthe
affichage(labyrinthe2,n,m,)            #affiche le labyrinthe fini

fenetre.update()            #met à jour la fenetre
"""

fenetre.update()            #met à jour la fenetre

