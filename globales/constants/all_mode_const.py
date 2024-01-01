import pygame as Py
from random import randrange

screen = Py.display.set_mode((800, 600))
get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))