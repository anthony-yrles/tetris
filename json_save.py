import json

def save_time(new_score):
    try:
        with open("player_time.json", "r") as time_file:
            time_list = json.load(time_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        time_list = []
    time_list.append(new_score)
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

def load_and_sort_data(filename):
    try:
        with open(filename, "r") as data_file:
            data_list = json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []
    sorted_data = sorted(data_list, reverse=True)
    return sorted_data
