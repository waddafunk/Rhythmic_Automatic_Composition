# shows acoustic features for tracks for the given artist

# from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import time
import numpy
from SpotipyEnvironmentPkg import SpotipyEnvironment


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


class SpotifyFeatures:
    def __init__(self, energy, loudness, acousticness, valence, tempo, danceability, time_signature):
        self._energy = energy
        self._loudness = loudness
        self._acousticness = acousticness
        self._valence = valence
        self._tempo = tempo
        self._danceability = danceability
        self._time_signature = time_signature

    def getEnergy(self):
        return self._energy

    def getLoudness(self):
        return self._loudness

    def getAcousticness(self):
        return self._acousticness

    def getValence(self):
        return self._valence

    def getTempo(self):
        return self._tempo

    def getDanceability(self):
        return self._danceability

    def getTimeSignature(self):
        return self._time_signature

    def getNumpyArray(self):
        return numpy.array([self._energy,
                            self._loudness,
                            self._acousticness,
                            self._valence,
                            self._tempo,
                            self._danceability,
                            self._time_signature])


def getMidpoint(featuresArray):
    return numpy.mean(getMatrix(featuresArray), axis=0)


def getMatrix(featuresArray):
    temp = []
    numpyMatrix = numpy.zeros((0, 7))
    for index in enumerate(featuresArray):
        npArray = featuresArray[index[0]].getNumpyArray()
        temp.append(npArray)
        numpyMatrix = numpy.vstack((numpyMatrix, temp[-1]))
    return numpyMatrix


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
