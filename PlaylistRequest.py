
import sys
import spotipy
import spotipy.util as util


def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))


scope = 'playlist-read-private'

username = 'tristankoopman'

token = util.prompt_for_user_token(username,scope,client_id='20e7931a6af8452c906815ff2270eebd',
client_secret='100e1ecfc2cc477a81dc8a789f406fde',
redirect_uri='http://localhost:8888/callback/')

if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print
                print (playlist['name'])
                print ('  total tracks', playlist['tracks']['total'])
                results = sp.user_playlist(username, playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
else:
    print( "Can't get token for", username)