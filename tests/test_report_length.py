from lib.report_length import report_length

def test_report_length():
    result = report_length('')
    assert f"This string was 0 characters long."

def test_report_length_hello():
    result = report_length('Hello')
    assert f"This string was 5 characters long."
