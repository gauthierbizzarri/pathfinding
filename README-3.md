# **PROJET D'INTEGRATION**
    
## *Initialisation*
    
    En premier lieu la variable du minautore est créée et nous mettons en place une matrice labyrinthe vide.
    Nous importons ensuite la matrice (fichier csv). Une mise en forme de la matrice est également réalisée.
    Le labyrinthe est réaliser.

## *Etude des fonctions*
    
    La fonction def test va permettre au minautore de tester les différentes directions dans lesquelles il peut 
    se déplacer. A chaque test de direction le minautore va établir les directions disponibles et avancer en fonction des 
    cases libres et de l'ordre de priorité. Nous stockons également la direction prise afin de pouvoir afficher le chemin 
    complet du minautore en fin de parcours.
    
    La fonction def conv_dir permet elle de convertir la chaine de direction en format "Avancer,Rotation"
    
## *Résumé première partie*
    
    Notre programme permet d'afficher chaque matrice correspondant à chaque déplacement du minautore afin de toujours 
    pouvoir le situer dans le labyrinthe.
    La chaine de caractère finale nous montre les mouvements du minautore en fonction de son avancée et des directions prises.
    
## *Deuxième partie*
    
    Ici le programme se divise en trois fonctions.
        - Une fonction définissant les déplacements à effectuer en fonction de la chaine récupérée.
        - Une fonction permettant au minautore d'effectuer les rotations présentes dans la chaine.
        - Une fonction permettant de lire la chaine de direction donnée.
    
    Suite à ces trois fonctions notre minautore va parcourir le labyrinthe en fonction des indications données jusqu'à qu'il
    trouve la sortie ou qu'il se bloque, dans ce cas un message d'erreur apparaîtra.
    
    Encore une fois nous affichons chaque matrice représentant la position du minautore dans le labyrinthe.
    
## *Troisième partie*
    Cette partie est consacrée à l'interface graphique en utilisant le mode tkinter.
    L'objectif étant de mettre en forme le labyrinthe pour que l'utilisateur puisse visualiser le jeu en temps réel. 
        -Une fonction scanne le labyrinthe ligne par ligne et affecte une couleur à chaque valeur de la cellule  :
            -si la valeur est 99 : vert 
            -si la valeur est -1 : noir 
            -si la valeur est  0 : jaune
        -La fonction sleep() extraite du module time nous permet de "mettre un temps de latence " que l'on a définit .
        -Pour finir nous avons imaginer afficher une fenêtre présentant le parcours du minotaure :
            -On utilise le module Tkinter avec les fonction title , canvas et geometry , 3 méthodes issues du module permettant respectivement de 
                -> afficher un titre 
                -> afficher une fenêtre aux dimensions définies 
                -> défini un espace de dessin 
    
## *Quatrième partie*
    Cette partie est dédiée à la recherche du plus court chemin .
    On s'initialise à la sortie du labyrinthe et on parcour progressivement les chemns libres en affectant à chaque case un compteur croissant qui s'arrêtera lors que le chemin s'arrête et donc quand le minautore touchera un mur . 
    Les chemins libres seront parcourus et seront continués jusqu'à ce que l'entrée soit atteinte . Le plus court chemin sera donc la suite de chiffres partant de l'arrivée dont le premier élément est le plus petit parmis les chemins possibles . 
    
    