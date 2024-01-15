# Shazam

This project will try to reproduce Shazam algorithm.
The idea comes from this video : https://www.youtube.com/watch?v=En7XJu7cNDM

## The process

### 1- Create a spectrogram of an audio file
A spectrogram is a visual representation of the spectrum of frequencies of a signal as it varies with time.
The spectrogram is usually represented as a heat map, i.e., as an image with the intensity shown by varying the color or brightness.
Fourier transformation is used to create the spectrogram.

## TO DO

### 2- Simplifier les spectrogrammes
Retenir les fréquences les plus importantes (celles qui ont la plus forte intensité)
Placer un point sur chacune de ces fréquences
Créer la constellation (nuage de points contenant l'identité de la chanson)

### 3 - Hacher la constellation
Selectionner plusieurs points de la constellation qui seront des points d'ancrage
Pour chacun des points d'ancrage, définir une zone cible contenant d'autre points

### 4 - Créer la table de hachage
| Hash | Timing d'apparition | Nom musique |
|------|---------------------|-------------|

### 5 - Trouver la musique
Avec histogramme du nb de timing d'apparition
