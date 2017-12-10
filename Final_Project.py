import unittest
import itertools
import collections
import sys
import spotify_info
import spotipy
import spotipy.util as util
import json
import sqlite3
import os
import oauth

#username = 'derekg608'
#scope = 'user-library-read'
#redirect_uri = 'https://example.com/callback/'

#os.environ["SPOTIPY_CLIENT_ID"] = spotify_info.client_id
#os.environ["SPOTIPY_CLIENT_SECRET"] = spotify_info.client_secret
#os.environ["SPOTIPY_REDIRECT_URI"] = spotify_info.spotify_redirect_url

scope = 'user-library-read'
username = 'derekg608'

util.prompt_for_user_token(username,scope,client_id='55192119e073409eb2486655e9ebafb8',client_secret='04581f38112541d481ef1b55484b46e6',redirect_uri='http://127.0.0.1/callback')

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)

CACHE_FNAME = "Spotify_Cache.json"

try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

def get_spotify_data():
    pass
