import pygame as Py
import time

image_bcg_survival = Py.image.load('./assets/images/bcg_survival.jpg')
rect_tetriste_survival = Py.Rect(50, 20, 250, 60)
rect_temps_ecoule = Py.Rect(50, 250, 250, 60)
rect_running_time = Py.Rect(50, 350, 250, 60)
survival_tile_size = 30
number_of_survival_tile_x = 420 // survival_tile_size
number_of_survival_tile_y = 600 // survival_tile_size
survival_grid_start_x = 350
survival_grid_start_y = 0
time_begin = time.time()