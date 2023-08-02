import pytest
from lib.present import Present



def test_content_None():
    present = Present()
    content = None
    result = present.wrap(content)
    assert result == None


def test_wrap_content():
    present = Present()
    content = "gift"
    present.wrap(content)
    result = present.unwrap()
    assert result == content


def test_wrap_mulitaple_present():
    present= Present()
    content1 = "gift1"
    content2 = "gift2"
    present.wrap(content1)
    with pytest.raises(Exception) as e:
        present.wrap(content2)
    assert str(e.value) == "A contents has already been wrapped."
        
def test_unwarp_empty_content():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."
