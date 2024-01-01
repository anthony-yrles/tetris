import pygame as Py

rect_tetriste_normal = Py.Rect(500, 20, 250, 60)
image_bcg_normal = Py.image.load('./assets/images/bcg_normal.jpg')
rect_level = Py.Rect(500, 330, 100, 50)
rect_level_count = Py.Rect(700, 330, 100, 50)
rect_ligne = Py.Rect(500, 430, 100, 50)
rect_ligne_count = Py.Rect(700, 430, 100, 50)
rect_score = Py.Rect(500, 530, 100, 50)
rect_score_count = Py.Rect(700, 530, 100, 50)
rect_display_game = Py.Rect(50, 0, 400, 600)
number_of_tile_x = 400 // 20
number_of_tile_y = 600 // 20
tile_size = 20
grid_start_x = 50
grid_start_y = 0