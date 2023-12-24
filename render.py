import pygame as Py
import states as STATES
from globals import *
from tetramino import *

def render(font, tetris_font):
    menu = get_menu()
    match menu:
        case STATES.MENU:
            render_menu(tetris_font, font)
        case STATES.NORMAL:
            render_normal_mode()
    Py.display.flip()

def render_menu(tetris_font, font):
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_tetriste)
    screen.blit(image_bcg_menu, (0,0))
    text_titre = tetris_font.render('Tetriste', True, (255, 0, 0))
    titre_text = text_titre.get_rect(center=rect_tetriste.center)
    screen.blit(text_titre, titre_text)
    Py.draw.rect(screen, Py.Color(255, 255, 255), barre_rect_normal)
    screen.blit(image_barre_menu, (50,250))
    text_normal = font.render('Normal', True, (255, 0, 0))
    normal_text = text_normal.get_rect(center=barre_rect_normal.center)
    screen.blit(text_normal, normal_text)
    Py.draw.rect(screen, Py.Color(255, 255, 255), barre_rect_time_attack)
    screen.blit(image_barre_menu, (50,450))
    text_time_attack = font.render('Time attack', True, (255, 0, 0))
    time_attack_text = text_time_attack.get_rect(center=barre_rect_time_attack.center)
    screen.blit(text_time_attack, time_attack_text)
    Py.draw.rect(screen, Py.Color(255, 255, 255), barre_rect_survival)
    screen.blit(image_barre_menu, (450,250))
    text_survival = font.render('Survival', True, (255, 0, 0))
    survival_text = text_survival.get_rect(center=barre_rect_survival.center)
    screen.blit(text_survival, survival_text)
    Py.draw.rect(screen, Py.Color(255, 255, 255), barre_rect_hall_of_fame)
    screen.blit(image_barre_menu, (450,450))
    text_hall_of_fame = font.render('Hall of Fame', True, (255, 0, 0))
    hall_of_fame_text = text_hall_of_fame.get_rect(center=barre_rect_hall_of_fame.center)
    screen.blit(text_hall_of_fame, hall_of_fame_text)

def render_normal_mode():
    screen.fill((0,0,0))
    screen.blit(image_bcg_normal, (0,0))
    Py.draw.rect(screen, 'black', rect_display_game)
    for i in range(number_of_tile_y):
        for j in range(number_of_tile_x):
            if get_grid()[i][j] == 0:
                rect_interior_game = Py.Rect(grid_start_x + j * tile_size + 1, grid_start_y + i * tile_size + 1, tile_size - 1, tile_size - 1)
                Py.draw.rect(screen, 'white', rect_interior_game)
    dessiner_tetramino()

