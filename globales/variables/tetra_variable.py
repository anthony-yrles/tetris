from globales import *
import random

# Fonction permettant de sélectionner un tetramino au hasard dans une liste
def random_tetramino(tetraminos):
    tetramino = random.choice(tetraminos)
    return tetramino

# Création de variables qui utilise la fonction ci dessus pour une liste précise
tetramino_normal = random_tetramino(tetraminos_normal)
tetramino_survival = random_tetramino(tetraminos_survival)

# Setteur et getteur de la liste de jeu normal + setteur des tetramino du mode normal après rotation
def set_tetramino_normal(tetraminos):
    global tetramino_normal
    tetramino_normal = tetraminos

def get_tetramino_normal():
    global tetramino_normal
    return tetramino_normal

def set_rotate_tetramino_normal():
    global tetramino_normal
    if tetramino_normal == tetramino_1:
        return tetramino_1_bis
    elif tetramino_normal == tetramino_1_bis:
        return tetramino_1_ter
    elif tetramino_normal == tetramino_1_ter:
        return tetramino_1_quatro
    elif tetramino_normal == tetramino_1_quatro:
        return tetramino_1
    elif tetramino_normal == tetramino_2:
        return tetramino_2_bis
    elif tetramino_normal == tetramino_2_bis:
        return tetramino_2
    elif tetramino_normal == tetramino_3:
        return tetramino_3_bis
    elif tetramino_normal == tetramino_3_bis:
        return tetramino_3
    elif tetramino_normal == tetramino_4:
        return tetramino_4
    elif tetramino_normal == tetramino_5:
        return tetramino_5_bis
    elif tetramino_normal == tetramino_5_bis:
        return tetramino_5_ter
    elif tetramino_normal == tetramino_5_ter:
        return tetramino_5_quatro
    elif tetramino_normal == tetramino_5_quatro:
        return tetramino_5
    elif tetramino_normal == tetramino_6:
        return tetramino_6_bis
    elif tetramino_normal == tetramino_6_bis:
        return tetramino_6
    
# Setteur et getteur de la liste de jeu survival + setteur des tetramino du mode survival après rotation
    
def set_tetramino_survival(tetraminos):
    global tetramino_survival
    tetramino_survival = tetraminos

def get_tetramino_survival():
    global tetramino_survival
    return tetramino_survival

def set_rotate_termino_survival():
    global tetramino_survival
    if tetramino_survival == tetramino_1:
        return tetramino_1_bis
    elif tetramino_survival == tetramino_1_bis:
        return tetramino_1_ter
    elif tetramino_survival == tetramino_1_ter:
        return tetramino_1_quatro
    elif tetramino_survival == tetramino_1_quatro:
        return tetramino_1
    elif tetramino_survival == tetramino_2:
        return tetramino_2_bis
    elif tetramino_survival == tetramino_2_bis:
        return tetramino_2
    elif tetramino_survival == tetramino_3:
        return tetramino_3_bis
    elif tetramino_survival == tetramino_3_bis:
        return tetramino_3
    elif tetramino_survival == tetramino_4:
        return tetramino_4
    elif tetramino_survival == survival_tetra_5:
        return survival_tetra_5_bis
    elif tetramino_survival == survival_tetra_5_bis:
        return survival_tetra_5_ter
    elif tetramino_survival == survival_tetra_5_ter:
        return survival_tetra_5_quatro
    elif tetramino_survival == survival_tetra_5_quatro:
        return survival_tetra_5
    elif tetramino_survival == survival_tetra_6:
        return survival_tetra_6_bis
    elif tetramino_survival == survival_tetra_6_bis:
        return survival_tetra_6
