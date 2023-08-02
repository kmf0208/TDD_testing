from lib.count_words import count_words

def test_check_for_empty_string():
    assert count_words("") == 0

def test_check_number_of_strings():
    assert count_words("hello hello hello hello") == 4


