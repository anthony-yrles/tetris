import pygame as Py
from globals import *
from collision import *

def normal(event, barre_rect_normal):
    if event.type == Py.MOUSEBUTTONDOWN:
        pos = Py.mouse.get_pos()
        if barre_rect_normal.collidepoint(pos):
            menu_on_clic = 1
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
        elif event.key == Py.K_RIGHT:
            direction = (1, 0)
            value = 1
            if test_collision(direction, tetramino):
                set_tetraminos_x(value)
        elif event.key == Py.K_UP:
            rotate_tetramino = set_rotate_tetramino()
            if test_collision((0, 0), rotate_tetramino):
                set_tetramino(rotate_tetramino)
        elif event.key == Py.K_DOWN:
            y_shift = 1
            while test_collision((0, y_shift), tetramino):
                y_shift += 1
            set_tetraminos_y(get_tetraminos_y() + y_shift - 1)