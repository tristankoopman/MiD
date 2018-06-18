import pandas as pd
import numpy as np
from datetime import datetime


def get_prefix(top_artists, top_tracks, genre_list):

    possible_prefix = dict()

    avg_track_date = user_avg_release_date(top_tracks)
    if avg_track_date < 1990:
        possible_prefix['retro'] = 1
    elif avg_track_date < 2000:
        possible_prefix['classic'] = 1

    user_popularity = popularity_score(top_artists)
    if user_popularity > 75:
        possible_prefix['band wagon'] = 1
    elif user_popularity < 52:
        possible_prefix['hipstery'] = 1

    num_of_genres = len(genre_list)
    if num_of_genres < 40:
        possible_prefix['passionate'] = 1
    elif num_of_genres > 90:
        possible_prefix['adventerous'] = 1

    holy_genres = ('christian rock', 'christian music', 'gospel', 'christian hip hop', 'christian metal', 'southern gospel', 'gospel music', 'spiritual', 'christian country')
    if any(genre in genre_list.keys() for genre in holy_genres):
        possible_prefix['holy'] = 1

    party_genres = ('trap music', 'bounce', 'dubstep')
    if any(genre in genre_list.keys() for genre in party_genres):
        possible_prefix['turnt'] = 1

    if len(possible_prefix) == 0:
        possible_prefix['one of a kind'] = 1

    prefix = list(possible_prefix.keys())
    return prefix



def popularity_score(top_artists):
	popularity_count = 0
	for artist in top_artists['items']:
		popularity_count += artist['popularity']
	popularity_score = popularity_count/top_artists['total']
	return popularity_score

def user_avg_release_date(top_tracks):
    user_avg_date = 0
    for track in top_tracks['items']:
        if track['album']['release_date_precision'] == 'day':
            release_date= track['album']['release_date']
            dt = datetime.strptime(release_date, '%Y-%m-%d')
            user_avg_date += dt.year
        elif track['album']['release_date_precision'] == 'year':
            release_date = int(track['album']['release_date'])
            user_avg_date += release_date
    user_avg_date = user_avg_date/top_tracks['total']
    return user_avg_date



