import math
import matplotlib.pyplot as plt
import matplotlib as MatPlotLib
import time
import matplotlib.image as mpimg
import tkinter as tk
MatPlotLib.use('TkAgg')

def Mort(graph,fenetre):
    M=float(input('Choisir MODE  de jeu : 0 : laser , 1 , mortier')) #On inscrit le mode de jeu
    if M ==0 : 
        g=0
        xcible = int(input("Distance de la cible en mètres : ") )    #input de la coordonnées x de la cible
        ycible = int(input("La hauteur  de la cible en mètres : ") )    #input de la coordonnées y de la cible 
    if M==1:
        g=9.81
        xcible = int(input("Distance de la cible en mètres : ") )    #input de la coordonnées x de la cible 
        ycible =0
      
    v = float(input("vitesse initiale ? : ") )                  #input la vitesse initiale 
    t=0                                                         # On initialise le temps à 0 
    cpt=0                                                      #on initialise un compteur à 0 
    TétaD =float(input("Angle de tir en degré ?  : "))            #On input un angle e tir en degré
    TétaR=TétaD*3.141592 /180
    TétaR=truncate(TétaR,3)                                         # on convertir l'angle en radian en faisant un petit arrondi au passage 
        #listes necessaires:
    X=[]      #liste des abscisses 
    Y=[]     #liste des ordonnées
    XA=[]    #Liste des abscisses atteintes 
    SOL=[0]   #liste modélisant le sol 
    T=[0]    #liste des temps 
    if g==9.81:
        tfinal=(v*math.sin(TétaR)) / (g*2) # temps que met le projectile à atteindre le sol 
        tfinal=truncate(tfinal, 2)      #petit arrondi
    if g==0:
        tfinal=2
    pas = truncate(tfinal/50,10)    #pas de temps on aura 50 points ici
    xfinal=int(delta(v,TétaR))      #calcul du point d'impact

    #TETASOL=0.5*(math.asin((2*xcible*g)/(v**2)))

    #################################### JEU DU MORTIER #########################################
    if g==9.81:
            
        for x in range (0,xfinal):
            t=t+pas #avancement du temps 
            xa=v*(math.cos(TétaR))*t #calcul de la position sur les abscisses
            xa=truncate(xa,10) #Petit arrondi pour bien faire les choses 
            X.append(x) #On rajoute pour les axes
            T.append(t)#on rajoute pour le temps 
            print(xa)
            
            y=-0.5*g *( (x**2) / ((v**2) *(( math.cos(TétaR))**2))) + x*math.tan(TétaR)  # Calcul de la hauteur 
            y=truncate(y,2)                                                         #Je le met en arrondi à E-2
            XA.append(xa)                                                           #Je calcule les abscisses atteintes
            Y.append(y)                                                             #Je calcul les orodnnées atteintes
            SOL.append(0)                                                           #Je modélise le sol 
            cpt=cpt+1
            
            
            
            
            ############# PARTIE GRAPHIQUE 

            plt.title('Le lancé')
            plt.figure()                                                   #C'est le titre
            plt.plot(XA,Y ,linestyle = 'dashed')# trajectoire en pointillés
            plt.plot(SOL) #affiche le sol 
            plt.plot(xcible,ycible,linestyle = 'none', marker = 'o', c = 'red',markersize = 10) #affiche la cible
            time.sleep(0.002)
            plt.plot(0,0,marker='$ Tank $',c='black',markersize=5)
            plt.savefig('graphique.png') ; plt.close()
            courbe = tk.PhotoImage(file='graphique.png',master=fenetre)
            graph.create_image(300, 300, image = courbe)
            graph.image = courbe
            fenetre.update()
            #mpimg.imsave("graphique.jpg",['255'])
            #plt.show()   
            
            
            
            
            ##########On sort de la boucle pour afficher le résultat final 
        plt.plot(xcible,[0],linestyle = 'none', marker = 'o', c = 'red',markersize = 10) #affiche la cible
        plt.plot(0,0,marker='$ [|8|] $',c='black',markersize=50)                          #afficher le motif du canon 
        plt.plot(XA[-1],[0],linestyle = 'none', marker = 'X', c = 'orange',markersize = 10) #affiche l'impact)
        
        
        
        
        plt.title('Le jeu du Mortier') 
        plt.plot(XA,Y ,linestyle = 'dashed')
        plt.plot(SOL) #affiche le sol 
        plt.show()
        print('la cible est à',xcible)
        print('tu as lancé à ',v,'mètres seconde', 'avec un angle de ' , TétaD,'degrés')
            
        
    
        if testsol(Y)==False: # teste si le tir est raté et le boulet tombe dans le sol 
            print('Lobus a manqué ! Tu étais à ',xcible-XA[-1],'mètres')    
            AIDE=int(input('Voulez vous une aide ? -> IE je vous donne langle à une vitesse fixée  : ENTRER 1 pour OUI ENTRER 0 pour NON '))  
            #if AIDE ==1:
                #print('il faut lancer le projectile pour une vitesse de ',v,'il faut un angle de ',TETASOL)
                    
                
                
        if testsol(Y)==True:
            print('lobus a touché le sol  :) ! ') 
        if testcible(xcible,XA)==True:
            print('Bravo tu as touché la cible')
        else : 
            print('Lobus a manqué ! Tu étais à ',xcible-XA[-1],'mètres')

    ###################### JEU LASER ####################################
    if g==0:
        for x in range (0,xfinal):
            t=t+pas #avancement du temps 
            xa=v*(math.cos(TétaR))*t #calcul de la position sur les abscisses
            xa=truncate(xa,10) #Petit arrondi pour bien faire les choses 
            X.append(x) #On rajoute pour les axes
            T.append(t)#on rajoute pour le temps 
            
            
            y=-0.5*g *( (x**2) / ((v**2) *(( math.cos(TétaR))**2))) + x*math.tan(TétaR)  # Calcul de la hauteur 
            y=truncate(y,2)                                                         #Je le met en arrondi à E-2
            XA.append(xa)                                                           #Je calcule les abscisses atteintes
            Y.append(y)                                                             #Je calcul les orodnnées atteintes
            SOL.append(0)                                                           #Je modélise le sol 
            cpt=cpt+1
            
            
            
            ######################## PARTIE GRAPHIQUE #####################
            plt.title('Le lancé')                                                   #C'est le titre
            plt.plot(XA,Y ,linestyle = 'dashed')# trajectoire en pointillés
            plt.plot(SOL) #affiche le sol 
            plt.plot(xcible,ycible,linestyle = 'none', marker = 'o', c = 'red',markersize = 4) #affiche la cible
            time.sleep(0.002)
            plt.plot(0,0,marker='$ Laser $',c='black',markersize=5)
            plt.show()
            
            
            if testlaser(xcible,XA,Y,ycible)==True:
                print('Bravo tu as touché la cible')
                print(XA)
                plt.title('Le jeux du laser') 
                plt.plot(XA,Y ,linestyle = 'dashed', markersize=4)
                plt.plot(SOL) #affiche le sol 
                plt.show()
                
                
                    
            if XA[-1]>xcible+10:
                return ( 'on arrête là on est trop loin')
        
    #Quand on a fini de boucler on a fini le jeu ! 
        plt.plot(0,0,marker='$ <0> $',c='black',markersize=5)                          #afficher le motif du canon 
        plt.plot(xcible,ycible,linestyle = 'none', marker = 'o', c = 'red',markersize = 4) #affiche la cible
        plt.plot(0,0,marker='$ [|LASER|]$',c='black',markersize=15)
        
        
        
            
        
            
        
        if testlaser(xcible,XA,Y,ycible)==True:
            plt.title('Le jeux du laser') 
            plt.plot(XA,Y ,linestyle = 'dashed')
            plt.plot(SOL) #affiche le sol 
            plt.show()
            print('la cible est à',xcible ,'et à ',ycible,'mètres de hauteur')
            print('tu as lancé à ',v,'mètres seconde')

            return('Bravo tu as touché la cible')
        else : 
                
            plt.title('Le jeux du laser') 
            plt.plot(XA,Y ,linestyle = 'dashed')
            plt.plot(SOL) #affiche le sol 
            plt.show()
            print('la cible est à',xcible ,'et à ',ycible,'mètres de hauteur')
            print('tu as lancé à ',v,'mètres seconde')
            return('domamge tu as raté la cible ')






