import pandas as pd
import numpy as np
import operator
import sys
import spotipy
import spotipy.util as util



from prefixAlgorithm import get_prefix
from suffixAlgorithm import get_suffix
from genreAlgorithm import get_genres

def list_to_string(stringlist):
	result = ''
	for s in stringlist:
		result += s + ' '
	return result


scope = 'user-top-read'

username = 'tristankoopman'

token = util.prompt_for_user_token(username,scope,client_id='20e7931a6af8452c906815ff2270eebd',
client_secret='100e1ecfc2cc477a81dc8a789f406fde',
redirect_uri='http://localhost/')

if token:
	print('login success')
	sp = spotipy.Spotify(auth=token)

	top_artists = sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')
	top_tracks= sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')

	genre_list = get_genres(top_artists)
	user_top_genre = max(genre_list.items(), key=operator.itemgetter(1))[0]

	prefixs = get_prefix(top_artists, top_tracks, genre_list)
	user_prefix = list_to_string(prefixs)

	user_suffix = get_suffix(top_artists, top_tracks, genre_list)

	print('User ' + username + "'s MiD is: ")
	print(user_prefix + user_top_genre + ' ' + user_suffix + '!')

	
	
	
else:
	print( "Can't get token for", username)