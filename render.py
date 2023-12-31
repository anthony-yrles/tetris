import pygame as Py
import states as STATES
from globals import *
from tetramino import *

def render(font, tetris_font, tile_size):
    menu = get_menu()
    match menu:
        case STATES.MENU:
            render_menu(font, tetris_font)
        case STATES.NORMAL:
            render_normal_mode(font,tetris_font, tile_size)
        case STATES.SURVIVAL:
            render_survival_mode(tetris_font, font)
    Py.display.flip()

def render_menu(font, tetris_font):
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_tetriste)
    Py.draw.rect(screen, Py.Color(255, 255, 255), barre_rect_normal)
    Py.draw.rect(screen, Py.Color(255, 255, 255), barre_rect_time_attack)
    Py.draw.rect(screen, Py.Color(255, 255, 255), barre_rect_survival)
    Py.draw.rect(screen, Py.Color(255, 255, 255), barre_rect_hall_of_fame)
    screen.blit(image_bcg_menu, (0,0))
    text_titre = tetris_font.render('Tetriste', True, ('blue'))
    titre_text = text_titre.get_rect(center=rect_tetriste.center)
    screen.blit(text_titre, titre_text)
    text_normal = font.render('Normal', True, ('blue'))
    normal_text = text_normal.get_rect(center=barre_rect_normal.center)
    screen.blit(text_normal, normal_text)
    text_time_attack = font.render('Time attack', True, ('blue'))
    time_attack_text = text_time_attack.get_rect(center=barre_rect_time_attack.center)
    screen.blit(text_time_attack, time_attack_text)
    text_survival = font.render('Survival', True, ('blue'))
    survival_text = text_survival.get_rect(center=barre_rect_survival.center)
    screen.blit(text_survival, survival_text)
    text_hall_of_fame = font.render('Hall of Fame', True, ('blue'))
    hall_of_fame_text = text_hall_of_fame.get_rect(center=barre_rect_hall_of_fame.center)
    screen.blit(text_hall_of_fame, hall_of_fame_text)

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
        screen.fill((0,0,0))
        Py.draw.rect(screen, Py.Color(255, 255, 255), rect_tetriste)
        Py.draw.rect(screen, Py.Color(255, 255, 255), rect_game_end)
        Py.draw.rect(screen, Py.Color(255, 255, 255), rect_register)
        Py.draw.rect(screen, Py.Color(255, 255, 255), rect_play_again)
        screen.blit(image_bcg_normal, (0,0))
        Py.draw.rect(screen, Py.Color(255, 255, 255), rect_register_name)
        Py.draw.rect(screen, Py.Color(255, 255, 255), rect_play_again_click)
        text_titre = tetris_font.render('Tetriste', True, ('black'))
        titre_text = text_titre.get_rect(center=rect_tetriste.center)
        screen.blit(text_titre, titre_text)
        partie_terminé = 'Perdu, score total: ' + str(get_total_score())
        text_game_end = font.render(partie_terminé, True, ('black'))
        game_end_text = text_game_end.get_rect(center=rect_game_end.center)
        screen.blit(text_game_end, game_end_text)
        text_register = font.render('Enregistrer votre score?',True, ('black'))
        register_text = text_register.get_rect(center=rect_register.center)
        screen.blit(text_register, register_text)
        text_register_name = font.render('cliquez içi', True, ('black'))
        register_name_text = text_register_name.get_rect(center=rect_register_name.center)
        screen.blit(text_register_name, register_name_text)
        text_play_again = font.render('Une nouvelle partie',True, ('black'))
        play_again_text = text_play_again.get_rect(center=rect_play_again.center)
        screen.blit(text_play_again, play_again_text)
        text_play_again_click = font.render('cliquez içi', True, ('black'))
        play_again_click_text = text_play_again_click.get_rect(center=rect_play_again_click.center)
        screen.blit(text_play_again_click, play_again_click_text)

def render_survival_mode(tetris_font, font):
    screen.fill((0,0,0))
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_tetriste_survival)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_temps_ecoule)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_running_time)
    screen.blit(image_bcg_survival, (0,0))
    text_survival = tetris_font.render('Survival', True, ('red'))
    survival_text = text_survival.get_rect(center=rect_tetriste_survival.center)
    text_temps_ecoule = font.render('Temps écoulé', True, ('red'))
    temps_ecoule_text = text_temps_ecoule.get_rect(center=rect_temps_ecoule.center)
    text_running_time = font.render('x secondes', True, ('red'))
    running_time_text = text_running_time.get_rect(center=rect_running_time.center)
    screen.blit(text_survival, survival_text)
    screen.blit(text_temps_ecoule, temps_ecoule_text)
    screen.blit(text_running_time, running_time_text)
    game_end = get_game_end()
    if not game_end:
        for i in range(number_of_survival_tile_y):
            for j in range(number_of_survival_tile_x):
                if get_survival_grid()[i][j] == 0:
                    rect_interior_game = Py.Rect(survival_grid_start_x + j * survival_tile_size + 1, survival_grid_start_y + i * survival_tile_size + 1, survival_tile_size - 1, survival_tile_size - 1)
                    Py.draw.rect(screen, 'white', rect_interior_game)
                else:
                    set_tetraminos_y(get_tetraminos_y())
                    rect_interior_game = Py.Rect(survival_grid_start_x + j * survival_tile_size + 1, survival_grid_start_y + i * survival_tile_size + 1, survival_tile_size - 1, survival_tile_size - 1)
                    Py.draw.rect(screen, get_color(), rect_interior_game)
        dessiner_tetramino(survival_tile_size)



