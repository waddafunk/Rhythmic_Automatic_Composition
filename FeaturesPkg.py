# shows acoustic features for tracks for the given artist

# from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import time
import sys
from SpotipyEnvironmentPkg import SpotipyEnvironment

from PlaylistPkg import getPlaylistIds


def getArtistFeatures(fromInput=False):
    client_credentials_manager = SpotifyClientCredentials()
    sp = SpotipyEnvironment().sp
    sp.trace = False

    if fromInput:
        artist_name = input("Give me the artist name")
    else:
        artist_name = 'A Tribe Called Quest'

    results = sp.search(q=artist_name, limit=50)
    tids = []
    for i, t in enumerate(results['tracks']['items']):
        print(' ', i, t['name'])
        tids.append(t['uri'])

    start = time.time()
    features = sp.audio_features(tids)
    delta = time.time() - start
    for feature in features:
        print(json.dumps(feature, indent=4))
        print()
        analysis = sp._get(feature['analysis_url'])
        print(json.dumps(analysis, indent=4))
        print()
    print("features retrieved in %.2f seconds" % (delta,))


def menu():
    usrInput = input("type \"get\" to get ATCQ features, \"get_custom\" to get other artists features, "
                     "anything else will quit\n")
    if usrInput == "get":
        getArtistFeatures()
    elif usrInput == "get_custom":
        getArtistFeatures(True)
    else:
        print("wrong input")


if __name__ == "__main__":
    menu()
