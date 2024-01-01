from globals import *
from tetramino import *
from render_game_end import *

def render_normal_mode(font, tetris_font, tile_size):
    screen.fill((0,0,0))
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_tetriste_normal)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_level)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_level_count)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_ligne)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_ligne_count)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_score)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_score_count)
    screen.blit(image_bcg_normal, (0,0))
    Py.draw.rect(screen, 'black', rect_display_game)
    text_titre = tetris_font.render('Tetriste', True, ('black'))
    titre_text = text_titre.get_rect(center=rect_tetriste_normal.center)
    text_level = font.render('Level :', True, ('black'))
    level_text = text_level.get_rect(center=rect_level.center)
    text_level_count = font.render(str(get_level()), True, ('black'))
    level_count_text = text_level_count.get_rect(center=rect_level_count.center)
    text_ligne = font.render('Lignes :', True, ('black'))
    ligne_text = text_ligne.get_rect(center=rect_ligne.center)
    text_ligne_count = font.render(str(get_completed_lignes()), True, ('black'))
    ligne_count_text = text_ligne_count.get_rect(center=rect_ligne_count.center)
    text_score = font.render('Score :', True, ('black'))
    score_text = text_score.get_rect(center=rect_score.center)
    text_score_count = font.render(str(get_total_score()), True, ('black'))
    score_count_text = text_score_count.get_rect(center=rect_score_count.center)
    screen.blit(text_titre, titre_text)
    screen.blit(text_level, level_text)
    screen.blit(text_level_count, level_count_text)
    screen.blit(text_ligne, ligne_text)
    screen.blit(text_ligne_count, ligne_count_text)
    screen.blit(text_score, score_text)
    screen.blit(text_score_count, score_count_text)
    game_end = get_game_end()
    if not game_end:
        for i in range(number_of_tile_y):
            for j in range(number_of_tile_x):
                if get_grid()[i][j] == 0:
                    rect_interior_game = Py.Rect(grid_start_x + j * tile_size + 1, grid_start_y + i * tile_size + 1, tile_size - 1, tile_size - 1)
                    Py.draw.rect(screen, 'white', rect_interior_game)
                else:
                    set_tetraminos_y(get_tetraminos_y())
                    rect_interior_game = Py.Rect(grid_start_x + j * tile_size + 1, grid_start_y + i * tile_size + 1, tile_size - 1, tile_size - 1)
                    Py.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rect_interior_game)
        dessiner_tetramino(tile_size)
    if game_end:
        score = str(get_total_score())
        render_end_game(tetris_font, font, score)