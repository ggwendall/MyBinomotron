#Ces lignes importent les modules nécessaires à l'exécution du programme. `random` est utilisé pour mélanger la liste des étudiants, 
#`mysql.connector` est utilisé pour se connecter et interroger une base de données MySQL, `math` est utilisé pour arrondir la taille du groupe 
#et `datetime` est utilisé pour obtenir le courant date.
import random
import mysql.connector
import math
import datetime



#Ce code tente d'établir une connexion à une base de données MySQL à l'aide du module `mysql.connector`. 
# Il spécifie l'hôte, le nom d'utilisateur, le mot de passe, le nom de la base de données et le numéro de port auquel se connecter. Le bloc `try` est 
# utilisé pour gérer toutes les exceptions qui peuvent se produire pendant le processus de connexion, telles que des identifiants de connexion incorrects 
# ou une base de données qui n'est pas disponible.
try:
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="example",
        database="binomotron",
        port="3307"
    )
    
    
    #`cache_apprenants = {}` initialise un dictionnaire vide appelé `cache_apprenants`. Ce dictionnaire sera utilisé pour stocker les adresses e-mail des 
    # étudiants pour une utilisation future, de sorte que le programme n'a pas besoin d'interroger la base de données chaque fois que l'adresse e-mail d'un 
    # étudiant est demandée.
    cache_apprenants = {}
    
#Ce bloc de code gère l'exception qui peut survenir lors d'une tentative de connexion à la base de données à l'aide du module `mysql.connector`. 
# Si une erreur se produit, il imprimera un message indiquant l'erreur qui s'est produite. La partie `as erreur` du code affecte le message d'erreur à 
# la variable `erreur` afin qu'il puisse être utilisé dans l'instruction print.
except mysql.connector.Error as erreur:
    print(f"Erreur de connexion à la base de données : {erreur}")

#`mycursor = connexion.cursor()` crée un objet curseur qui nous permet d'exécuter des requêtes SQL sur la base de données connectée par `connexion`.
mycursor = connexion.cursor()


#Ce bloc de code crée un objet curseur à l'aide de la connexion à la base de données "connexion" et exécute une requête SELECT pour récupérer la colonne "nom" (nom) 
# de la table "apprenants" de la base de données. Il récupère ensuite tous les résultats à l'aide de la méthode `fetchall()` et les stocke dans une liste 
# appelée `bdd_apprenants`. Ce code récupère essentiellement une liste de tous les noms des étudiants dans la base de données. L'instruction `with` est 
# utilisée pour s'assurer que le curseur est correctement fermé après l'exécution de la requête.
with connexion.cursor() as curseur:
    curseur.execute("SELECT nom FROM apprenants")
    bdd_apprenants = [ligne[0] for ligne in curseur.fetchall()]

#La fonction `former_groupes` prend en entrée une liste d'`apprenants` (apprenants) et un nombre de `nombre_groupes` (nombre de groupes). 
# Il mélange aléatoirement la liste des apprenants à l'aide de la fonction `random.shuffle()`, puis calcule la `taille_groupe` (taille du groupe) en divisant 
# la longueur de la liste des apprenants par le nombre de groupes et en arrondissant à l'entier le plus proche à l'aide de la fonction `math.ceil()`.
#  Il crée ensuite une liste de groupes `groupes` en utilisant une compréhension de liste pour diviser la liste mélangée des apprenants en sous-listes 
# de taille `taille_groupe`. Enfin, il renvoie la liste des groupes.
def former_groupes(apprenants, nombre_groupes):
    random.shuffle(apprenants)
    taille_groupe = math.ceil(len(apprenants) / nombre_groupes)
    groupes = [apprenants[i:i+taille_groupe] for i in range(0, len(apprenants), taille_groupe)]
    return groupes

#La fonction `demander_nombre_groupes()` demande à l'utilisateur de saisir le nombre de groupes souhaité, puis de convertir cette entrée en entier avant de la renvoyer.
def demander_nombre_groupes():
    nombre_groupes = int(input("Entrez le nombre de groupes souhaités : "))
    return nombre_groupes

#La fonction `afficher_groupes()` prend en entrée une liste de groupes et imprime chaque groupe sur une nouvelle ligne avec un en-tête indiquant le numéro du groupe.
#  Il utilise une boucle "for" pour itérer sur chaque groupe de la liste, et une boucle "for" interne pour itérer sur chaque étudiant du groupe. 
# Il imprime ensuite le numéro de groupe et le nom de chaque élève du groupe à l'aide de f-strings. Enfin, il imprime une ligne vierge pour séparer les groupes.
def afficher_groupes(groupes):
    for i, groupe in enumerate(groupes):
        print(f"Groupe {i+1}:")
        for apprenant in groupe:
            print(apprenant)
        print()

#La fonction `afficher_adresse_email()` demande à l'utilisateur de saisir le nom d'un apprenti puis vérifie si l'adresse e-mail de cet apprenti est déjà stockée
#  dans le dictionnaire `cache_apprenants`. Si c'est le cas, la fonction récupère l'adresse e-mail du dictionnaire et l'imprime sur la console. Si ce n'est pas le cas, 
# la fonction interroge la table `apprenants` de la base de données pour récupérer l'adresse e-mail de l'apprenti et l'imprime dans la console. Si l'apprenti n'est
#  pas trouvé dans la base de données, la fonction imprime un message indiquant qu'aucun apprenti portant ce nom n'a été trouvé. La fonction stocke également 
# l'adresse e-mail dans le dictionnaire `cache_apprenants` pour une utilisation future.
def afficher_adresse_email(apprenants):
    nom = input("Entrez le nom de l'apprenant : ")


