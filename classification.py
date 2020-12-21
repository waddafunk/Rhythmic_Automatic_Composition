from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import numpy as np
from pprint import pprint
import os
import re
os.environ['SPOTIPY_CLIENT_ID'] = '7ce43cbf9883427e84fa7581dbac0f83'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'b60c4489024d403c911865b67d264d88'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

pl_id = 'spotify:playlist:0XgEPjlWTX4g4HjBNhtZIL'
offset = 0
songs = []
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

#print(str(songs))
#print(str(songs).split(','))

stringa = str(sp.playlist_items(pl_id,fields='items.track.id'))
print(stringa)
print(len(stringa))
stri = stringa.split(", ")
print((stri)[0])
print(len(stri))



for i in range(len(stri)):
    text = (stri)[i]

    m = re.search('id\': \'(.+?)\'}}', text)
    if m:
     found = m.group(1)
    print(found)
    print(sp.audio_features(found))
    audio_features = str(sp.audio_features(found))
    #print(len(audio_features))
    n = re.search('energy\': (.+?), ', audio_features)
    if n:
     energy = n.group(1)
     energy=float(energy)

    n = re.search('loudness\': (.+?), ', audio_features)
    if n:
        loudness = n.group(1)
    loudness=float(loudness)

    n = re.search('acousticness\': (.+?), ', audio_features)
    if n:
        acousticness = n.group(1)
    acousticness=float(acousticness)

    n = re.search('valence\': (.+?), ', audio_features)
    if n:
        valence = n.group(1)
    valence = float(valence)

    n = re.search('tempo\': (.+?), ', audio_features)
    if n:
        tempo = n.group(1)
    tempo=float(tempo)

    n = re.search('danceability\': (.+?), ', audio_features)
    if n:
        danceability = n.group(1)
    danceability=float(danceability)

    n = re.search('time_signature\': (.+?)}]', audio_features)
    if n:
        time_signature = n.group(1)
    time_signature=float(time_signature)



'''stri = stringa.split(", ")
print((stri)[0])
print(len(stri))

for i in len(stri):'''











'''for i in range(len(songs)):
    id = str(songs[i]).split(" '")
    id2=str(id).split("'}")
    #print(id2)
    ids.append(id2)

print(ids)

    #print(sp.audio_features(id_))'''


