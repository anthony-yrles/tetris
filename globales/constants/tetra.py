import pygame as Py

# Globals pour les différents forme de tuiles en mode normal
tetramino_1 = [[0, -1], [1, -1],[-1, 0], [0, 0],[-1, 1]]
tetramino_1_bis = [[-1, 0],[0, 0],[0, 1], [-1, -1],[1, 1]]
tetramino_1_ter = [[-1, 1],[0, 1], [0, 0], [1, 0], [1, -1]]
tetramino_1_quatro = [[-1, -1], [-1, 0], [0, 0], [0, 1], [1, 1]]
tetramino_2 = [[-1, 0],[0, -2], [0, -1], [0, 0], [0, 1], [0, 2],[1, 0]]
tetramino_2_bis = [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0], [0, -1], [0, 1]]
tetramino_3 = [[-1, -1], [-1, 1],[0, -2], [0, -1], [0, 0], [0, 1], [0, 2],[1, -1], [1, 1]]
tetramino_3_bis = [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0], [1, -1], [1, 1],[-1, -1], [-1, 1]]
tetramino_4 = [[0,0], [0,1], [1,1], [1,0],[-1,0],[-1,-1],[0,-1],[-1,1],[1,-1]]
tetramino_5 = [[-4, 0],[-3, 0],[-2, 0],[-1, 0],[0, 0], [0, 1], [0, 2],[0, 3], [0, 4]]
tetramino_5_bis = [[4, 0],[3, 0],[2, 0],[1, 0],[0, 0], [0, 1], [0, 2],[0, 3], [0, 4]]
tetramino_5_ter = [[4, 0],[3, 0],[2, 0],[1, 0],[0, 0], [0, -1], [0, -2],[0, -3], [0, -4]]
tetramino_5_quatro = [[-4, 0],[-3, 0],[-2, 0],[-1, 0],[0, 0], [0, -1], [0, -2],[0, -3], [0, -4]]
tetramino_6 = [[-3, 0],[-2, 0],[-1, 0],[0, 0],[1, 0],[2, 0], [3, 0]]
tetramino_6_bis = [[0, -3], [0, -2],[0, -1],[0, 0],[0, 1],[0, 2], [0, 3]]

# Globals pour les différents forme de tuiles en mode survival
survival_tetra_5 = [[-3, 0], [-2, 0], [-1, 0], [0, 0], [0, 1], [0, 2]]
survival_tetra_5_bis = [[2, 0], [1, 0], [0, 0], [0, 1], [0, 2], [0, 3]]
survival_tetra_5_ter = [[3, 0], [2, 0], [1, 0], [0, 0], [0, -1], [0, -2]]
survival_tetra_5_quatro = [[-2, 0], [-1, 0], [0, 0], [0, -1], [0, -2], [0, -3]]
survival_tetra_6 = [[-2, 0],[-1, 0],[0, 0],[1, 0],[2, 0]]
survival_tetra_6_bis = [[0, -2],[0, -1],[0, 0],[0, 1],[0, 2]]

# Création d'une liste contenant les différentes formes
tetraminos_normal = [tetramino_1, tetramino_2, tetramino_3, tetramino_4, tetramino_5, tetramino_6]
# tetraminos_normal = [tetramino_4, tetramino_6]
tetraminos_survival = [tetramino_1, tetramino_2, tetramino_3, tetramino_4, survival_tetra_5, survival_tetra_6]
# tetraminos_survival = [survival_tetra_6]