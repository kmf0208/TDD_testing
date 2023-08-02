from lib.greet import greet

def test_greet():
    result = greet('Kay')
    assert result == "Hello, Kay"