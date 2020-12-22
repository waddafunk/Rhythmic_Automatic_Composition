import json
import time
import numpy
from SpotipyEnvironmentPkg import SpotipyEnvironment

'''
CLASS SpotifyFeatures:
    Class representing features of a song
        __init__(self, energy=0, loudness=0, acousticness=0, valence=0, tempo=0, danceability=0, time_signature=0):
            Args:
                energy feature
                loudness feature
                acousticness feature
                valence feature
                tempo feature
                danceability feature
                time_signature feature    
        
        STANDARD GETTERS
        
        getNumpyArray(self):
            return: 1x7 numpy array containing all features
                 
getArtistFeatures(fromInput=False):
    Shows acoustic features for tracks for the given artist

getMidpoint(featuresArray):
    Gets midpoint of a set of features
    Args:
        features array: python array of SpotifyFeatures class
        
    return: 1x7 numpy.array containing midpont in feature space   
    
getMatrix(featuresArray):   
    Gets feature matrix of a set of features
    Args:
        features array: python array of SpotifyFeatures class
        
    return: Nx7 numpy.array with N = len(featuresArray) 
'''


def getArtistFeatures(fromInput=False):  #
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
    def __init__(self, energy=0, loudness=0, acousticness=0, valence=0, tempo=0, danceability=0, time_signature=0):
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
