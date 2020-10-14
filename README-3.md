# **PROJET D'INTEGRATION**
    
## *Initialisation*
    
    En premier lieu la variable du minautore est créé et nous mettons en place une matrice labyrinthe vide.
    Nous importons ensuite la matrice (fichier csv). Une mise en forme de la matrice est également réalisé.
    Le labyrinthe est réaliser.

## *Etude des fonctions*
    
    La fonction def test va permettre au minautore de tester les différentes directions dans le quel il peut 
    se déplacer. A chaque test de direction le minautore va établir les directon disponible et avancer en fonction des 
    cases libres et de l'ordre de priorité. Nois stockons également la direction prise afinn de pouvoir afficher le chemin 
    complet du minautore en fin de parcours.
    
    La fonction def conv_dir permet elle de convertir la chaine de direction en format "Avancer,Rotation"
    
## *Résumé première partie*
    
    Notre programme permet d'afficher chaque matrice correspondant à chaque déplacement du minautore afin de toujours 
    pouvoir le situer dans le labyrinthe.
    La chaine de caractère final nous montre les mouvements du minautore en fonction de son avancer et des directions prises.
    
## *Deuxième partie*
    
    Ici le programme se divise en trois fonctions.
        - Une fonction définissant les déplacements à effectuer en fonction de la chaine récupérer.
        - Une fonction permettant au minautore d'effectuer les rotations présentes dans la chaine.
        - Une fonction permettant de lire la chaine de direction donnée.
    
    Suite à ces trois fonctions notre minautore va parcourir le labyrinthe en fonction des indications données jusqu'à qu'il
    trouve la sortie ou qu'il se bloque, dans ce cas un message d'erreur apparaitra.
    
    Encore une fois nous affichons chaque matrice représentant la position du minautore dans le labyrinthe.
    
## **Troisième partie*
    Cette partie est consacrée à l'interface graphique en utilisant le mode tkinter.
    L'objectif étant de mettre en forme le labyrinthe pour que l'utilisateur puisse visualiser le jeu en temps réel. 
        -Une fonction scanne le labyrinthe lignes par lignes et affecte une couleur à chaque valeur de la cellule  :
            -si la valeur est 99 : vert 
            -si la valeur est -1 : noir 
            -si la valeur est  0 : jaune
        -La fonction sleep() extraite du module time nous permet de "mettre un temps de latence " que l'on a définit .
        -Pour finir nous avons imaginer afficher une fenêtre présentant le parcours du minotaure :
            -On utilise le module Tkinter avec les fonction title , canvas et geometry , 3 méthodes issues du module permettant respectivement de 
                -> afficher un titre 
                -> afficher une fenêtre aux dimensions définies 
                -> défini un espace de dessin 
    
