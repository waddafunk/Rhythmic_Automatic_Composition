import os
import pathlib
import time

import librosa
import pydub
from pydub import playback

from Track import Track


def getTracks(path):  # returns list of all wav files in "path" directory
    tracks_collection = [f for f in os.listdir(path) if f.endswith('.wav')]
    return tracks_collection


# begin init
projectPath = pathlib.Path(__file__).parent.absolute()  # get path of the project
multiTrackPath = pathlib.Path(str(projectPath) + '/multitrack/lofi_1')  # append desired multitrack path
tracks = getTracks(multiTrackPath)
outputMix = []
tracksObjects = []
firstTrackPath = pathlib.Path(str(multiTrackPath) + '/{}'.format(tracks[0]))
signal, rate = librosa.load(firstTrackPath, sr=None, mono=False)

mixedAudio = pydub.AudioSegment.from_file(firstTrackPath, format='wav')  # load first track
outputMix.append(mixedAudio)  # append first track
# end init

for index in enumerate(tracks):  # load tracks
    singleTrackPath = pathlib.Path(str(multiTrackPath) + '/{}'.format(index[1]))  # append single track name
    audio, fs = librosa.load(singleTrackPath, sr=None, mono=False)  # load track

    # begin append and mix track
    tracksObjects.append(Track(singleTrackPath)) # store track object

    if index[0] != 0:
        segment = tracksObjects[-1].getPydubTrack()  # get track to overlay
        mix = outputMix[-1].overlay(segment)  # overlay to output mix
        outputMix.append(mix)  # append new mix
    # end append and mix track

playback._play_with_simpleaudio(outputMix[-1])  # play last appended track (complete one)
time.sleep(len(outputMix[-1]) / 1000 + 1)  # wait for the track to end + 1 sec