############# FONCTIONS NECESSAIRE #####################
def testsol(Y):         #teste si le bouelt atteint le sol pour le jeu du mortier
    if Y[-1]< 0:
        return True 
    else : 
        return False 
def testcible(xcible,XA):           #test si le boulet du mortier atteint la cible au sol 
    if XA[-1]< xcible-2.1 or XA[-1]>xcible+2.1 :
        return False 
    else : 
        return False 
def delta(v,TétaR):             # solveur équation 2nd degré 
    a=((-0.5)*9.81 )/ ((v**2)*(math.cos(TétaR))**2)
    b=math.tan(TétaR)
    c=0
    d=(b**2) - 4*a*c
    X1=(-b-math.sqrt(d) )/ (2*a)
    X2=(-b+math.sqrt(d) )/ (2*a)
    if X1>0:
        return(X1)
    else : 
        return(X2)
        
def truncate(n, decimals=0):        #fonction faisant un arrondi  à un nombre de virgules près 
    multiplier = 10*decimals
    return int(n* multiplier)/multiplier


def testlaser(xcible,XA,Y,ycible):      #teste si le laser touche la cible à X+/- 4 et Y+/-4
    
    if XA[-1]<xcible-4 or XA[-1]>xcible+4:
        return False 
    else  :
        if Y[-1]<ycible -4 or Y[-1]>ycible+4:
            return False 
        else : 
            return True 
        
class Mortier:      
    def __init__(self,graph,fenetre):
        Mort(graph,fenetre)

