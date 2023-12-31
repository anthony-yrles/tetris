import pygame as Py
import random
from random import choice, randrange

screen = Py.display.set_mode((800, 600))
get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))

# Création d'un setteur et d'un getteur de menu
menu = 0
def set_menu(menu_on_clic):
    global menu
    menu = menu_on_clic 
def get_menu():
    global menu
    return menu

# Globals pour le render du menu

image_bcg_menu = Py.image.load('./assets/images/bcg.jpg')
image_barre_menu = Py.image.load('./assets/images/barre_2.jpg')
rect_tetriste = Py.Rect(250, 20, 300, 60)
barre_rect_normal = Py.Rect(50, 250, 300, 77)
barre_rect_time_attack = Py.Rect(50, 450, 300, 77)
barre_rect_survival = Py.Rect(450, 250, 300, 77)
barre_rect_hall_of_fame = Py.Rect(450, 450, 300, 77)

# Globals pour le render du normal

rect_tetriste_normal = Py.Rect(500, 20, 250, 60)
image_bcg_normal = Py.image.load('./assets/images/bcg_normal.jpg')
rect_level = Py.Rect(500, 330, 100, 50)
rect_level_count = Py.Rect(700, 330, 100, 50)
rect_ligne = Py.Rect(500, 430, 100, 50)
rect_ligne_count = Py.Rect(700, 430, 100, 50)
rect_score = Py.Rect(500, 530, 100, 50)
rect_score_count = Py.Rect(700, 530, 100, 50)
rect_display_game = Py.Rect(50, 0, 400, 600)
number_of_tile_x = 400 // 20
number_of_tile_y = 600 // 20
tile_size = 20
grid_start_x = 50
grid_start_y = 0

# Globals pour le render du end_game
rect_game_end = Py.Rect(0, 100, 800, 80)
rect_register = Py.Rect(0, 200, 800, 80)
rect_register_name = Py.Rect(270, 300, 300, 80)
rect_play_again = Py.Rect(0, 400, 800, 80)
rect_play_again_click = Py.Rect(270, 500, 300, 80)

# Globals pour le render du survival_mode
image_bcg_survival = Py.image.load('./assets/images/bcg_survival.jpg')
rect_tetriste_survival = Py.Rect(50, 20, 250, 60)
survival_tile_size = 30
number_of_survival_tile_x = 420 // survival_tile_size
number_of_survival_tile_y = 600 // survival_tile_size
survival_grid_start_x = 350
survival_grid_start_y = 0

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
tetraminos_survival = [tetramino_1, tetramino_2, tetramino_3, tetramino_4, survival_tetra_5, survival_tetra_6]
# tetraminos_survival = [survival_tetra_6]

def random_tetramino(tetraminos):
    tetramino = random.choice(tetraminos)
    return tetramino

# next_tetramino = None

# def set_next_tetramino(tetraminos):
#     global next_tetramino
#     tetramino = random.choice(tetraminos)
#     next_tetramino = tetramino

# def get_next_tetramino():
#     global next_tetramino
#     return next_tetramino

tetramino_normal = random_tetramino(tetraminos_normal)
tetramino_survival = random_tetramino(tetraminos_survival)

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

def set_tetramino_normal(tetraminos):
    global tetramino_normal
    tetramino_normal = tetraminos
def set_tetramino_survival(tetraminos):
    global tetramino_survival
    tetramino_survival = tetraminos

def get_tetramino_normal():
    global tetramino_normal
    return tetramino_normal
def get_tetramino_survival():
    global tetramino_survival
    return tetramino_survival

# Gestion des coordonées des tetramino et du remplissage de la grille en mode normal
grid = [[0] * 20 for _ in range(31)]
tetraminos_x = 10
tetraminos_y = 0

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

def get_tetraminos_x():
    global tetraminos_x
    return tetraminos_x
def get_tetraminos_y():
    global tetraminos_y
    return tetraminos_y
def get_grid():
    global grid
    return grid

# Gestion des coordonées des tetramino et du remplissage de la grille en mode survival
survival_grid = [[0] * 14 for _ in range(21)]
survival_tetraminos_x = 7

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

def set_survival_tetraminos_x(value):
    global survival_tetraminos_x
    if value == 1:
        survival_tetraminos_x += 1
    elif value == -1:
        survival_tetraminos_x -= 1
    else:
        survival_tetraminos_x = value

def get_survival_tetraminos_x():
    global survival_tetraminos_x
    return survival_tetraminos_x

def get_survival_grid():
    global survival_grid
    return survival_grid

completed_lignes = 0
total_score = 0
level = 1
FPS = 1
game_end = 0

def set_completed_lignes(lignes_finished):
    global completed_lignes
    completed_lignes += lignes_finished
    set_level(completed_lignes)

def get_completed_lignes():
    global completed_lignes
    return completed_lignes

def set_total_score(lignes_finished):
    global total_score
    if lignes_finished == 1:
        total_score += 10
    elif lignes_finished == 2:
        total_score += 30
    elif lignes_finished == 3:
        total_score += 90
    elif lignes_finished == 4:
        total_score += 270
    elif lignes_finished == 5:
        total_score += 810
    elif lignes_finished == 6:
        total_score += 2500

def get_total_score():
    global total_score
    return total_score

def set_level(completed_lignes):
    global level
    level = completed_lignes // 10 +1
    set_FPS(level)

def get_level():
    global level
    return level

def set_FPS(level):
    global FPS
    FPS = FPS + level / 10

def get_FPS():
    global FPS
    return FPS

def set_game_end():
    global game_end
    if game_end == 0:
        game_end = 1
    else:
        game_end = 0

def get_game_end():
    global game_end
    return game_end

def set_initial_value():
    global grid, survival_grid, tetraminos_x, survival_tetraminos_x, tetraminos_y, completed_lignes, total_score, level, FPS
    menu = get_menu
    if menu == 1:
        grid = [[0] * 20 for _ in range(31)]
        tetraminos_x = 10
    elif menu == 2:
        survival_grid = [[0] * 20 for _ in range(31)]
        survival_tetraminos_x = 10
    tetraminos_y = 1
    completed_lignes = 0
    total_score = 0
    level = 1
    FPS = 1