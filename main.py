import pygame as Py
from globals import *
from render import *
from event import *

Py.init()
clock = Py.time.Clock()

continuer = True
tetris_font = Py.font.Font('./assets/font/Tetris.ttf', 60)
font = Py.font.SysFont(None, 70)
tetramino = random_tetramino(tetraminos)

while continuer:
    render(font, tetris_font, tetramino)
    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
        normal(event, barre_rect_normal)
        mouvement(event, tetramino)
    clock.tick(60)
    Py.display.update()