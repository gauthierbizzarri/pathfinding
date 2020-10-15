"""
y = ax + b
equation du premier degres
il faut recuperer le point a et b
je te fixe un point dans l'espace dans x et y
il a une abcisse qui vaut xc et yc
le but est que je te demande qu'est ce que je met devant le x dans ma fonction pour pouvoir trouver ce point
on me demande de trouver le coefficient directeur
b = 0
on veut ax
"""
import matplotlib.pyplot as plt

graph = plt #objet plt

def calcule_A(pxc, pyc):
    print("")
    a = 0.0
    a = float(pyc)/float(pxc)

    liste_de_point_ord = []
    liste_de_point_abs = []
    
    ordplus = 0.0
    absplus = pxc - 1 #valeur max des abs = pxc - 1
    
    for i in range(1, pxc):
        liste_de_point_abs.append(i) #append sur les abs

    for i in range(1, pxc):
        a = float(i)/float(a)
        liste_de_point_ord.append(a*i) #append sur les ord
        if ordplus < (a*i): #condition pour obtenir la valeur max des ord
            ordplus = a*i
    
    graph.plot(liste_de_point_abs, liste_de_point_ord) #trace la courbe des points
    return absplus, ordplus #retourne les coordonnées du dernier point de la courbe

def check_A(pxc, pyc, px, py):
    coord = calcule_A(pxc, pyc) #récupération des coordonnées de pxc & pyx
    result_color = '' #couleur en fonction du resultat: gagnié = vert | raté = rouge
    
    if coord[0] == px and coord[1]== py: #comparaison avec les coordonnées utilisateur
        print("gagné")
        result_color = 'green'
    else:
        print("raté")
        result_color = 'red'
        
    graph.scatter(px,py, s=30, c=result_color, marker='X') #affichage de la cible
    graph.plot([1,coord[0]], [1,coord[1]], "-", c=result_color) #affichage trajectoire

