import pygame as Py
from globales import *
from collision import *

def normal(event, barre_rect_normal):
    if event.type == Py.MOUSEBUTTONDOWN:
        pos = Py.mouse.get_pos()
        if barre_rect_normal.collidepoint(pos):
            menu_on_clic = 1
            set_menu(menu_on_clic)
            
def survival(event, barre_rect_survival):
    if event.type == Py.MOUSEBUTTONDOWN:
        pos = Py.mouse.get_pos()
        if barre_rect_survival.collidepoint(pos):
            menu_on_clic = 2
            set_menu(menu_on_clic)

def return_button(event, rect_return):
    game_end = get_game_end()
    if game_end == 1:
        if event.type == Py.MOUSEBUTTONDOWN:
            pos = Py.mouse.get_pos()
            if rect_return.collidepoint(pos):
                menu_on_clic = 0
                set_menu(menu_on_clic)

def hall_of_fame(event, barre_rect_hall_of_fame):
    if event.type == Py.MOUSEBUTTONDOWN:
        pos = Py.mouse.get_pos()
        if barre_rect_hall_of_fame.collidepoint(pos):
            menu_on_clic = 4
            set_menu(menu_on_clic)

def hall_of_fame_normal(event, rect_mode_normal):
    menu = get_menu()
    if menu == 4:
        if event.type == Py.MOUSEBUTTONDOWN:
            pos = Py.mouse.get_pos()
            if rect_mode_normal.collidepoint(pos):
                menu_on_clic = 5
                set_menu(menu_on_clic)

def hall_of_fame_survival(event, rect_mode_survival):
    menu = get_menu()
    if menu == 4:
        if event.type == Py.MOUSEBUTTONDOWN:
            pos = Py.mouse.get_pos()
            if rect_mode_survival.collidepoint(pos):
                menu_on_clic = 6
                set_menu(menu_on_clic)

def hall_of_fame_return(event, rect_return_hall):
    menu = get_menu()
    if menu == 4 or menu == 5 or menu == 6:
        if event.type == Py.MOUSEBUTTONDOWN:
            pos = Py.mouse.get_pos()
            if rect_return_hall.collidepoint(pos):
                menu_on_clic = 0
                set_menu(menu_on_clic)

def play_again(event, rect_play_again_click):
    if event.type == Py.MOUSEBUTTONDOWN:
        pos = Py.mouse.get_pos()
        if rect_play_again_click.collidepoint(pos):
            set_game_end()
        
def mouvement(event, tetramino):
    if event.type == Py.KEYDOWN:
        if event.key == Py.K_LEFT:
            direction = (-1, 0)
            value = -1
            if test_collision(direction, tetramino):
                set_tetraminos_x(value)
                set_survival_tetraminos_x(value)
        elif event.key == Py.K_RIGHT:
            direction = (1, 0)
            value = 1
            if test_collision(direction, tetramino):
                set_tetraminos_x(value)
                set_survival_tetraminos_x(value)
        elif event.key == Py.K_UP:
            menu = get_menu()
            if menu == 1:
                rotate_tetramino = set_rotate_tetramino_normal()
                if test_collision((0, 0), rotate_tetramino):
                    set_tetramino_normal(rotate_tetramino)
            elif menu == 2:
                rotate_tetramino = set_rotate_termino_survival()
                if test_collision((0, 0), rotate_tetramino):
                    set_tetramino_survival(rotate_tetramino)
        elif event.key == Py.K_DOWN:
            game_end = get_game_end()
            if not game_end:
                y_shift = 1
                while test_collision((0, y_shift), tetramino):
                    y_shift += 1
                set_tetraminos_y(get_tetraminos_y() + y_shift - 1)