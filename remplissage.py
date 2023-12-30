from globals import *

# def test_ligne():
#     grid = get_grid()
#     lignes_a_supprimer = get_lines_to_remove()
#     for y in range(30):
#         ligne_complete = all(cell == 1 for cell in grid[y])
#         if ligne_complete:
#             print(f"Ligne {y} est complète.")
#             lignes_a_supprimer.append(y)

#     for y in reversed(lignes_a_supprimer):
#         for x in range(len(grid[y])):
#             set_grid_value(y, x, 0)

#         nouvelle_ligne = [0] * len(grid[0])
#         for x in range(len(grid[0])):
#             set_grid_value(0, x, nouvelle_ligne[x])

import random

def test_ligne():
    global grid

    for y in range(30):
        ligne_complete = all(cell == 1 for cell in grid[y])
        if ligne_complete:
            print(f"Ligne {y} est complète.")

            # Décaler les lignes vers le bas
            for i in range(y, 0, -1):
                grid[i] = grid[i - 1].copy()

            # Ajouter une nouvelle ligne en haut de la grille (tous les éléments à 0)
            nouvelle_ligne = [0] * len(grid[0])
            grid[0] = nouvelle_ligne.copy()

    # Réinitialiser la liste des lignes à supprimer après les avoir traitées
    set_lines_to_remove([])



            


