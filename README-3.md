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
    
