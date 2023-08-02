from lib.diary import Diary
from lib.dairy_entry import DiaryEntry

"""
initally has an emoty list of entries
"""



def test_adds_to_list_of_diarys():
    diary = Diary()
    entry1 = DiaryEntry('my title 1', 'my content 1')
    entry2 = DiaryEntry('my title 2', 'my content 2')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]


def test_count_words_return_number_of_word_in_diary():
    diary = Diary()
    entry1 = DiaryEntry('my title 1', 'one two')
    entry2 = DiaryEntry('my title 2', 'three four five')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 5
    