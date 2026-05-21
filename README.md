FullScreenBlocker
Description
Application Python utilisant Tkinter pour afficher une fenetre en plein ecran impossible a fermer.
Elle affiche :

une image au centre

un compte a rebours (1 heure par defaut)

un texte en bas de l ecran

Le script bloque toutes les entrees clavier et souris et force la fenetre a rester au premier plan.

Fonctionnement
Fenetre en plein ecran, sans bordures

Tous les evenements clavier et souris sont bloques

Chargement automatique de image.png si present

Timer mis a jour chaque seconde

Texte fixe "WE SEE YOU" en bas

La fonction resource_path() permet la compatibilite avec PyInstaller.

Installation
Installer Python 3

Verifier que Tkinter est disponible

Placer script.py et image.png dans le meme dossier

Lancement
bash
python script.py
Structure
Code
/
├── script.py
└── image.png   (optionnel)
Compilation en executable (optionnel)
bash
pip install pyinstaller
pyinstaller --noconsole --onefile script.py
Notes
Le blocage complet des entrees est volontaire

Pour le developpement, commenter temporairement block_all_inputs()
