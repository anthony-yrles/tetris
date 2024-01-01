from globales import *

def render_end_game(tetris_font, font, score):
    screen.fill((0,0,0))
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_tetriste)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_game_end)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_play_again)
    screen.blit(image_bcg_normal, (0,0))
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_play_again_click)
    text_titre = tetris_font.render('Tetriste', True, ('black'))
    titre_text = text_titre.get_rect(center=rect_tetriste.center)
    screen.blit(text_titre, titre_text)
    partie_terminé = 'Perdu, score total: ' + score
    text_game_end = font.render(partie_terminé, True, ('black'))
    game_end_text = text_game_end.get_rect(center=rect_game_end.center)
    screen.blit(text_game_end, game_end_text)
    text_play_again = font.render('Une nouvelle partie',True, ('black'))
    play_again_text = text_play_again.get_rect(center=rect_play_again.center)
    screen.blit(text_play_again, play_again_text)
    text_play_again_click = font.render('cliquez içi', True, ('black'))
    play_again_click_text = text_play_again_click.get_rect(center=rect_play_again_click.center)
    screen.blit(text_play_again_click, play_again_click_text)