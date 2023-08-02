from lib.dairy_entry import DiaryEntry
import pytest


def test_raise_an_error_empty_tile():
    with pytest.raises(Exception) as e:
         DiaryEntry('', 'ergf')
    assert str(e.value) == "sorry no title to show"

def test_raise_an_error_empty_contents():
    with pytest.raises(Exception) as e:
         DiaryEntry('ytt', '')
    assert str(e.value) == "sorry no title to show"
        

def test_format_title_content():
    dairy_entry = DiaryEntry("Hello", 'something')
    result = dairy_entry.format()
    assert result == "Hello: something"


def test_count_titile_contents():
     dairy_entry = DiaryEntry("Hello", 'something')
     result = dairy_entry.count_words()
     assert result == 2


def  test_reading_time_per_min():
    dairy_entry = DiaryEntry("Hello", 'something two')
    result = dairy_entry.reading_time(2)
    assert result == 1

def  test_reading_time_per_min_for_more_word():
    dairy_entry = DiaryEntry("Hello", 'something two three four')
    result = dairy_entry.reading_time(2)
    assert result == 2

def  test_reading_time_per_min_for_more_word_for_three_words():
    dairy_entry = DiaryEntry("Hello", 'something two three')
    result = dairy_entry.reading_time(2)
    assert result == 2

def  test_reading_time_per_min_for_zero_words():
    dairy_entry = DiaryEntry("Hello", 'something two three')
    with pytest.raises(Exception) as e:
        dairy_entry.reading_time(0)
    assert str(e.value) == 'sorry can not calculate time with wpm of zero'



def test_reading_chunk_of_two_wpm_two_minutes():
    dairy_entry = DiaryEntry("Hello", 'one two three four five six')
    result = dairy_entry.reading_chunk(2, 2)
    assert result == 'one two three four'

def test_reading_chunk_of_two_wpm_two_and_min_called_multi_times():
    dairy_entry = DiaryEntry("Hello", 'one two three four five six')
    assert dairy_entry.reading_chunk(2, 1) == 'one two'
    assert dairy_entry.reading_chunk(1, 1) == 'three'
    assert dairy_entry.reading_chunk(2, 1) == 'four five'


def test_reading_chunk_of_two_wpm_two_and_min_called_repetedly_multi_times():
    dairy_entry = DiaryEntry("Hello", 'one two three four five six')
    assert dairy_entry.reading_chunk(2, 2) == 'one two three four'
    assert dairy_entry.reading_chunk(2, 2) == 'five six'
    assert dairy_entry.reading_chunk(2, 2) == 'one two three four'

def test_reading_chunk_with_exact_ending():
    dairy_entry = DiaryEntry("Hello", 'one two three four five six')
    assert dairy_entry.reading_chunk(2, 2) == 'one two three four'
    assert dairy_entry.reading_chunk(2, 1) == 'five six'
    assert dairy_entry.reading_chunk(2, 2) == 'one two three four'