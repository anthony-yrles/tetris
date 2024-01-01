from globales import *

def test_collision(direction, tetramino):
    menu = get_menu()
    if menu == 1:
        x = get_tetraminos_x()
        y = get_tetraminos_y()
        grid = get_grid()
        for coords in tetramino:
            new_x = x + coords[1] + direction[0]
            new_y = y + coords[0] + direction[1]
            if new_x < 0 or new_x > 19 or new_y > 29 or (new_y >= 0 and grid[new_y][new_x] != 0):
                return False
        return True
    if menu == 2:
        x = get_survival_tetraminos_x()
        y = get_tetraminos_y()
        grid = get_survival_grid()
        for coords in tetramino:
            new_x = x + coords[1] + direction[0]
            new_y = y + coords[0] + direction[1]
            if new_x < 0 or new_x > 13 or new_y > 19 or (new_y >= 0 and grid[new_y][new_x] != 0):
                return False
        return True

def test_lose():
    y = get_tetraminos_y()
    if y == 0:
        return True
    return False
