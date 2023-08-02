from lib.grammerstats import GrammarStats
import pytest 



def test_check_text_not_empty():
    grammer = GrammarStats()
    with pytest.raises(Exception) as e:
        grammer.check('')
    assert str(e.value) == 'it is not be empty'

def test_check_requirements_true():
    grammar = GrammarStats()
    result = grammar.check('Hello are you alright?')
    assert result == True

def test_check_requirements_false():
    grammar = GrammarStats()
    result = grammar.check('hello')
    assert result == False

def test_check_percentage_of_passed_check():
    grammer = GrammarStats()
    assert grammer.percentage_good() == 0
    
    
def test_check_and_return_percetage():
    grammer = GrammarStats()
    grammer.check('Hello are you alright?')
    grammer.check('hello')
    assert grammer.percentage_good() == 50
    

def test_check_and_return_percetage_multi():
    grammer = GrammarStats()
    grammer.check('Hello are you alright?')
    grammer.check(' Hello?')
    grammer.check('Hello are you alright?')
    grammer.check('Hello?')
    grammer.check('Hello are you alright?')
    grammer.check('Hello are you alright?')
    grammer.check('Hello?')
    grammer.check('Hello are you alright?')
    assert grammer.percentage_good() == 88



