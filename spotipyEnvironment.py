from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os


class SpotipyEnvironment:
    os.environ['SPOTIPY_CLIENT_ID'] = '7ce43cbf9883427e84fa7581dbac0f83'
    os.environ['SPOTIPY_CLIENT_SECRET'] = 'b60c4489024d403c911865b67d264d88'
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    pl_id = 'spotify:playlist:4M54T82f6qWjpX0ib34a6T'
    offset = 0
