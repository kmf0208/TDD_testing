As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

we want to add a remove track
show the list of all added track



class TrackMusic():
    def __init__(self, name):
        # Parameters:
        #a list to store tracks

    def add_track(self, track):
        # Parameters:
        #   task: string representing a single track to be added

    def remove_track(self, track):
        # Returns:
        #   A string representing a single track to be removed of the list
        Throws an exception if no track to remove

    def track_list():
         return the track list


track_music = TrackMusic()
track_music.track_list => []


track_music = TrackMusic()
track_music.add_track('hello')
track_music.track_list => ['hello']

track_music = TrackMusic()
track_music.add_track('')
track_music.track_list => exception(no track to add)

track_music = TrackMusic()
track_music.add_track('hello')
track_music.add_track('other side')
track_music.track_list => ['hello', 'other side']


track_music = TrackMusic()
track_music.add_track('hello')
track_music.add_track('other side')
track_music.remove_track('other side')
track_music.track_list => ['hello']

track_music = TrackMusic()
track_music.remove_track() => exception("nothing in the list to remove")