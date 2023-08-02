from lib.check_grammer import check_grammer

def test_check_if_endwith_appropraite_sgin():
    result = check_grammer("Hello, this a fine day")
    assert result == False

def test_check_first_letter_cap():
    result = check_grammer("hello, this a fine day.")
    assert result == False

def test_check_first_letter_cap_and_ends_with_right_sgin():
    result = check_grammer("Hello, this a fine day.")
    assert result == True