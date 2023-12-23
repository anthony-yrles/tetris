import pygame as Py
from globals import *
from collision import *

def normal(event, barre_rect_normal):
    if event.type == Py.MOUSEBUTTONDOWN:
        pos = Py.mouse.get_pos()
        if barre_rect_normal.collidepoint(pos):
            menu_on_clic = 1
            set_menu(menu_on_clic)

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