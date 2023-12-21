import pygame as Py
from globals import *

def normal(event, barre_rect_normal):
    if event.type == Py.MOUSEBUTTONDOWN:
        pos = Py.mouse.get_pos()
        if barre_rect_normal.collidepoint(pos):
            menu_on_clic = 1
            set_menu(menu_on_clic)
