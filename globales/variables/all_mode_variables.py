from .mode_normal import set_grid_initial
from .mode_survival import set_survival_grid_initial

# Initialisation des variables
menu = 0
completed_lignes = 0
total_score = 0
level = 1
FPS = 1
game_end = 0
time_end_game = 0

#Setteur pour les variables initié
def set_menu(menu_on_clic):
    global menu
    menu = menu_on_clic 
def set_completed_lignes(lignes_finished):
    global completed_lignes
    completed_lignes += lignes_finished
    set_level(completed_lignes)
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
def set_level(completed_lignes):
    global level
    level = completed_lignes // 10 +1
    set_FPS(level)
def set_FPS(level):
    global FPS
    FPS = FPS + level / 10
def set_game_end():
    global game_end
    if game_end == 0:
        game_end = 1
    else:
        game_end = 0
def set_time_end_game(time_running):
    global time_end_game
    time_end_game = time_running

#Setteur pour remettre à zéro toutes les variables en cas de redemarrage d'une partie
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

#Getteur des variables cités
def get_menu():
    global menu
    return menu
def get_completed_lignes():
    global completed_lignes
    return completed_lignes
def get_total_score():
    global total_score
    return total_score
def get_level():
    global level
    return level
def get_FPS():
    global FPS
    return FPS
def get_game_end():
    global game_end
    return game_end
def get_time_end_game():
    global time_end_game
    return time_end_game