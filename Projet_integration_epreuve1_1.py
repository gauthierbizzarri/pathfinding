#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:09:31 2020

@author: brice
"""
labyrinthe = [[]] #défini une matrice labyrinthe vide
minotaure = '00'

import csv

with open('laby_exemple.csv', newline='') as csvfile:   #ouvre le fichier
    spamreader = csv.reader(csvfile)    #récupère une ligne du fichier
    for row in spamreader:              #pour chaque ligne du fichier
        labyrinthe.append(row)          #ajoute la ligne à la matrice labyrinthe
csvfile.close()                         #ferme le fichier

def affichage(matrice):
    for i in range(2,17):
        for j in range(11):
            print(matrice[i][j],end='|')
        print("")
    print("\n")
 
def test(labyrinthe,chaine,x,y):
#    print(labyrinthe[x][y-1])
    if labyrinthe[x][y-1] == '99':
        print("G")
        labyrinthe[x][y-1] = "0G"
        y = y - 1
        chaine = chaine + "G"
        return chaine,x,y
    else:
#        print(labyrinthe[x-1][y])
        if labyrinthe[x-1][y] == '99':
            print("H")
            labyrinthe[x-1][y] = "0H"
            x = x - 1
            chaine = chaine + "H"
            return chaine,x,y
        else:
#            print(labyrinthe[x][y+1])
            if labyrinthe[x][y+1] == '99':
                print("D")
                labyrinthe[x][y+1] = "0D"
                y = y + 1
                chaine = chaine + "D"
                return chaine,x,y
            else:
#                print(labyrinthe[x+1][y])
                if labyrinthe[x+1][y] == '99':
                    print("B")
                    labyrinthe[x+1][y] = "0B"
                    x = x + 1
                    chaine = chaine + "B"
                    return chaine,x,y
                else:
                    print("erreur")
                    return chaine,x,y

def deplacement(labyrinthe, chaine, x, y):
    for car in chaine:
        if car == 'G':
            if labyrinthe[x][y-1] == '99':
                labyrinthe[x][y-1] = "0G"
                y = y - 1
            else:
                print("parcours incorect")
                break
        elif car == 'H':
            if labyrinthe[x-1][y] == '99':
                labyrinthe[x-1][y] = "0H"
                x = x - 1
            else:
                print("parcours incorect")
                break
        elif car == 'D':
            if labyrinthe[x][y+1] == '99':
                labyrinthe[x][y+1] = "0D"
                y = y + 1
            else:
                print("parcours incorect")
                break   
        elif car == 'B':
            if labyrinthe[x+1][y] == '99':
                labyrinthe[x+1][y] = "0B"
                x = x + 1
            else:
                print("parcours incorect")
                break
        
        
               
affichage(labyrinthe)
labyrinthe[3][1] = minotaure
x = 3
y = 1
#affichage(labyrinthe)
chaine = ""

"""while(((x!=3) and (y!=9)) or ((x!=15) and (y!=9)) or ((x!=15) and (y!=1))):
#for i in range(50):
    chaine,x,y = test(labyrinthe,chaine,x,y)
    affichage(labyrinthe)"""
    
#    affichage(labyrinthe)
    
print(chaine)
