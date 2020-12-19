import os
import pathlib
import time

import librosa
import pydub
from pydub import playback


def getTracks(path):  # returns list of all wav files in "path" directory
    tracks_collection = [f for f in os.listdir(path) if f.endswith('.wav')]
    return tracks_collection


# begin init
projectPath = pathlib.Path(__file__).parent.absolute()  # get path of the project
multiTrackPath = pathlib.Path(str(projectPath) + '/multitrack/lofi_1')  # append desired multitrack path
tracks = getTracks(multiTrackPath)
librosaAudioObject = {'files': [], 'samplingFreqs': []}  # contains audio files and relative sampling freqs
pydubTracks = []
firstTrackPath = pathlib.Path(str(multiTrackPath) + '/{}'.format(tracks[0]))
signal, rate = librosa.load(firstTrackPath, sr=None, mono=False)

mixedAudio = pydub.AudioSegment.from_file(firstTrackPath, format='wav')  # load first track
pydubTracks.append(mixedAudio)  # append first track
# end init

for index in enumerate(tracks):  # load tracks
    singleTrackPath = pathlib.Path(str(multiTrackPath) + '/{}'.format(index[1]))  # append single track name
    audio, fs = librosa.load(singleTrackPath, sr=None, mono=False)  # load track

    # begin append and mix track
    librosaAudioObject['files'].append(audio)
    librosaAudioObject['samplingFreqs'].append(fs)
    channel1 = audio[:, 0]

    if index[0] != 0:
        segment = pydub.AudioSegment.from_file(singleTrackPath, format='wav')
        mix = pydubTracks[-1].overlay(segment)
        pydubTracks.append(mix)
    # end append and mix track

playback._play_with_simpleaudio(pydubTracks[-1])  # play track
time.sleep(len(pydubTracks[-1]) / 1000)  # wait for the track to end


print(librosaAudioObject)  # print librosa object (not used for now)
