from globals import *

def draw_tetra(forme, x, y):
    for i in range(len(forme)):
        for j in range(len(forme[i])):
            if forme[i][j] == 1:
                Py.draw.rect(screen, 'blue', (x + j * 20, y + i * 20, 20, 20))