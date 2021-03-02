# StarWars : Un projet de Dataiku

Ce projet a été réalisé dans le cadre d'un entretien d'embauche pour Dataiku par Louis CUNI.

# Projet

A partir d'une base de donnée représentant un graphe et de fichiers JSON, le but du projet est d'implémenter une application capable de trouver un chemin d'un point A à un point B en rencontrant le moins de danger possible. L'application devra comporter un BackEnd, un FrontEnd et une CLI.

## Fichiers

Un des fichiers JSON représente les contraintes du graphe. Celles ci sont variables et fluctuent au cours du temps. Elles sont représentées de la façon suivante :

Fichier "empire.json" :
- countdown : int    *représente le nombre de période max pour effectuer le trajet*
- bountyhunter : [
	- {planet : string, day: int}, *un danger est présent sur la planète string au jour int*
	- ...
	- ]
	
Le point de départ et le point d'arrivé sont stockés dans un second fichier JSON :

Fichier "vaisseau.json" :
  - autonomy : int, *nombre de période durant lesquelles le vaisseau peut avancer sans s'arrétter*
  - departure : string, *point de départ*
  - arrival : string, *point d'arrivé*
  - routes_db : file.db *nom du fichier de base de donnée*

Enfin, le fichier de base de donnée représente le graphe dans lequel le vaisseau évolue.

## Algorithme

L'idée principale de l'algorithme utilisé est de construire un tableau à deux entrées. Il représente tous les meilleurs états possibles du vaisseau à une période **p** sur une planète **Pl** :

| planète\période | p : 1 | p : 2 | ... | p : n | p : countdown|
|--------------------|-------|------|----|------|--------------|
|point de départ| état initiale
|planète 1|
|planète 2|
|planète n|
|planète arrivée |

En démarrant à l'état initial, on va inscrire sur le tableau tous les potentiels état issus de l'état initial sur les périodes correspondantes.
Par exemple, si depuis l'état initiale, le vaisseau peut se rendre à la **planète 1 en 2 périodes de temps** et à la  *planète 2 en 3 périodes de temps*, on remplie le tableau comme suit : 

| planète\période | p : 1 | p : 2 | p : 3 | p : 4 | p : n | p : countdown|
|--------------------|-------|------|-------|------|------|-------|
|point de départ| état initiale|
|planète 1| | | **état 1**|
|planète 2| | | | *état 2*|
|planète n|
|planète arrivée |

En répétant cette opération sur toutes les planètes et sur toutes les périodes on va remplir le tableau sans oublier un seul état. Une fois le remplissage terminé il suffit d'inspecter la ligne de la planète d'arrivée et de sélectionner l'état ayant rencontré le moins de danger.
Il est possible que sur une case, il existe plusieurs états. Pour être sûr de rien n'oublier il faut tous les explorer. Cependant certains états peuvent être supprimés dés lors qu'ils sont moins bon qu'un des états sur la même planète au même moment : par exemple, s'il existe deux états E1, E2 à la période p sur la planète Pl :

- E1 a rencontré 2 dangers
- E2 a rencontré 5 dangers

Il est claire que E1 est mieux que E2 et que E2 ne pourra pas engendrer des états meilleurs que ceux de E1. Par conséquent on peut supprimer E2.
Selon la façon dont les états sont représentés, il sera nécessaire d'intégrer des notions de modélisation multi-objectifs pour les comparer. 
L'avantage de ce tableau est qu'il garantie d'avoir tous les états optimaux à un période p et ainsi de ne pas à avoir à recalculer des calculs déjà effectués.

**Complexité** : O(nombre de planète * nombre de période max * degré moyen des planète)

### Optimisations sur les planètes
On peut remarquer qu'à partir d'une certaine période, plusieurs planètes deviendront inutiles car tous vaisseaux sur celles ci n'auront plus le temps d'atteindre le point d'arrivé. Dés lors, il devient inutile de continuer de fouiller leurs états dans le tableau. 
On peut obtenir cette information en calculant l'arbre des plus courts chemins depuis la planète d'arrivée. Chaque planète a alors une valeurs qui représente la période à partir de laquelle il n'est plus nécessaire de la fouiller.

## Implémentation

Le Backend a été réalisé en Python avec Flask, le Frontend en HTML, CSS et JavaScript et l'accés à la base de donnée en SQLite.

## How to Use

### Installation
**pip install -r requirements.txt --user**

### Démarrer le serveur
Sur windows :
**py run.py**

### How to uses Front
La fenêtre de droite est la console où l'équipage réagit. La fenêtre de droite est le fichier d'input et la fenêtre du bas est le chemin à emprunter.  
Pour rentrer un nouveaux fichier de danger, appuyer sur le bouton **"intercept file"**.
Pour analyser le fichier et obtenir la probabilité de réussite, appuyer sur le bouton **"analyse file"**

### Installer la ligne de commande
Depuis le dossier dataiku/service :
**pip install .**

### Appeler la ligne de commande
**give-me-the-odds  vaisseau.json  danger.json**

## Commentaires d'améliorations
- Le front pourrait être amélioré, notamment graphiquement.
- Il faudrait vérifier le fichier transmis au back au lieu de l'éxecuter directement.
- Il faudrait vérifier le bon format les fichiers JSON utilisés par la CLI.
