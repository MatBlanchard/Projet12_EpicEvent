# OpenClassrooms: Projet 12 - EpicEvent
Projet réalisé dans le cadre de ma formation OpenClassrooms Développeur d'Applications Python.  
Il s'agit d'une API réalisée avec Django pour une société fictive, EpicEvent.  
L'application permet de gérer des évenements pour les différents clients de l'entreprise.
## Documentation
Tout les endpoints, leurs détails ainsi que des exemples d'utilisation sont décrits dans la [documentation](https://documenter.getpostman.com/view/25251122/2s93CLtEDY).
## Installation et lancement
Commencez tout d'abord par installer Python.

https://www.python.org/downloads/

Lancez ensuite la console, placez-vous dans le dossier de votre choix puis clonez ce repository :
```
git clone https://github.com/MatBlanchard/Projet12_EpicEvent.git
```
Créez un nouvel environnement virtuel :
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate
```
Installez ensuite les packages :
```
pip install -r requirements.txt
```
Créez un super utilisateur :
```
python EpicEvent\manage.py createsuperuser
```
Ce super utilisateur sera automatiquement intégré à l'équipe de gestion et pourra donc créer d'autres utilisateurs.

Il ne vous reste plus qu'à lancez le serveur : 
```
python EpicEvent\manage.py runserver
```
Vous pouvez ensuite utiliser l'applicaton via les différents endpoints décrits dans la documentation.