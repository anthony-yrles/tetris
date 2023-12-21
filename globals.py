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
rect_interior_game = Py.Rect(200, 0, 19, 19)

# Globals pour les différents forme de tuiles
forme_1 = [
    [1],[1],[1],
    [1],
    [1],
    [1],
    [1],[1]
]