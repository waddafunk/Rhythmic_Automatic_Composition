import os

import librosa
import pydub
from pydub import playback

'''
CLASS Track:
    Class representing a track to play
        __init__(self, path):
            Args:
                path: path to wav file   

        STANDARD GETTERS

        play(self):
            play track

getTracks(path):
    Gets tracs in a folder
    Args:
        path: path to multitrack folder
        
    return: 1xN python array containing all wav files in Args:path folder
'''


class Track:
    def __init__(self, path):
        self._path = path  # path to wav file
        self._signal, self._rate = librosa.load(path, sr=None, mono=False)  # librosa array (for analisys only)
        self._pydubTrack = pydub.AudioSegment.from_file(path, format='wav')  # track to play back

    def getPydubTrack(self):
        return self._pydubTrack

    def getSignal(self):
        return self._signal

    def getSampleRate(self):
        return self._rate

    def getPath(self):
        return self._path

    def play(self):  # play track
        playback.play(self._pydubTrack)


def getTracks(path):  # returns list of all wav files in "path" directory
    tracks_collection = [f for f in os.listdir(path) if f.endswith('.wav')]
    return tracks_collection
