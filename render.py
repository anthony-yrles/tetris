import pygame as Py
import states as STATES
from render_menu import *
from render_normal_mode import *
from render_survival_mode import *

def render(font, tetris_font, tile_size):
    menu = get_menu()
    match menu:
        case STATES.MENU:
            render_menu(font, tetris_font)
        case STATES.NORMAL:
            render_normal_mode(font,tetris_font, tile_size)
        case STATES.SURVIVAL:
            render_survival_mode(tetris_font, font)
    Py.display.flip()





