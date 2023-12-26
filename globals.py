import pygame as Py
import random

screen = Py.display.set_mode((800, 600))

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

image_bcg_normal = Py.image.load('./assets/images/bcg_normal.jpg')
rect_display_game = Py.Rect(200, 0, 400, 600)
number_of_tile_x = 400 // 20
number_of_tile_y = 600 // 20
tile_size = 20
grid_start_x = 200
grid_start_y = 0
rect_interior_game = Py.Rect(200, 0, 19, 19)

# Globals pour les différents forme de tuiles
tetramino_1 = [[0, -1], [1, -1],[-1, 0], [0, 0],[-1, 1]]
tetramino_1_bis = [[-1, 0],[0, 0],[0, 1], [-1, -1],[1, 1]]
tetramino_1_ter = [[-1, 1],[0, 1], [0, 0], [1, 0], [1, -1]]
tetramino_1_quatro = [[-1, -1], [-1, 0], [0, 0], [0, 1], [1, 1]]
tetramino_2 = [[-1, 0],[0, -2], [0, -1], [0, 0], [0, 1], [0, 2],[1, 0]]
tetramino_2_bis = [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0], [0, -1], [0, 1]]
tetramino_3 = [[-1, -1], [-1, 1],[0, -2], [0, -1], [0, 0], [0, 1], [0, 2],[1, -1], [1, 1]]
tetramino_3_bis = [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0], [1, -1], [1, 1],[-1, -1], [-1, 1]]
tetramino_4 = [[0, 0]]
tetramino_5 = [[-4, 0],[-3, 0],[-2, 0],[-1, 0],[0, 0], [0, 1], [0, 2],[0, 3], [0, 4]]
tetramino_5_bis = [[4, 0],[3, 0],[2, 0],[1, 0],[0, 0], [0, 1], [0, 2],[0, 3], [0, 4]]
tetramino_5_ter = [[4, 0],[3, 0],[2, 0],[1, 0],[0, 0], [0, -1], [0, -2],[0, -3], [0, -4]]
tetramino_5_quatro = [[-4, 0],[-3, 0],[-2, 0],[-1, 0],[0, 0], [0, -1], [0, -2],[0, -3], [0, -4]]
tetramino_6 = [[0, 0],[1, 0],[2, 0],[3, 0],[4, 0],[5, 0]]
tetramino_6_bis = [[0, 0],[0, 1],[0, 2],[0, 3],[0, 4], [0, 5]]

# Création d'une liste contenant les différentes formes
tetraminos = [tetramino_1, tetramino_2, tetramino_3, tetramino_4, tetramino_5, tetramino_6]

def random_tetramino(tetraminos):
    tetramino = random.choice(tetraminos)
    return tetramino

tetramino = random_tetramino(tetraminos)

def set_rotate_tetramino():
    global tetramino
    if tetramino == tetramino_1:
        tetramino = tetramino_1_bis
    elif tetramino == tetramino_1_bis:
        tetramino = tetramino_1_ter
    elif tetramino == tetramino_1_ter:
        tetramino = tetramino_1_quatro
    elif tetramino == tetramino_1_quatro:
        tetramino = tetramino_1
    elif tetramino == tetramino_2:
        tetramino = tetramino_2_bis
    elif tetramino == tetramino_2_bis:
        tetramino = tetramino_2
    elif tetramino == tetramino_3:
        tetramino = tetramino_3_bis
    elif tetramino == tetramino_3_bis:
        tetramino = tetramino_3
    elif tetramino == tetramino_5:
        tetramino = tetramino_5_bis
    elif tetramino == tetramino_5_bis:
        tetramino = tetramino_5_ter
    elif tetramino == tetramino_5_ter:
        tetramino = tetramino_5_quatro
    elif tetramino == tetramino_5_quatro:
        tetramino = tetramino_5
    elif tetramino == tetramino_6:
        tetramino = tetramino_6_bis
    elif tetramino == tetramino_6_bis:
        tetramino = tetramino_6

def set_tetramino(tetraminos):
    global tetramino
    tetramino = random_tetramino(tetraminos)

def get_tetramino():
    global tetramino
    return tetramino

# Gestion des coordonées des tetramino et du remplissage de la grille 
grid = [[0] * 20 for _ in range(30)]
tetraminos_x = 10
tetraminos_y = 0

def set_grid(tetramino, draw_x, draw_y, taille_cote):
    global grid
    for coord in tetramino:
        x = (draw_x + coord[1] * taille_cote - grid_start_x) // tile_size
        y = (draw_y + coord[0] * taille_cote) // tile_size
        grid[y][x] = 1

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

