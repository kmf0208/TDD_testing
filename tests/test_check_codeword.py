from lib.check_codeword import check_codeword



def test_codeword_password():
    result = check_codeword('horse')
    assert "Correct! Come in."

def test_check_frist_last_character():
    result = check_codeword('hello')
    assert "Close, but nope."

def test_check_wrong_password():
    result = check_codeword('apple')
    assert "WRONG"

