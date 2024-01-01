import pygame as Py
from globals import *
from rendering import *
from event import *
from clocking import *
from globales import *

Py.init()
clock = Py.time.Clock()

continuer = True
tetris_font = Py.font.Font('./assets/font/Tetris.ttf', 60)
font = Py.font.Font('./assets/font/Tetris.ttf', 40)

while continuer:
    render(font, tetris_font, tile_size)
    menu = get_menu()
    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
        normal(event, barre_rect_normal)
        survival(event, barre_rect_survival)
        play_again(event, rect_play_again_click)
        hall_of_fame(event, barre_rect_hall_of_fame)
        hall_of_fame_normal(event, rect_mode_normal)
        hall_of_fame_survival(event, rect_mode_survival)
        if menu == 1:
            tetramino = get_tetramino_normal()
            mouvement(event, tetramino)
        elif menu == 2:
            tetramino = get_tetramino_survival()
            mouvement(event, tetramino)
    if menu == 1:
        clock.tick(get_FPS())
    if menu == 2:
        clock.tick(8)
    Py.display.update()