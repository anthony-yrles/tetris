from globals import *

def test_collision(direction, tetramino):
    x = get_tetraminos_x()
    y = get_tetraminos_y()
    grid = get_grid()
    for coords in tetramino:
        new_x = x + coords[1] + direction[0]
        new_y = y + coords[0] + direction[1]
        if new_x < 0 or new_x > 19 or new_y > 29 or grid[new_y][new_x] != 0:
            return False
    return True

def test_rotation():
    if get_tetraminos_x() < 0 or get_tetraminos_x() > 19 or get_tetraminos_y() > 29 or grid[get_tetraminos_y()][get_tetraminos_x()] != 0:
        return False
    return True