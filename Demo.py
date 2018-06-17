import pandas as pd
import numpy as np
import sys
import spotipy
import spotipy.util as util

sp = spotipy.Spotify()

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print ' ', i, t['name']