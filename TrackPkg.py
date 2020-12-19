import os

import librosa
import pydub
from pydub import playback


class Track:
    def __init__(self, path):
        self.path = path  # path to wav file
        self.signal, self.rate = librosa.load(path, sr=None, mono=False)  # librosa array (for analisys only)
        self.pydubTrack = pydub.AudioSegment.from_file(path, format='wav') # track to play back

    def getPydubTrack(self):
        return self.pydubTrack

    def getSignal(self):
        return self.signal

    def getSampleRate(self):
        return self.rate

    def play(self):  # play track
        playback._play_with_simpleaudio(self.pydubTrack)


def getTracks(path):  # returns list of all wav files in "path" directory
    tracks_collection = [f for f in os.listdir(path) if f.endswith('.wav')]
    return tracks_collection
