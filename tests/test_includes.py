from lib.includes import includes
import pytest
"""
As a user
So that I can keep track of my tasks
I want to check if a text includes the string TODO.
"""

"""
check if the string the strin is empty
returns an exception
"""
def test_check_for_empty_string():
    with pytest.raises(Exception) as e:
        includes("")
    assert str(e.value) == "no tasks"
    
"""
check if todo is in a string
return True
"""
def test_TODO_in_string():
    assert includes("HELLO HELLO TODO") == True

"""
if todo not in a string 
return false
"""
def test_TODO_in_not_string():
    result = includes("hello hello")
    assert result == False
