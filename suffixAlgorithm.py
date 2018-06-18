import pandas as pd
import numpy as np
from datetime import datetime
import operator


def get_suffix(top_artists, top_tracks, genre_list):

    possible_suffix = dict()

    user_popularity = popularity_score(top_artists)
    if user_popularity > 75:
        possible_suffix['follower'] = 3
    elif user_popularity < 52:
        possible_suffix['leader'] = 2

    num_of_genres = len(genre_list)
    if num_of_genres < 40:
        possible_suffix['cultist'] = 4
    elif num_of_genres > 90:
        possible_suffix['explorer'] = 5

    if len(possible_suffix) == 0:
        possible_suffix['individual'] = 1

    suffix = max(possible_suffix.items(), key=operator.itemgetter(1))[0]
    return suffix



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