#Ce bloc de code définit la fonction `afficher_adresse_email()` qui prend l'entrée de l'utilisateur pour le nom d'un apprenant et vérifie si l'adresse e-mail de 
# cet apprenant est déjà stockée dans le dictionnaire `cache_apprenants`. Si c'est le cas, la fonction récupère l'adresse e-mail du dictionnaire et l'imprime sur la 
# console. Si ce n'est pas le cas, la fonction interroge la table `apprenants` dans la base de données pour récupérer l'adresse e-mail de l'apprenant et l'imprime
#  dans la console. Si l'apprenant n'est pas trouvé dans la base de données, la fonction imprime un message indiquant qu'aucun apprenant portant ce nom n'a été trouvé. 
# La fonction stocke également l'adresse e-mail dans le dictionnaire `cache_apprenants` pour une utilisation future.
    if nom in cache_apprenants:
        adresse_email = cache_apprenants[nom]
        print(f"L'adresse e-mail de {nom} est {adresse_email}")
    else:
        with connexion.cursor() as curseur:
            curseur.execute("SELECT mail FROM apprenants WHERE nom = %s", (nom,))
            resultat = curseur.fetchone()
            if resultat:
                adresse_email = resultat[0]
                cache_apprenants[nom] = adresse_email  # Stocker le résultat en cache
                print(f"L'adresse e-mail de {nom} est {adresse_email}")
            else:
                print(f"Aucun apprenant avec le nom {nom} n'a été trouvé.")

#La fonction `afficher_projets()` récupère la liste des projets de la table `projets` de la base de données et les imprime dans la console. 
# Il crée d'abord un objet curseur en utilisant la connexion à la base de données, puis exécute une requête SELECT pour récupérer la `libelle` (nom) de chaque projet.
#  Il récupère ensuite tous les résultats à l'aide de la méthode `fetchall()` et les stocke dans une liste appelée `projets`. Enfin, il parcourt la liste et imprime chaque nom de projet sur la console.
def afficher_projets():
    with connexion.cursor() as curseur:
        curseur.execute("SELECT libelle FROM projets")
        projets = [ligne[0] for ligne in curseur.fetchall()]
        print("Liste des projets :")
        for projet in projets:
            print(projet)

#La fonction `afficher_groupes_projet()` propose à l'utilisateur de saisir le nom d'un projet, puis interroge la table `groupes_projets` de la base de données pour 
# récupérer la liste des groupes associés à ce projet. Si des groupes sont associés au projet, il imprime un message indiquant le nom du projet, puis répertorie 
# chaque groupe associé au projet. Si aucun groupe n'est associé au projet, il imprime un message indiquant qu'aucun groupe n'a été trouvé.
def afficher_groupes_projet():
    projet = input("Entrez le nom du projet : ")
    with connexion.cursor() as curseur:
        curseur.execute("SELECT groupe FROM groupes_projets WHERE projet = %s", (projet,))
        groupes = [ligne[0] for ligne in curseur.fetchall()]
        if groupes:
            print(f"Groupes associés au projet '{projet}' :")
            for groupe in groupes:
                print(groupe)
        else:
            print(f"Aucun groupe associé au projet '{projet}' n'a été trouvé.")

#La fonction `stocker_groupes_constitues` prend une liste de groupes en entrée et les stocke dans la table `groupes_constitues` de la base de données avec la date actuelle. Pour ce faire, il itère sur chaque groupe de la liste, convertit la liste des noms en une chaîne séparée par des virgules, puis exécute une instruction SQL "INSERT" pour ajouter le groupe et la date à la table. Enfin, il valide les modifications apportées à la base de données.
def stocker_groupes_constitues(groupes):
    date_creation = datetime.date.today()  # Obtenez la date actuelle
    with connexion.cursor() as curseur:
        for groupe in groupes:
            groupe_str = ', '.join(groupe)  # Convertir la liste de noms de groupe en une chaîne de caractères séparée par des virgules
            curseur.execute("INSERT INTO groupes_constitues (groupe, date_creation) VALUES (%s, %s)", (groupe_str, date_creation))
        connexion.commit()

#Il s'agit de la boucle principale du programme qui affiche un menu d'options à l'utilisateur et l'invite à entrer un choix. Selon le choix saisi, le programme exécutera 
# une fonction spécifique telle que la génération de groupes, la recherche de l'email d'un apprenant ou l'affichage d'une liste de projets. La boucle continuera à s'exécuter jusqu'à ce que l'utilisateur choisisse de quitter le programme en entrant "5".
while True:
    print("Que souhaitez-vous faire ?")
    print("1. Générer des groupes")
    print("2. Rechercher le mail d'un apprenant")
    print("3. Consulter la liste des projets")
    print("4. Afficher la liste des groupes pour un projet")
    print("5. Quitter")

    choix = input("Entrez le numéro de votre choix : ")

    if choix == "1":
        nombre_groupes = demander_nombre_groupes()
        groupes = former_groupes(bdd_apprenants, nombre_groupes)
        afficher_groupes(groupes)
        stocker_groupes_constitues(groupes)
    elif choix == "2":
        afficher_adresse_email(bdd_apprenants)
    elif choix == "3":
        afficher_projets()
    elif choix == "4":
        afficher_groupes_projet()
    elif choix == "5":
        break  # Quitter la boucle et terminer le programme
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")