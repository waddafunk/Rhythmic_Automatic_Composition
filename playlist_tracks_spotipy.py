from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint
import os

# Set environment variables
os.environ['SPOTIPY_CLIENT_ID'] = '7ce43cbf9883427e84fa7581dbac0f83'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'b60c4489024d403c911865b67d264d88'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

pl_id = input("Give me playlist ID\n")
#pl_id = 'spotify:playlist:4M54T82f6qWjpX0ib34a6T'
offset = 0

while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])

    if len(response['items']) == 0:
        break

    pprint(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])