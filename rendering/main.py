import pygame as Py
from globales import states as STATES
from .render_menu import *
from .render_game_end import *
from .render_normal_mode import *
from .render_survival_mode import *
from .render_hall_of_fame import *

def render(font, tetris_font, tile_size):
    menu = get_menu()
    match menu:
        case STATES.MENU:
            render_menu(font, tetris_font)
        case STATES.NORMAL:
            render_normal_mode(font,tetris_font, tile_size)
        case STATES.SURVIVAL:
            render_survival_mode(tetris_font, font)
        case STATES.HALL_OF_FAME:
            render_hall_of_fame(tetris_font, font)
        case STATES.HALL_OF_FAME_NORMAL:
            render_hall_of_fame_normal(tetris_font, font)
        case STATES.HALL_OF_FAME_SURVIVAL:
            render_hall_of_fame_survival(tetris_font, font)
    Py.display.flip()





