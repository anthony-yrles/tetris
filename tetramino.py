from globals import *
from collision import *
from remplissage import *

def dessiner_tetramino(tile_size):
    draw_x = grid_start_x + get_tetraminos_x() * tile_size
    draw_y = 0 + get_tetraminos_y() * tile_size
    tetramino = get_tetramino()
    dessiner_tetramino_aux(tetramino, draw_x, draw_y, tile_size)
    # next_tetramino = draw_next_tetarmino(tile_size)
    # set_next_tetramino(tetraminos)
    if test_collision((0, 1), tetramino):
        set_tetraminos_y(1)
    else:
        if not test_loose():
            set_grid(tetramino, draw_x, draw_y, tile_size)
            set_tetramino(random_tetramino(tetraminos))
            set_tetraminos_y(0)
            set_tetraminos_x(10)
            test_ligne()
            dessiner_tetramino_aux(tetramino, draw_x, draw_y, tile_size)
        else:
            set_initial_value()
            set_game_end()

# def draw_next_tetarmino(tile_size):
#     next_tetramino = get_next_tetramino()

#     # Si next_tetramino n'est pas défini, générez-en un nouveau
#     if next_tetramino is None:
#         next_tetramino = random_tetramino(tetraminos)

#     for coord in next_tetramino:
#         rect_x = 620 + coord[1] * tile_size
#         rect_y = 150 + coord[0] * tile_size
#         Py.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (rect_x, rect_y, tile_size, tile_size))
#     return next_tetramino

def dessiner_tetramino_aux(tetramino, draw_x, draw_y, tile_size):
    # if tetramino is not None:
    for coord in tetramino:
        rect_x = draw_x + coord[1] * tile_size
        rect_y = draw_y + coord[0] * tile_size
        Py.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (rect_x, rect_y, tile_size, tile_size))