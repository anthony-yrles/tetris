import json

def save_time(new_score):
    try:
        # Essayer de charger le fichier JSON existant
        with open("player_time.json", "r") as time_file:
            time_list = json.load(time_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # Si le fichier n'existe pas ou est vide, initialiser la liste à vide
        time_list = []

    # Ajouter le nouveau score à la liste
    time_list.append(new_score)

    # Sauvegarder la liste mise à jour dans le fichier JSON
    with open("player_time.json", "w") as time_file:
        json.dump(time_list, time_file, indent=2)

def save_score(new_score):
    try:
        with open("player_score.json", "r") as score_file:
            score_list = json.load(score_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        score_list = []
    score_list.append(new_score)
    with open("player_score.json", "w") as score_file:
        json.dump(score_list, score_file, indent=2)
