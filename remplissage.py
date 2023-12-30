from globals import *

def test_ligne():
    global grid
    lignes_finished = 0

    for y in range(30):
        ligne_completed = all(cell == 1 for cell in grid[y])
        if ligne_completed:
            lignes_finished += 1
            for i in range(y, 0, -1):
                grid[i] = grid[i - 1].copy()
            nouvelle_ligne = [0] * len(grid[0])
            grid[0] = nouvelle_ligne.copy()

    set_completed_lignes(lignes_finished)
    set_total_score(lignes_finished)

    lignes_finished = 0





            


