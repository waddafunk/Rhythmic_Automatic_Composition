import os
import pathlib


def getTracks(path):
    fullpath = str(path) + '/multitrack/lofi_1'
    tracks = [f for f in os.listdir(fullpath) if f.endswith('.wav')]
    return tracks


path = pathlib.Path(__file__).parent.absolute()
tracks = getTracks(path)
for track in tracks:
    print(track)






