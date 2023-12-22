import pygame as Py

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
tetramino_2 = [[-1, 0],[0, -2], [0, -1], [0, 0], [0, 1], [0, 2],[1, 0],]
tetramino_3 = [[-1, -1], [-1, 1],[0, -2], [0, -1], [0, 0], [0, 1], [0, 2],[1, -1], [1, 1],]
tetramino_4 = [[0, 0]]
tetramino_5 = [[-4, -2],[-3, -2],[-2, -2],[-1, -2],[0, -2], [0, -1], [0, 0], [0, 1], [0, 2],]
tetramino_6 = [[0, 0],[1, 0],[2, 0],[3, 0],[4, 0],[5, 0],]

# Création d'une liste contenant les différentes formes
tetraminos = [tetramino_1, tetramino_2, tetramino_3, tetramino_4, tetramino_5, tetramino_6]

grid = [[0] * 20 for _ in range(30)]
tetraminos_x = 10
tetraminos_y = 0

def set_tetraminos_x_LEFT():
    global tetraminos_x
    tetraminos_x -= 1

def set_tetraminos_x_RIGHT():
    global tetraminos_x
    tetraminos_x += 1

def set_tetraminos_y():
    global tetraminos_y
    tetraminos_y += 1

def get_tetraminos_x():
    global tetraminos_x
    return tetraminos_x
def get_tetraminos_y():
    global tetraminos_y
    return tetraminos_y
def get_grid():
    global grid
    return grid

