Ce projet consiste en un programme permettant de générer des groupes d'étudiants, de rechercher l'adresse e-mail d'un étudiant, de consulter la liste des projets et d'afficher les groupes associés à un projet.

Prérequis

Pour exécuter ce programme, assurez-vous d'avoir les modules suivants installés :

random pour mélanger la liste des étudiants,
mysql.connector pour se connecter et interroger une base de données MySQL,
math pour arrondir la taille du groupe,
datetime pour obtenir la date actuelle.
Configuration de la base de données
Assurez-vous de configurer correctement la connexion à la base de données MySQL dans le code. Vous devez spécifier l'hôte, le nom d'utilisateur, le mot de passe, le nom de la base de données et le numéro de port dans le bloc try du code.

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="example",
    database="binomotron",
    port="3307"
)

Utilisation du programme
Le programme présente un menu avec les options suivantes :

Générer des groupes : Cette option permet de générer des groupes d'étudiants. Vous serez invité à entrer le nombre de groupes souhaités. Les groupes seront formés en mélangeant aléatoirement la liste des étudiants récupérée depuis la base de données.
Rechercher le mail d'un apprenant : Cette option permet de rechercher l'adresse e-mail d'un étudiant en entrant son nom. Si l'adresse e-mail est déjà enregistrée dans le cache, elle sera directement affichée. Sinon, elle sera récupérée depuis la base de données et stockée dans le cache pour une utilisation ultérieure.
Consulter la liste des projets : Cette option affiche la liste des projets enregistrés dans la base de données.
Afficher la liste des groupes pour un projet : Cette option permet d'afficher la liste des groupes associés à un projet. Vous serez invité à entrer le nom du projet.
Quitter : Cette option permet de quitter le programme.
Assurez-vous de sélectionner l'option correspondante en entrant le numéro de votre choix.

Note : N'oubliez pas d'ajuster les informations de connexion à la base de données et de vous assurer que le serveur MySQL est en cours d'exécution avant d'exécuter le programme.
