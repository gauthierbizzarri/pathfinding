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

def calcule_A(pxc, pyc):
    print("")
    a = 0.0
    a = float(pyc)/float(pxc)

    liste_de_point_ord = []
    liste_de_point_abs = []
    
    for i in range(1, pxc):
        liste_de_point_abs.append(i)

    for i in range(1, pxc):
        a = float(i)/float(a)
        liste_de_point_ord.append(i)
    
#    return liste_de_point_ord,liste_de_point_abs
 
    plt.plot(liste_de_point_abs, liste_de_point_ord)
    plt.show(())
