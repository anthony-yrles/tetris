import pygame as Py
import random
import time
from random import randrange
from globales import *

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

#Globals pour le render du Hall Of Fame
image_bcg_hall_of_fame = Py.image.load('./assets/images/bcg_hall_of_fame.jpg')
rect_mode_normal = Py.Rect(200, 220, 400, 60)
rect_mode_survival = Py.Rect(200, 320, 400, 60)
rect_hall_of_fame = Py.Rect(150, 480, 500, 60)
rect_premier = Py.Rect(300, 220, 200, 60)
rect_deuxieme = Py.Rect(20, 320, 250, 60)
rect_troisieme = Py.Rect(530, 380, 250, 60)

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
# tetraminos_normal = [tetramino_1, tetramino_2, tetramino_3, tetramino_4, tetramino_5, tetramino_6]
tetraminos_normal = [tetramino_4, tetramino_6]
tetraminos_survival = [tetramino_1, tetramino_2, tetramino_3, tetramino_4, survival_tetra_5, survival_tetra_6]
# tetraminos_survival = [survival_tetra_6]

def random_tetramino(tetraminos):
    tetramino = random.choice(tetraminos)
    return tetramino

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

def set_grid_initial(new_grid, new_tetraminos_x):
    global grid, tetraminos_x
    grid = new_grid
    tetraminos_x = new_tetraminos_x

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

def set_survival_grid_initial(new_survival_grid, new_survival_tetraminos_x):
    global survival_grid, survival_tetraminos_x
    survival_grid = new_survival_grid
    survival_tetraminos_x = new_survival_tetraminos_x

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
    global tetraminos_x, survival_tetraminos_x, tetraminos_y, completed_lignes, total_score, level, FPS
    menu = get_menu()
    if menu == 1:
        set_grid_initial([[0] * 20 for _ in range(31)], 10)
        tetraminos_x = 10
    elif menu == 2:
        set_survival_grid_initial([[0] * 14 for _ in range(21)], 7)
        survival_tetraminos_x = 7
    tetraminos_y = 1
    completed_lignes = 0
    total_score = 0
    level = 1
    FPS = 1


time_begin = time.time()
time_end_game = 0
time_running = time.time()

def set_time_end_game(time_running):
    global time_end_game
    time_end_game = time_running
def get_time_end_game():
    global time_end_game
    return time_end_game
