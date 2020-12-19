import os
import pathlib
import librosa


def getTracks(path):  # returns list of all wav files in "path" directory
    tracks_collection = [f for f in os.listdir(path) if f.endswith('.wav')]
    return tracks_collection


# begin init
projectPath = pathlib.Path(__file__).parent.absolute()  # get path of the project
multiTrackPath = pathlib.Path(str(projectPath) + '/multitrack/lofi_1')  # append desired multitrack path
tracks = getTracks(multiTrackPath)
audioObject = {'files': [], 'samplingFreqs': []}  # contains audio files and relative sampling freqs
# end init

for index in enumerate(tracks):  # load tracks
    singleTrackPath = pathlib.Path(str(multiTrackPath) + '/{}'.format(index[1]))  # append single track name
    audio, fs = librosa.load(singleTrackPath, sr=None)
    audioObject['files'].append(audio)
    audioObject['samplingFreqs'].append(fs)

print(audioObject)
