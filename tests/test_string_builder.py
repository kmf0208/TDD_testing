from lib.string_builder import StringBuilder

def test_string_buider_check_empty_str():
    string_builder = StringBuilder()
    result = string_builder.output()
    assert result == ""

def test_string_builder_adding_string():
    string_builder = StringBuilder()
    string_builder.add('khalifa')
    result = string_builder.output()
    assert result == "khalifa"


def test_string_builder_adding_multi_strings():
    string_builder = StringBuilder()
    string_builder.add('khalifa')
    string_builder.add('fadel')
    result = string_builder.output()
    assert result == "khalifafadel"

def test_string_builder_adding_multi_strings():
    string_builder = StringBuilder()
    string_builder.add('khalifa')
    string_builder.add('fadel')
    result = string_builder.size()
    assert result == 12


def test_string_builder_adding_multi_strings():
    string_builder = StringBuilder()
    string_builder.add('khalifa')
    string_builder.add(' ')
    string_builder.add('fadel')
    result = string_builder.output()
    assert result == "khalifa fadel"

