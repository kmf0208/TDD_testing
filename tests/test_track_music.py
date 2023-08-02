from lib.track_music import TrackMusic
import pytest




def test_track_list_return_empty_list():
    track_music = TrackMusic()
    assert track_music.track_lists() == []


def test_add_track_to_list():
    track_music = TrackMusic()
    track_music.add_track('hello')
    assert track_music.track_lists() == ['hello']

def test_add_multi_track_to_list():
    track_music = TrackMusic()
    track_music.add_track('hello')
    track_music.add_track('other side')
    assert track_music.track_lists() == ['hello', 'other side']

def test_add_empty_string_to_tracks():
    track_music = TrackMusic()
    with pytest.raises(Exception) as e:
        track_music.add_track('')
    assert str(e.value) == 'no track to add'

def test_remove_track_from_list():
    track_music = TrackMusic()
    track_music.add_track('hello')
    track_music.add_track('other side')
    track_music.add_track('other')
    track_music.remove_track('other side')
    assert track_music.track_lists() == ['hello', 'other']

def test_return_exception_when_nothing_to_remove():
    track_music = TrackMusic()
    with pytest.raises(Exception) as e:
        track_music.remove_track('other')
    assert str(e.value) == 'track may be empty of track is not in the tracklist'

def test_return_exception_when_track_not_in_list():
    track_music = TrackMusic()
    track_music.add_track('hello')
    track_music.add_track('other side')
    with pytest.raises(Exception) as e:
        track_music.remove_track('other')
    assert str(e.value) == 'track may be empty of track is not in the tracklist'