from lib.password_manager import PasswordChecker
import pytest



def test_check_length():
    passwordChecker = PasswordChecker()
    num = "12345678"
    assert passwordChecker.check(num) == True

def test_exception_manager():
    passwordChecker = PasswordChecker()
    with pytest.raises(Exception) as r:
        passwordChecker.check("12321")
    result = str(r.value)
    assert result == "Invalid password, must be 8+ characters."