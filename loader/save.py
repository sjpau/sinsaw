import pygame
import json

chapter_save = {
    'Completed': False,
    'AchMaxKills': False,
    'AchMinTurns': False,
}

game_save = {
    'Night Shift': chapter_save,
    'The Afterparty': chapter_save,
    'Carte Blanche': chapter_save,
}

def save_game_data(game_save_arg):
    with open("cache.ssf", "w") as save_file:
        json.dump(game_save_arg, save_file)

def load_game_data():
    global game_save
    try:
        with open("cache.ssf", "r") as save_file:
            game_save = json.load(save_file)
    except EnvironmentError:
        print('No cache file found, creating default. This wipes any progress, if you have an existing cache file dump it here.')
        save_game_data(game_save)