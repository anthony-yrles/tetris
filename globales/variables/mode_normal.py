from globales import *

# Initialisation de la grille du mode normal
grid = [[0] * 20 for _ in range(31)]

# Initialisation de l'emplacement dans la grille ou les tetraminos vont apparaitre
tetraminos_x = 10
tetraminos_y = 0

# Setteur de la grille a chaque fois qu'elle se rempli
def set_grid(tetramino, draw_x, draw_y, taille_cote):
    global grid
    for coord in tetramino:
        x = (draw_x + coord[1] * taille_cote - grid_start_x) // tile_size
        y = (draw_y + coord[0] * taille_cote) // tile_size
        set_grid_value(y, x, 1)

def set_grid_value(y, x, value):
    global grid
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        grid[y][x] = value

# Setteur de la grille initial afin de redemarrer une partie
def set_grid_initial(new_grid, new_tetraminos_x):
    global grid, tetraminos_x
    grid = new_grid
    tetraminos_x = new_tetraminos_x

# Setteur tetraminos_x et tetraminos_y pour gérer les déplacements et les collisions
def set_tetraminos_x(value):
    global tetraminos_x
    if value == 1:
        tetraminos_x += 1
    elif value == -1:
        tetraminos_x -= 1
    else:
        tetraminos_x = value

def set_tetraminos_y(value):
    global tetraminos_y
    if value == 1:
        tetraminos_y += 1
    else:
        tetraminos_y = value

# Getteur de grid, tetramino_x et tetramino_y
def get_grid():
    global grid
    return grid
def get_tetraminos_x():
    global tetraminos_x
    return tetraminos_x
def get_tetraminos_y():
    global tetraminos_y
    return tetraminos_y