from lib.estimate_reading_time import estimate_reading_time
import pytest

def test_check_reading_200_word_a_minute():
    text = ' '.join('word' for i in range(0, 200))
    result = estimate_reading_time(text)
    assert result == 1.0

def test_check_reading_400_word_a_minute():
    text = ' '.join('word' for i in range(0, 400))
    result = estimate_reading_time(text)
    assert result == 2.0

def test_check_empty_string():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    message = str(e.value)
    assert message == "sorry it is an empty string"