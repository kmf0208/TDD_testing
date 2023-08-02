from lib.diary import Diary

def test_init_empty_list():
    diary = Diary()
    assert diary.all() == []