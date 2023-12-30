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
    lignes_completed = 0

    for y in range(30):
        ligne_completed = all(cell == 1 for cell in grid[y])
        if ligne_completed:
            lignes_completed += 1
            for i in range(y, 0, -1):
                grid[i] = grid[i - 1].copy()
            nouvelle_ligne = [0] * len(grid[0])
            grid[0] = nouvelle_ligne.copy()

    set_completed_lignes(lignes_completed)
    set_total_score(lignes_completed)

    lignes_completed = 0





            


