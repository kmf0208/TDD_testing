class TrackMusic():
    def __init__(self):
        self._tracks = []
    def add_track(self, track):
        if track == '':
            raise Exception('no track to add')

        return self._tracks.append(track)

    def remove_track(self, track):
        if self._tracks == [] or track not in self._tracks:
            raise Exception('track may be empty of track is not in the tracklist') 
        return self._tracks.remove(track)

    def track_lists(self):
        return self._tracks