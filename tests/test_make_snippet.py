from lib.make_snippet import make_snippet


def test_empty_string_words():
    assert make_snippet("") == ""

def test_two_words():
    assert make_snippet("hello hello") == "hello hello"

def test_three_words():
    assert make_snippet("hello hello hello") == "hello hello hello"

def test_check_for_five_words_():
    assert make_snippet("hello hello hello hello hello hello") == "hello hello hello hello hello..."
