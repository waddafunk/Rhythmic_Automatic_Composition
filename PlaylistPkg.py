from pprint import pprint
from spotipyEnvironment import SpotipyEnvironment

env = SpotipyEnvironment()


def getPlaylistIds(fromInput=False):
    if fromInput:
        input_id = input("Give me playlist ID\n")
    else:
        input_id = env.pl_id

    response = env.sp.playlist_items(input_id,
                                     offset=env.offset,
                                     fields='items.track.id,total',
                                     additional_types=['track'])

    pprint(response['items'])
    offset = env.offset + len(response['items'])
    print(offset, "/", response['total'])


if __name__ == "__main__":
    getPlaylistIds(True)
