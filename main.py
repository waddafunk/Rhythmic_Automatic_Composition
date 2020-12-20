import pathlib

import pydub
from pydub import playback, effects

from TrackPkg import Track, getTracks
from PlaylistPkg import getPlaylistIds
from spotipyEnvironment import SpotipyEnvironment

# begin init
# begin set spotipy environment variables
env = SpotipyEnvironment()
sp = env.sp

pl_id = env.pl_id
offset = env.offset
# end set spotipy environment variables

getPlaylistIds(sp, pl_id, offset)  # playlist ids

projectPath = pathlib.Path(__file__).parent.absolute()  # get path of the project
multiTrackPath = pathlib.Path(str(projectPath) + '/multitrack/lofi_2')  # append desired multitrack path
tracks = getTracks(multiTrackPath)
outputMix = []
tracksObjects = []
firstTrackPath = pathlib.Path(str(multiTrackPath) + '/{}'.format(tracks[0]))
mixedAudio = pydub.AudioSegment.from_file(firstTrackPath, format='wav')  # load first track
outputMix.append(mixedAudio)  # append first track
# end init
for index in enumerate(tracks):  # load tracks

    singleTrackPath = pathlib.Path(str(multiTrackPath) + '/{}'.format(index[1]))  # append single track name

    # begin append and mix track
    tracksObjects.append(Track(singleTrackPath))  # store track object

    if index[0] != 0:
        segment = tracksObjects[-1].getPydubTrack()  # get track to overlay
        mix = outputMix[-1].overlay(segment)  # overlay to output mix
        outputMix.append(mix)  # append new mix
    # end append and mix track

playback.play(effects.normalize(outputMix[-1], headroom=3))  # play last appended track (complete one)
