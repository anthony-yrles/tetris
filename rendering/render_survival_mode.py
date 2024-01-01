from globals import *
from globales import *
from tetramino import *
from rendering.render_game_end import *
from clocking import *

def render_survival_mode(tetris_font, font):
    screen.fill((0,0,0))
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_tetriste_survival)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_temps_ecoule)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_running_time)
    screen.blit(image_bcg_survival, (0,0))
    text_survival = tetris_font.render('Survival', True, ('red'))
    survival_text = text_survival.get_rect(center=rect_tetriste_survival.center)
    text_temps_ecoule = font.render('Temps écoulé', True, ('red'))
    screen.blit(text_survival, survival_text)
    game_end = get_game_end()
    if not game_end:
        time_running = chrono()
        secondes = str(int(time_running)) + ' secondes'
        temps_ecoule_text = text_temps_ecoule.get_rect(center=rect_temps_ecoule.center)
        text_running_time = font.render(secondes, True, ('red'))
        running_time_text = text_running_time.get_rect(center=rect_running_time.center)
        screen.blit(text_temps_ecoule, temps_ecoule_text)
        screen.blit(text_running_time, running_time_text)
        for i in range(number_of_survival_tile_y):
            for j in range(number_of_survival_tile_x):
                if get_survival_grid()[i][j] == 0:
                    rect_interior_game = Py.Rect(survival_grid_start_x + j * survival_tile_size + 1, survival_grid_start_y + i * survival_tile_size + 1, survival_tile_size - 1, survival_tile_size - 1)
                    Py.draw.rect(screen, 'white', rect_interior_game)
                else:
                    set_tetraminos_y(get_tetraminos_y())
                    rect_interior_game = Py.Rect(survival_grid_start_x + j * survival_tile_size + 1, survival_grid_start_y + i * survival_tile_size + 1, survival_tile_size - 1, survival_tile_size - 1)
                    Py.draw.rect(screen, get_color(), rect_interior_game)
        dessiner_tetramino(survival_tile_size, int(time_running))
    if game_end:
        time_running = get_time_end_game()
        score = str(int(time_running))
        render_end_game(tetris_font, font, score)