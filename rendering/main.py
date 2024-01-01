import pygame as Py
from globales import states as STATES
from .render_menu import *
from .render_game_end import *
from .render_normal_mode import *
from .render_survival_mode import *
from .render_hall_of_fame import *

def render(font, tetris_font, tile_size):
    menu = get_menu()
    sorted_data_normal = load_and_sort_data("player_score.json")
    sorted_data_survival = load_and_sort_data("player_time.json")
    match menu:
        case STATES.MENU:
            render_menu(font, tetris_font)
        case STATES.NORMAL:
            render_normal_mode(font,tetris_font, tile_size)
        case STATES.SURVIVAL:
            render_survival_mode(tetris_font, font)
        case STATES.HALL_OF_FAME:
            render_hall_of_fame(tetris_font, font, image_bcg_hall_of_fame, 'Hall of Fame')
        case STATES.HALL_OF_FAME_NORMAL:
            render_hall_of_fame_normal(tetris_font, font, image_bcg_hall_of_fame, 'Normal', str(sorted_data_normal[0]), str(sorted_data_normal[1]), str(sorted_data_normal[2]))
        case STATES.HALL_OF_FAME_SURVIVAL:
            render_hall_of_fame_survival(tetris_font, font, image_bcg_hall_of_fame, 'Survival', str(sorted_data_survival[0]), str(sorted_data_survival[1]), str(sorted_data_survival[2]))
        case STATES.HALL_OF_SHAME:
            render_hall_of_fame(tetris_font, font, image_bcg_hall_of_shame, 'Hall of Shame')
        case STATES.HALL_OF_SHAME_NORMAL:
            render_hall_of_fame_normal(tetris_font, font, image_bcg_hall_of_shame, 'Normal', str(sorted_data_normal[-1]), str(sorted_data_normal[-2]), str(sorted_data_normal[-3]))
        case STATES.HALL_OF_SHAME_SURVIVAL:
            render_hall_of_fame_survival(tetris_font, font, image_bcg_hall_of_shame, 'Survival', str(sorted_data_survival[-1]), str(sorted_data_survival[-2]), str(sorted_data_survival[-3]))
    Py.display.flip()





