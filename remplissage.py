from globales import *

def test_ligne():
    global grid, survival_grid
    lignes_finished = 0
    menu = get_menu()
    if menu == 1:
        for y in range(30):
            ligne_completed = all(cell == 1 for cell in grid[y])
            if ligne_completed:
                lignes_finished += 1
                for i in range(y, 0, -1):
                    grid[i] = grid[i - 1].copy()
                nouvelle_ligne = [0] * len(grid[0])
                grid[0] = nouvelle_ligne.copy()
    elif menu == 2:
        for y in range(20):
            ligne_completed = all(cell == 1 for cell in survival_grid[y])
            if ligne_completed:
                lignes_finished += 1
                for i in range(y, 0, -1):
                    survival_grid[i] = survival_grid[i - 1].copy()
                nouvelle_ligne = [0] * len(survival_grid[0])
                survival_grid[0] = nouvelle_ligne.copy()

    set_completed_lignes(lignes_finished)
    set_total_score(lignes_finished)

    lignes_finished = 0





            


