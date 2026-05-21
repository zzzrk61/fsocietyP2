# FullScreenBlocker

## Description

Application Python utilisant Tkinter pour afficher une fenetre en plein ecran impossible a fermer.

Le programme affiche :

- une image au centre de l ecran
- un compte a rebours (1 heure par defaut)
- un texte fixe en bas de la fenetre

Le script garde la fenetre au premier plan et bloque les entrees clavier et souris.

---

## Fonctionnement

- Fenetre plein ecran sans bordures
- Blocage des touches clavier et des clics souris
- Chargement automatique de `image.png` si le fichier est present
- Mise a jour du timer chaque seconde
- Texte fixe `"WE SEE YOU"` affiche en bas
- Compatibilite PyInstaller avec `resource_path()`

---

## Installation

### Prerequis

- Python 3
- Tkinter installe

Verification rapide :

```bash
python -m tkinter
