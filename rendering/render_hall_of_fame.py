from globales import *
from json_save import *

def render_hall_of_fame(tetris_font, font, image, titre):
    screen.fill((0,0,0))
    screen.blit(image, (0,0))
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_hall_of_fame)
    text_titre = tetris_font.render(titre, True, ('blue'))
    titre_text = text_titre.get_rect(center=rect_hall_of_fame.center)
    screen.blit(text_titre, titre_text)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_mode_normal)
    text_normal = font.render('Mode Normal', True, ('blue'))
    normal_text = text_normal.get_rect(center=rect_mode_normal.center)
    screen.blit(text_normal, normal_text)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_mode_survival)
    text_survival = font.render('Mode Survival', True, ('blue'))
    survival_normal = text_survival.get_rect(center=rect_mode_survival.center)
    screen.blit(text_survival, survival_normal)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_return_hall)
    text_return = font.render('Retour', True, ('blue'))
    return_normal = text_return.get_rect(center=rect_return_hall.center)
    screen.blit(text_return, return_normal)

def render_hall_of_fame_normal(tetris_font, font, image, titre, classement_1, classement_2, classement_3):
    screen.fill((0,0,0))
    screen.blit(image, (0,0))
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_hall_of_fame)
    text_titre = tetris_font.render(titre, True, ('blue'))
    titre_text = text_titre.get_rect(center=rect_hall_of_fame.center)
    screen.blit(text_titre, titre_text)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_premier)
    text_premier = font.render(classement_1, True, ('blue'))
    premier_text = text_premier.get_rect(center=rect_premier.center)
    screen.blit(text_premier, premier_text)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_deuxieme)
    text_deuxieme = font.render(classement_2, True, ('blue'))
    deuxieme_normal = text_deuxieme.get_rect(center=rect_deuxieme.center)
    screen.blit(text_deuxieme, deuxieme_normal)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_troisieme)
    text_troisieme = font.render(classement_3, True, ('blue'))
    troisieme_normal = text_troisieme.get_rect(center=rect_troisieme.center)
    screen.blit(text_troisieme, troisieme_normal)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_return_hall)
    text_return = font.render('Retour', True, ('blue'))
    return_normal = text_return.get_rect(center=rect_return_hall.center)
    screen.blit(text_return, return_normal)

def render_hall_of_fame_survival(tetris_font, font, image, titre, classement_1, classement_2, classement_3):
    screen.fill((0,0,0))
    screen.blit(image, (0,0))
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_hall_of_fame)
    text_titre = tetris_font.render(titre, True, ('blue'))
    titre_text = text_titre.get_rect(center=rect_hall_of_fame.center)
    screen.blit(text_titre, titre_text)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_premier)
    text_premier = font.render(classement_1, True, ('blue'))
    premier_text = text_premier.get_rect(center=rect_premier.center)
    screen.blit(text_premier, premier_text)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_deuxieme)
    text_deuxieme = font.render(classement_2, True, ('blue'))
    deuxieme_normal = text_deuxieme.get_rect(center=rect_deuxieme.center)
    screen.blit(text_deuxieme, deuxieme_normal)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_troisieme)
    text_troisieme = font.render(classement_3, True, ('blue'))
    troisieme_normal = text_troisieme.get_rect(center=rect_troisieme.center)
    screen.blit(text_troisieme, troisieme_normal)
    Py.draw.rect(screen, Py.Color(255, 255, 255), rect_return_hall)
    text_return = font.render('Retour', True, ('blue'))
    return_normal = text_return.get_rect(center=rect_return_hall.center)
    screen.blit(text_return, return_normal)
