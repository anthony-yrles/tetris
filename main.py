import pygame as Py
from globals import *
from render import *
from event import *

Py.init()
clock = Py.time.Clock()

continuer = True
tetris_font = Py.font.Font('./assets/font/Tetris.ttf', 60)
font = Py.font.Font('./assets/font/Tetris.ttf', 40)

while continuer:
    render(font, tetris_font, tile_size)
    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
        normal(event, barre_rect_normal)
        survival(event, barre_rect_survival)
        play_again(event, rect_play_again_click)
        menu = get_menu()
        if menu == 1:
            tetramino = get_tetramino_normal()
            mouvement(event, tetramino)
        elif menu == 2:
            tetramino = get_tetramino_survival()
            mouvement(event, tetramino)
    clock.tick(get_FPS())
    Py.display.update()