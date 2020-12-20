from pprint import pprint


def getPlaylistIds(sp, pl_id, offset):
    while True:
        response = sp.playlist_items(pl_id,
                                     offset=offset,
                                     fields='items.track.id,total',
                                     additional_types=['track'])

        if len(response['items']) == 0:
            break

        pprint(response['items'])
        offset = offset + len(response['items'])
        print(offset, "/", response['total'])