from globales import *

# Initialisation de la grille du mode survival + initialisation du point d'apparition en x.
# La gestion des y ne change pas entre le mode normal et celui ci, il n'ai donc pas necessaire de recréer de setteur et de getteur
survival_grid = [[0] * 14 for _ in range(21)]
survival_tetraminos_x = 7

# Setteur de la grille a chaque fois qu'elle se rempli
def set_survival_grid(tetramino, draw_x, draw_y, taille_cote):
    global survival_grid
    for coord in tetramino:
        x = (draw_x + coord[1] * survival_tile_size - survival_grid_start_x) // survival_tile_size
        y = (draw_y + coord[0] * survival_tile_size) // survival_tile_size
        set_survival_grid_value(y, x, 1)

def set_survival_grid_value(y, x, value):
    global survival_grid
    if 0 <= y < len(survival_grid) and 0 <= x < len(survival_grid[0]):
        survival_grid[y][x] = value

# Setteur de la grille initial afin de redemarrer une partie
def set_survival_grid_initial(new_survival_grid, new_survival_tetraminos_x):
    global survival_grid, survival_tetraminos_x
    survival_grid = new_survival_grid
    survival_tetraminos_x = new_survival_tetraminos_x

# Setteur tetraminos_x pour gérer les déplacements et les collisions.
def set_survival_tetraminos_x(value):
    global survival_tetraminos_x
    if value == 1:
        survival_tetraminos_x += 1
    elif value == -1:
        survival_tetraminos_x -= 1
    else:
        survival_tetraminos_x = value

# Getteur de grid, tetramino_x
def get_survival_grid():
    global survival_grid
    return survival_grid
def get_survival_tetraminos_x():
    global survival_tetraminos_x
    return survival_tetraminos_x