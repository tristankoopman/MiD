import pandas as pd
import numpy as np
import operator


def get_genres(top_artists):
    genre_list = dict()
    
    for artist in top_artists['items']:
        for genre in artist['genres']:
            genre_list = add_genre(genre, genre_list)
    
    return genre_list
    


def add_genre(genre, genre_list):
    if genre in genre_list.keys():
        count = genre_list[genre]
        genre_list[genre] = count + 1
    else:
        genre_list[genre] = 1

    return genre_list


